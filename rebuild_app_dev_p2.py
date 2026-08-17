import re

with open(r'c:\Elevix Digital\services sub folder\app-development.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 7. Process Section
content = content.replace('Engineered in Next.js 15 (or WordPress / Shopify when that\'s the right call), with a hard performance budget — LCP under 2.5s, INP under 200ms, CLS under 0.1. CRO patterns baked in: clear primary CTAs, single-column forms, social proof at decision points.', 'Engineered in Swift, Kotlin, React Native, or Flutter, with a hard performance budget — sub-second launch, 60fps scrolling, zero memory leaks. UI patterns baked in: thumb-friendly navigation, skeleton loaders, and instant touch feedback.')
content = content.replace('Rigorous cross-device testing, SEO technical audit, and final Lighthouse verification. We handle the deployment and provide you with complete code ownership, hosting access, and a recorded training session.', 'Rigorous testing on real iOS and Android devices, API stress tests, and final App Store compliance verification. We handle the App Store and Google Play deployments and provide you with complete code ownership and cloud infrastructure access.')

# 8. Why Elevix Digital
content = content.replace('Why teams pick Elevix Digital over generic web agencies', 'Why teams pick Elevix Digital over generic app agencies')
content = content.replace('We engineer production-grade websites that survive traffic spikes, Google core updates, and three years of content additions without a rebuild. Four reasons clients move to us.', 'We engineer production-grade mobile applications that survive OS updates, millions of active users, and massive feature expansions without a codebase rewrite. Four reasons clients move to us.')
content = content.replace('Lighthouse 90+ is the baseline, not a stretch goal. Speed budgets enforced in CI, image pipelines tuned, third-party scripts ruthlessly audited.', 'Fluid 60fps animations are the baseline, not a stretch goal. Bundle sizes strictly monitored, API calls optimized, and background processes battery-profiled.')

content = content.replace('SEO-native architecture', 'API-first architecture')
content = content.replace('Semantic HTML, schema.org markup, server-rendered metadata, sitemap automation, llms.txt — every site ships ready for Google + AI Overviews.', 'REST and GraphQL APIs, offline-first syncing, secure token management, WebSocket integration — every app ships ready for scalable user growth.')

content = content.replace('Post-launch partnership', 'Post-launch maintenance')
content = content.replace('Most agencies disappear after invoice three. We retain you — security patches, uptime monitoring, conversion experiments, content updates. The site keeps compounding.', 'Most agencies disappear after launch. We retain you — iOS/Android SDK updates, server-side scaling, bug tracking via Sentry, and new feature rollouts. The app keeps compounding.')

# 9. Technology Stack
content = content.replace('The Elevix Digital Web Stack', 'The Elevix Digital Mobile Stack')
content = content.replace('Next.js 15 (App Router, RSC, edge runtime), TypeScript strict, Tailwind v4, shadcn/ui primitives, Framer Motion + GSAP for motion.', 'React Native, Flutter, Swift for iOS, Kotlin for Android, Reanimated for 60fps fluid gesture-driven UI components.')

content = content.replace('CMS + Storefront', 'Backend + Cloud')
content = content.replace('Sanity, Payload, or Strapi for headless content. Shopify Hydrogen + WooCommerce for commerce. WordPress when editing UX trumps everything else.', 'Firebase for real-time sync, Node.js microservices on AWS, scalable PostgreSQL databases, and Supabase for authentication and edge functions.')

content = content.replace('Vercel, Dokploy, and Railway for deployment, Cloudflare for edge delivery, GitHub Actions for CI, Sentry for error tracking, Plausible / GA4 for analytics, GHL for forms and CRM.', 'Apple App Store Connect and Google Play Console for deployment, Bitrise and GitHub Actions for mobile CI/CD, Sentry and Crashlytics for crash tracking, PostHog for mobile analytics.')

with open(r'c:\Elevix Digital\services sub folder\app-development.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced Process, Why Us, and Technology Stack.")
