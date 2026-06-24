/** @type {import('tailwindcss').Config} */
export default {
  content: ["./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}"],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        brand: {
          50: "#f0f5ff",
          100: "#e0eaff",
          200: "#c7d7fe",
          300: "#a4bcfd",
          400: "#8098f9",
          500: "#6172f3",
          600: "#444ce7",
          700: "#3538cd",
          800: "#2d31a6",
          900: "#2b2f83",
        },
        adhd: {
          orange: "#F97316",
          purple: "#8B5CF6",
          blue: "#3B82F6",
          green: "#10B981",
          pink: "#EC4899",
          teal: "#14B8A6",
          red: "#EF4444",
          yellow: "#F59E0B",
          indigo: "#6366F1",
          lime: "#84CC16",
          violet: "#A855F7",
        },
      },
      fontFamily: {
        sans: [
          '"Inter"',
          '"Noto Sans SC"',
          '"PingFang SC"',
          '"Microsoft YaHei"',
          "sans-serif",
        ],
        display: ['"Inter"', '"Noto Sans SC"', "sans-serif"],
      },
      typography: {
        DEFAULT: {
          css: {
            maxWidth: "75ch",
            color: "var(--tw-prose-body)",
            a: {
              color: "#6172f3",
              textDecoration: "underline",
              fontWeight: "500",
            },
          },
        },
      },
    },
  },
  plugins: [],
};
