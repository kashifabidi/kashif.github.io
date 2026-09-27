# Multiplayer Competitive Radar

A three-agent [CrewAI](https://docs.crewai.com) pipeline that finds where rival
multiplayer games are failing their players, turns that into an SEO landing
page, and builds a creator outreach playbook for playtest recruiting.

| Step | Agent | Output file |
|------|-------|-------------|
| 1 | Competitor & Sentiment Intelligence Scout | `output/01_competitor_briefing.md` |
| 2 | Gaming SEO & Narrative Engineer | `output/02_landing_page.md` |
| 3 | Streamer & Clan Lead Generator | `output/03_outreach_playbook.md` |

Each step receives the earlier steps' output as context, so the landing page is
built on the briefing and the pitch reuses both.

## Setup

```bash
cd crews/multiplayer_radar
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

export ANTHROPIC_API_KEY=...        # or the key for whichever model you set
export SERPER_API_KEY=...           # optional: live Google search for the radar agent
export CREW_MODEL=anthropic/claude-sonnet-5   # optional: any LiteLLM model id
```

Without `SERPER_API_KEY` the radar agent works from model knowledge plus page
scraping only, so double-check its complaints and keywords before publishing.

## Run

```bash
python crew.py \
  --genre "extraction shooter" \
  --competitors "Escape from Tarkov, Arena Breakout: Infinite, Hunt: Showdown 1896" \
  --our-game "Your Game Name" \
  --playtest-url "https://yourgame.com/playtest"
```

## Before you publish

- Replace every `[CONFIRM]` in the landing page with facts from the studio.
- Check each competitor claim against its cited source; comparison pages that
  overstate a rival's problems lose trust (and can draw legal complaints).
- Validate the FAQ JSON-LD with Google's Rich Results Test.
