import { defineConfig } from 'astro/config';
import remarkExtractJsonLd from './src/plugins/remark-extract-jsonld.mjs';
import rehypeWrapTables from './src/plugins/rehype-wrap-tables.mjs';

// Netlify sets URL to the site's primary address during builds.
const site = process.env.URL || 'http://localhost:4321';

export default defineConfig({
  site,
  trailingSlash: 'ignore',
  markdown: {
    remarkPlugins: [remarkExtractJsonLd],
    rehypePlugins: [rehypeWrapTables],
  },
});
