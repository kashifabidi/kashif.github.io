"""Multiplayer Competitive Radar crew.

Three agents run in sequence:
  1. Radar scout      -> competitor pain points + alternative-intent keywords
  2. SEO architect    -> "Why players are leaving X for Y" landing page (Markdown + FAQ schema)
  3. Lead scout       -> creator/clan playtest outreach pitch + qualification checklist

Run:
    python crew.py --genre "extraction shooter" \
        --competitors "Escape from Tarkov, Arena Breakout: Infinite, Hunt: Showdown 1896" \
        --our-game "Our Game" --playtest-url "https://example.com/playtest"
"""

import argparse
import os
from pathlib import Path

from crewai import LLM, Agent, Crew, Process, Task

OUTPUT_DIR = Path(__file__).parent / "output"

# Model is configurable; any LiteLLM-style id works (e.g. "anthropic/claude-sonnet-5").
llm = LLM(model=os.getenv("CREW_MODEL", "anthropic/claude-sonnet-5"), temperature=0.4)


def research_tools():
    """Web search/scrape tools for the radar agent.

    Search needs SERPER_API_KEY. Without it the radar agent still runs, but works
    from model knowledge only, so its findings should be treated as unverified.
    """
    try:
        from crewai_tools import ScrapeWebsiteTool, SerperDevTool
    except ImportError:
        return []
    tools = [ScrapeWebsiteTool()]
    if os.getenv("SERPER_API_KEY"):
        tools.insert(0, SerperDevTool())
    return tools


# ==========================================
# 1. THE COMPETITIVE RADAR BOT
# ==========================================
radar_agent = Agent(
    role="Competitor & Sentiment Intelligence Scout",
    goal="Identify player pain points, pricing complaints, and server gripes in rival {genre} games.",
    backstory=(
        "An elite game industry analyst with a sharp eye for market voids. "
        "You scour Steam forums, Reddit threads, and search queries to detect "
        "where existing multiplayer titles are failing their player base. "
        "You always cite where a complaint comes from and never invent quotes or stats."
    ),
    tools=research_tools(),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# ==========================================
# 2. THE EDITORIAL & PROGRAMMATIC ARCHITECT
# ==========================================
seo_architect = Agent(
    role="Gaming SEO & Narrative Engineer",
    goal="Turn competitor pain points into high-ranking 'Alternative-To' teardowns and landing pages.",
    backstory=(
        "A veteran game journalist turned technical SEO master. You know that gamers "
        "hate corporate marketing speak. You write sharp, authentic, technically credible "
        "comparison pages that rank for 'Games like X' and convert searchers into playtesters. "
        "You criticise competitors only with facts the research supports."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# ==========================================
# 3. THE CREATOR / PLAYTESTER LEAD SCOUT (Inside Sales)
# ==========================================
lead_scout = Agent(
    role="Streamer & Clan Lead Generator",
    goal="Discover micro-creators, Discord community leaders, and competitive teams who play {genre} games.",
    backstory=(
        "A hyper-focused community scout. In gaming, 'inside sales' means getting closed alpha "
        "keys into the hands of 500-follower streamers and competitive guild leaders who command "
        "actual player swarms. You build targeted outreach rosters."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# --- Define Tasks ---
task_identify_gaps = Task(
    description=(
        "Analyze the top 3 incumbent games in the {genre} genre: {competitors}. "
        "For each, pinpoint their 3 biggest community complaints (e.g., predatory monetization, "
        "netcode, cheating, lack of updates), with the source (subreddit, Steam review trend, forum) "
        "and a rough severity. Then name the single most vulnerable competitor. "
        "Finally map out 5 high-intent Google search keywords players use to look for alternatives "
        "(e.g. 'games like <competitor>', '<competitor> alternative no pay to win')."
    ),
    expected_output=(
        "A structured Markdown briefing: one section per competitor with a complaints table "
        "(complaint | evidence/source | severity), a 'Primary target' line naming the most "
        "vulnerable competitor, and a numbered list of 5 long-tail search queries with the "
        "search intent behind each."
    ),
    agent=radar_agent,
    output_file=str(OUTPUT_DIR / "01_competitor_briefing.md"),
)

task_generate_landing_page = Task(
    description=(
        "Using the briefing's primary target and search queries, draft a complete Markdown landing page "
        "titled 'Why Players Are Leaving <Primary target> for {our_game}'. "
        "Focus on cost efficiency, netcode integrity, and pure gameplay. Work the 5 queries into the "
        "title, H2s and body naturally. Include a meta title (<60 chars), meta description (<155 chars), "
        "a comparison table, an FAQ section, and a matching JSON-LD FAQPage schema block. "
        "Every call-to-action points to {playtest_url}. Do not claim features for {our_game} that "
        "the brief does not give you; mark anything needing studio confirmation as [CONFIRM]."
    ),
    expected_output=(
        "Production-ready Markdown file: YAML front matter (title, description, slug, keywords), "
        "H1, section headers, comparison table, FAQ, a ```json FAQPage schema block, and a clear "
        "call-to-action for playtest signups."
    ),
    agent=seo_architect,
    context=[task_identify_gaps],
    output_file=str(OUTPUT_DIR / "02_landing_page.md"),
)

task_hunt_influencers = Task(
    description=(
        "Draft an outreach criteria framework for inside playtest recruiting for {our_game}. "
        "Define who qualifies (Twitch/YouTube micro-creators, Discord community leads, competitive "
        "teams/clans in the {genre} scene) and where to find them. "
        "Specify the exact pitch angle for micro-creators frustrated with the incumbents' pain points "
        "from the briefing, offering exclusive early access and studio co-branding perks, and link "
        "the landing page at {playtest_url}."
    ),
    expected_output=(
        "A Markdown playbook with: (1) a qualification checklist with scoring (follower range, "
        "avg CCV, genre focus, engagement, brand safety), (2) where-to-find search strings for "
        "Twitch, YouTube and Discord, (3) pitch templates for creators, Discord leads and clans "
        "(subject line + DM/email body, under 120 words each), and (4) a 2-step follow-up cadence."
    ),
    agent=lead_scout,
    context=[task_identify_gaps, task_generate_landing_page],
    output_file=str(OUTPUT_DIR / "03_outreach_playbook.md"),
)

# --- Assemble the Crew ---
multiplayer_crew = Crew(
    agents=[radar_agent, seo_architect, lead_scout],
    tasks=[task_identify_gaps, task_generate_landing_page, task_hunt_influencers],
    process=Process.sequential,
    verbose=True,
)


def main():
    parser = argparse.ArgumentParser(description="Run the multiplayer competitive radar crew.")
    parser.add_argument("--genre", default="extraction shooter")
    parser.add_argument(
        "--competitors",
        default="Escape from Tarkov, Arena Breakout: Infinite, Hunt: Showdown 1896",
        help="Comma-separated incumbent titles to analyse.",
    )
    parser.add_argument("--our-game", default="Our Game")
    parser.add_argument("--playtest-url", default="https://example.com/playtest")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(exist_ok=True)
    result = multiplayer_crew.kickoff(
        inputs={
            "genre": args.genre,
            "competitors": args.competitors,
            "our_game": args.our_game,
            "playtest_url": args.playtest_url,
        }
    )
    print("\n=== Final output ===\n")
    print(result.raw)
    print(f"\nAll task outputs saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
