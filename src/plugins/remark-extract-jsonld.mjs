/**
 * Pulls <script type="application/ld+json"> blocks out of Markdown bodies,
 * validates them as JSON, and exposes them as `jsonLd` in
 * remarkPluginFrontmatter so the layout can place them in <head>.
 * The blocks are removed from the rendered body.
 */
const JSON_LD_RE = /<script\s+type=["']application\/ld\+json["']\s*>([\s\S]*?)<\/script>/gi;

export default function remarkExtractJsonLd() {
  return (tree, file) => {
    const found = [];

    const walk = (node) => {
      if (!Array.isArray(node.children)) return;
      node.children = node.children.filter((child) => {
        if (child.type === 'html' && /application\/ld\+json/i.test(child.value)) {
          for (const match of child.value.matchAll(JSON_LD_RE)) {
            try {
              found.push(JSON.parse(match[1]));
            } catch (err) {
              const where = file.path || file.history?.[0] || 'unknown file';
              throw new Error(`Invalid JSON-LD in ${where}: ${err.message}`);
            }
          }
          return false;
        }
        walk(child);
        return true;
      });
    };

    walk(tree);

    const astro = (file.data.astro ??= {});
    astro.frontmatter ??= {};
    astro.frontmatter.jsonLd = found;
  };
}
