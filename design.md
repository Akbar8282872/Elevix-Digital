# Design
## Elevix Digital
Kinetic Neo-Media: DESIGN.md
---
name: Kinetic Neo-Media
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#212121'
  surface-container-high: '#2b2a2a'
  surface-container-highest: '#363535'
  on-surface: '#e3e3e3'
  on-surface-variant: '#c4c7c5'
  outline: '#8e918f'
  outline-variant: '#444746'
  primary: '#e8282b'
  on-primary: '#ffffff'
  primary-container: '#ffdad4'
  on-primary-container: '#410001'
  secondary: '#775651'
  on-secondary: '#ffffff'
  secondary-container: '#ffdad4'
  on-secondary-container: '#2c1512'
  tertiary: '#705c2e'
  on-tertiary: '#ffffff'
  tertiary-container: '#fbe0a6'
  on-tertiary-container: '#251a00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'

typography:
  font-family: 'Montserrat', sans-serif
  display-large:
    weight: 900
    size: 120px
    line-height: 1.1
    letter-spacing: -0.05em
    case: uppercase
  headline-medium:
    weight: 800
    size: 48px
    line-height: 1.2
    case: uppercase
  body-large:
    weight: 400
    size: 18px
    line-height: 1.6
    letter-spacing: 0.02em

spacing:
  base: 8px
  section-gap: 120px
  container-padding: 64px

components:
  buttons:
    primary:
      bg: '#e8282b'
      text: '#ffffff'
      shape: rectangular
      weight: bold
      hover: 'scale-105, brightness-110'
  cards:
    dark-glass:
      bg: 'rgba(28, 27, 27, 0.8)'
      border: '1px solid rgba(232, 40, 43, 0.2)'
      backdrop-blur: 10px
      olors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#212121'
  surface-container-high: '#2b2a2a'
  surface-container-highest: '#363535'
  primary: '#e8282b' # Kinetic Red
  on-primary: '#ffffff'
  on-surface: '#e3e3e3'
  outline: '#8e918f'
  glass-bg: 'rgba(19, 19, 19, 0.85)'
  glass-blur: '12px'

typography:
  font-family: 'Montserrat', sans-serif
  display-large: { weight: 900, size: 120px, letter-spacing: -0.05em, case: uppercase }
  headline-large: { weight: 800, size: 64px, letter-spacing: -0.02em, case: uppercase }
  label-mono: { font: 'JetBrains Mono', weight: 400, size: 14px, case: uppercase }

layout:
  section-gap: 160px
  container-max-width: 1440px
  grid-pillars: 'repeat(3, 1fr)'

components:
  nav-bar:
    style: 'fixed, sticky, glassmorphism'
    hover: 'line-through decoration-2 decoration-primary'
  cta-button:
    primary: 'bg-primary text-white font-bold uppercase py-4 px-10'
    ghost: 'border border-white/20 hover:bg-white hover:text-black'
  service-card:
    numbering: 'font-mono text-primary text-2xl mb-4'
    border: '1px solid #2b2a2a'
---
---
name: Kinetic Neo-Media
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2121'
  surface-container-high: '#292b2b'
  surface-container-highest: '#343636'
  on-surface: '#e1e3e2'
  on-surface-variant: '#c0c9c8'
  outline: '#8a9392'
  outline-variant: '#404948'
  primary: '#e8282b'
  on-primary: '#ffffff'
  primary-container: '#93000a'
  on-primary-container: '#ffdad6'
  secondary: '#b0ccc9'
  on-secondary: '#1b3533'
  secondary-container: '#324b49'
  on-secondary-container: '#cce8e5'
  tertiary: '#b0c9e8'
  on-tertiary: '#19324b'
  tertiary-container: '#314963'
  on-tertiary-container: '#d1e4ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
typography:
  font-family: Montserrat, sans-serif
  display-large:
    size: 120px
    weight: 900
    line-height: 1.0
    letter-spacing: -0.04em
    text-transform: uppercase
  headline-large:
    size: 64px
    weight: 800
    line-height: 1.1
  label-mono:
    font-family: JetBrains Mono, monospace
    size: 14px
    weight: 500
    letter-spacing: 0.05em
spacing:
  section-gap: 160px
  container-padding: 80px
  component-gap: 32px
components:
  top-nav-bar:
    style: glassmorphism
    blur: 12px
    bg-opacity: 0.9
    border-bottom: 1px solid rgba(255, 255, 255, 0.1)
  primary-button:
    bg: '#e8282b'
    text: '#ffffff'
    radius: 0px
    hover: scale-95
  service-card:
    border: 1px solid #2b2a2a
    numbering-color: '#e8282b'
    numbering-font: JetBrains Mono
---

# Kinetic Neo-Media: Design Protocol

## Visual Identity
The brand is defined by "High-Velocity Engineering." It uses a deep obsidian base to create a high-contrast environment where **Kinetic Red (#e8282b)** acts as the primary signal for action, results, and movement.

## Grid & Layout
- **Section Gaps:** Maintain a strict 160px vertical rhythm between major sections.
- **Max-Width:** Content is capped at 1440px with 80px side margins on desktop.
- **3-Column Architecture:** Standard grid for services, portfolio items, and case study cards.

### Multiple Pages & Routing
- `index.html` — The main landing page.
- `our-story.html` — The "Our Story" page featuring the founders, core team, and company values.

### The Team (Our Story)
- **Akbar Ali**: Highlighted as the core identity in the Our Story heading.
- **Aziz Heema**: Founder & CEO
- **Ali Raja**: Manager & Vibe Coder

### Core Values (Our Story)
- **// 04 Radical Ownership**: Responsibility without excuses. Client numbers miss, we own it. A deadline slips, we own it. No finger-pointing at platforms, vendors, or algorithms.
- **// 05 Transparent Partnership**: Honest communication on progress and ROI. If the campaign isn't working, you hear it from us before you notice it in the dashboard.
- **// 06 Relentless Improvement**: Compounding systems that improve monthly. Every retrospective ships at least one process upgrade into the next sprint.

## 6. Implementation Notes
- **Navigation:** Links utilize a Kinetic Red line-through decoration on hover.
- **CTAs:** Primary buttons are solid red; secondary buttons are ghosted with 1px white or red borders.
- **Glass Effects:** Overlays and dropdowns use a 90% obsidian fill with a 12px backdrop blur.

---
This updated document ensures that any agent or tool you u