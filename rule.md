# UI - Neogen Inspired 3D Design Rules

## 1. Core Aesthetic (WebGL Wave Terrain)
- The hero section background MUST NOT be a CSS gradient or image.
- It MUST be a `react-three-fiber` WebGL canvas rendering an animated 3D wave/terrain mesh.
- The visual style is dark/black valleys with deep crimson red, glowing peaks using shader materials or lighting effects.

## 2. Background Layering & Z-Index Safety
- The Three.js `<Canvas>` wrapper MUST use `absolute inset-0 z-0 pointer-events-none overflow-hidden`.
- Foreground content (text, buttons, hero container) MUST use `relative z-10` to sit above the WebGL canvas.

## 3. Performance
- Ensure the 3D animation loop uses `useFrame` properly to adjust the time uniform (`uTime`) for the vertex displacement without causing React re-renders.
# Homepage Specific Rules (Nexbit Agency)

## 1. Hero Section & 3D WebGL Background
- **Background Implementation:** The hero background MUST use a Three.js / React Three Fiber WebGL canvas (`<Canvas>`) rendering a 3D animated wave/terrain plane (`PlaneGeometry`).
- **3D Aesthetic:** Deep pitch-black base/valleys with glowing crimson red (`#8b0000` to `#ff0000`) peaks animated via noise/vertex shaders over time (`uTime`).
- **Hero Layering & Z-Index:**
  - WebGL Canvas container MUST be `absolute inset-0 z-0 pointer-events-none overflow-hidden`.
  - Hero text, badges, and CTA buttons MUST be wrapped in a `relative z-10` container.
- **Hero Copy & CTAs:**
  - Large bold heading with AI automation agency focus.
  - Primary CTA: Crimson red glowing button (`bg-red-600 hover:bg-red-500 shadow-lg shadow-red-900/50`).
  - Secondary CTA: Glassmorphism style (`backdrop-blur-md bg-white/5 border border-white/10 hover:bg-white/10`).

## 2. Key Metrics & Proof Banner (Below Hero)
- Positioned directly below the hero section.
- Layout: Glassmorphic ticker or grid (`backdrop-blur-lg bg-neutral-900/60 border border-neutral-800`).
- Display key agency stats (e.g., "74.75 Cr+ Client ROI", "AI-First Automation", "24/7 Executing Systems").

## 3. Services / Solutions Grid
- Display 3–4 core offerings (e.g., AI Workflow Automation, Conversational AI, Custom AI Agents).
- Layout: Responsive 3-column grid (`grid grid-cols-1 md:grid-cols-3 gap-6`).
- Card Styling:
  - Dark background (`bg-neutral-900/80 border border-neutral-800`).
  - Hover transition: Subtle scale up (`hover:-translate-y-1`), red glowing border (`hover:border-red-500/50`).

## 4. Featured Case Studies Preview
- Showcase 2 top client success stories on the homepage before linking to the full `/case-studies` page.
- Emphasize visual thumbnails, metric badges, and client results.

## 5. Global Homepage Layout Safeguards
- Main wrapper MUST have `bg-black text-white overflow-x-hidden min-h-screen`.
- Every section MUST explicitly declare its `z-index` so background elements never block text or clickable buttons.
- All interactive links and buttons MUST remain clickable above background overlays (`pointer-events-auto`).
# Elevix Digital Global Design & Graphics Rules

# Nexbit Agency Structural & Content Rules

## 1. Services Page Layout & Component Structure
- **Header Section:**
  - Dynamic page header layout following the 2-column header pattern: bold primary headline on the left, descriptive subtext on the right.
  - Sub-badge header tag displaying overall core service count and total capability offerings.
- **6-Pillar Services Grid:**
  - Layout: 2-column responsive grid displaying Nexbit's 6 core service offerings (01 to 06).
  - Each Service Card Must Contain:
    1. Large background sequence number (`01` through `06`).
    2. Service Title & Overview paragraph.
    3. Count badge (e.g., "X SERVICES") paired with tech stack highlights (e.g., custom AI frameworks, tools, platforms).
    4. Sub-service capability pills listing specific deliverables.

## 2. Footer & Call-to-Action (CTA) Constraints
- **NO NEOGEN COPY:** Strictly DO NOT use text like "READY TO SCALE THE UNSCALABLE?", Neogen address details, or Indian phone numbers/locations from the reference video.
- **CTA Section:** Match the Nexbit homepage bottom CTA section ("Ready to transform your business with custom AI automation?"). Include the strategy call booking button.
- **Locations & Footers:** Use Nexbit's designated global markets (e.g., Australia / target service regions) matching the main homepage footer configuration.
- **Footer Navigation:** Include company links (Our Story, Case Studies, Blogs, Services, Contact), legal pages, social links, and the full-width Nexbit brand watermark banner at the very bottom.

## 3. Data Integrity Directive
- Treat the video clip purely as a **UI/UX layout and structural reference**.
- NEVER copy client names, phone numbers, addresses, or specific service counts verbatim from the screen recording. Always inject Nexbit agency content into the structured layout.u have to make same address map location as in our services and home page 