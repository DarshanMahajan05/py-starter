import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* Performance & correctness */
  reactStrictMode: true,

  /* Allow local TTF fonts to be served */
  experimental: {
    optimizeCss: false,
  },

  images: {
    formats: ["image/avif", "image/webp"],
    deviceSizes: [320, 375, 640, 768, 1024, 1280, 1536, 1920],
  },
};

export default nextConfig;
