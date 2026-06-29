import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const articles = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/articles" }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string().optional(),
    description: z.string().optional(),
    date: z.string(),
    category: z.string(),
    categoryId: z.string(),
    categoryEn: z.string().optional(),
    tags: z.array(z.string()).optional(),
    readingTime: z.number().optional(),
    slug: z.string().optional(),
    topicId: z.string().optional(),
    angle: z.string().optional(),
    rank: z.number().optional(),
    score: z.number().optional(),
    sourceCount: z.number().optional(),
    toolsCited: z.array(z.string()).optional(),
    isEvolved: z.boolean().optional(),
  }),
});

export const collections = { articles };
