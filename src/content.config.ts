import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const page = z.object({
  title: z.string(),
  description: z.string(),
  slug: z.string().regex(/^[a-z0-9-]+$/, 'slug must be a single lowercase path segment').optional(),
  date: z.coerce.date().optional(),
  draft: z.boolean().default(false),
  keywords: z.array(z.string()).optional(),
});

const heroes = defineCollection({
  loader: glob({ pattern: '*.md', base: './content/heroes' }),
  schema: page,
});

const zoneBriefings = defineCollection({
  loader: glob({ pattern: '*.md', base: './content/zone-briefings' }),
  schema: page,
});

export const collections = { heroes, 'zone-briefings': zoneBriefings };
