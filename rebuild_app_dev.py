import re

with open(r'c:\Elevix Digital\services sub folder\app-development.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Breadcrumbs
content = content.replace('>Web Development</span>', '>App Development</span>')

# 2. Hero Section
content = content.replace('WEBSITE DEVELOPMENT COMPANY • GULBERG, LAHORE', 'APP DEVELOPMENT COMPANY • GULBERG, LAHORE')
content = content.replace('The website development company<br>\n                    engineered to scale', 'The mobile app development company<br>\n                    engineered to scale')
content = content.replace('Web development Lahore — a Gulberg-based website development company shipping Next.js, WordPress, Shopify, and custom web development.', 'App development Lahore — a Gulberg-based app development company shipping iOS, Android, React Native, and Flutter applications.')
content = content.replace('Engineered for Core Web Vitals, SEO, and conversion from day one. No plugin bloat, no template churn, no rip-and-replace at scale. Every build ships to a Lighthouse 90+ performance budget.', 'Engineered for fluid 60fps performance, intuitive UX, and user retention from day one. No hybrid sluggishness, no template churn, no rip-and-replace at scale. Every build ships to an App Store-ready standard.')

# Update the little code block
content = content.replace('engine: <span class="text-[#A3A3A3]">' + "'Next.js'" + '</span>', 'engine: <span class="text-[#A3A3A3]">' + "'React Native'" + '</span>')
content = content.replace('alt="Web Dev 3D Concept"', 'alt="App Dev 3D Concept"')

# 3. In Short Section
content = content.replace('What does a website development company in Lahore do?', 'What does an app development company in Lahore do?')
content = content.replace('Elevix Digital is a website development company in Lahore, Pakistan that engineers sites to rank, convert, and scale. We build on Next.js, WordPress, and Shopify — 15+ websites shipped at a 85+ average Lighthouse score, with SEO and CRO baked in from the first commit rather than retrofitted.', 'Elevix Digital is an app development company in Lahore, Pakistan that engineers mobile apps to scale, retain, and perform. We build on Swift, Kotlin, React Native, and Flutter — 10+ mobile apps shipped at a 4.8+ average App Store rating, with intuitive UX and fluid performance baked in from the first commit rather than retrofitted.')
content = content.replace('Whether it\'s a custom web app, a WordPress build, an e-commerce store, or a campaign landing page, performance and search visibility are engineered in, not bolted on later.', 'Whether it\'s a native iOS app, an Android build, a cross-platform solution, or a minimum viable product, performance and fluid UI are engineered in, not bolted on later.')

# 4. Definition & Stack Section
content = content.replace('What makes a high-performance website in 2026?', 'What makes a high-performance mobile app in 2026?')
content = content.replace('A high-performance website in 2026 is engineered, not templated. It loads under 2.5 seconds on a mid-tier Android phone (the <span class="text-white border-b border-white/30">Core Web Vitals</span> LCP threshold), hits CLS under 0.1 and INP under 200ms, ranks on Google because the markup is semantic and the schema is correct, and converts because the funnel was designed before a single component was coded.', 'A high-performance mobile app in 2026 is engineered, not templated. It launches instantly on a mid-tier phone (the <span class="text-white border-b border-white/30">App Startup Time</span> threshold), hits 60fps animations, secures data because the architecture is robust and the API is encrypted, and retains users because the journey was mapped before a single view was coded.')
content = content.replace('As a website development company in Lahore, every Elevix Digital build runs on the <span class="text-white font-semibold">Elevix Web Stack — Next.js 15</span>, headless CMS, edge rendering on Vercel, and a Core Web Vitals budget enforced in CI from day one.', 'As an app development company in Lahore, every Elevix Digital build runs on the <span class="text-white font-semibold">Elevix Mobile Stack — React Native/Flutter</span>, scalable cloud backends, edge APIs on AWS/Firebase, and a strict performance budget enforced in CI from day one.')

content = content.replace('THE ELEVIX WEB STACK', 'THE ELEVIX MOBILE STACK')
content = content.replace('"Next.js 15 + headless CMS + a Core Web Vitals budget enforced in CI. SEO and conversion are baked into the architecture, not bolted on after launch."', '"React Native/Flutter + scalable cloud APIs + a 60fps performance budget enforced in CI. UX and retention are baked into the architecture, not bolted on after launch."')

content = content.replace('LIGHTHOUSE SCORE*', 'APP STORE RATING*')
content = content.replace('85+', '4.8+')
content = content.replace('<span class="text-kinetic-red font-display font-bold text-[32px]">&lt;2.5s</span>', '<span class="text-kinetic-red font-display font-bold text-[32px]">&lt;1.0s</span>')
content = content.replace('LCP TARGET*', 'STARTUP TIME*')
content = content.replace('*Median outcomes across Elevix Digital production builds, measured on Mobile Slow 4G.', '*Median outcomes across Elevix Digital production builds, measured on mid-tier mobile devices.')

# 5. Metrics
content = content.replace('WEBSITES SHIPPED', 'APPS PUBLISHED')
content = content.replace('AVG LIGHTHOUSE SCORE', 'AVG APP STORE RATING')
content = content.replace('DOMAINS UNDER MANAGEMENT', 'ACTIVE MONTHLY USERS')
content = content.replace('10+', '100K+')
content = content.replace('BUILDING FOR THE WEB', 'BUILDING FOR MOBILE')

# 6. Capabilities Bento Grid
content = content.replace('Custom Next.js Apps', 'iOS App Development')
content = content.replace('High-performance, edge-rendered web applications built for speed and infinite scalability.', 'High-performance, native iOS applications built with Swift for unparalleled Apple ecosystem integration.')

content = content.replace('E-Commerce Stores', 'Android App Development')
content = content.replace('Scalable Shopify and custom commerce solutions built to convert and handle high traffic volumes across global markets.', 'Scalable Android solutions built with Kotlin to reach billions of devices with perfect fluid performance.')

content = content.replace('Corporate Sites', 'React Native & Flutter')
content = content.replace('Websites for B2B brands that function as 24/7 sales engines rather than static digital brochures.', 'Cross-platform apps that deploy to both iOS and Android simultaneously without compromising on native-like speed.')

content = content.replace('Web App Modernization', 'App UI/UX Design')
content = content.replace('Migrating legacy React or Vue SPAs to server-rendered Next.js architectures for immediate SEO and performance gains.', 'Crafting intuitive, thumb-friendly interfaces that drive engagement, retention, and 5-star user reviews.')

content = content.replace('Headless Commerce', 'App Maintenance & Scaling')
content = content.replace('Decoupled frontends for enterprise e-commerce, linking Vercel/Next.js with Shopify Plus or Commerce Layer.', 'Continuous updates, bug fixes, feature rollouts, and cloud backend scaling to keep your app store-ready 24/7.')


with open(r'c:\Elevix Digital\services sub folder\app-development.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced Hero, Definition, Metrics, and Capabilities grid.")
