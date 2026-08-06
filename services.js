gsap.registerPlugin(ScrollTrigger, TextPlugin);

// Magnetic buttons and links
document.querySelectorAll('button, a[class*="rounded-full"]').forEach(btn => {
    btn.addEventListener('mousemove', e => {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        gsap.to(btn, { x: x * 0.25, y: y * 0.25, duration: 0.3, ease: 'power2.out' });
    });
    btn.addEventListener('mouseleave', () => {
        gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.5)' });
    });
});

// Spotlight effect and magnetic tilt on hover (identical to homepage style)
document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
        card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
    });
    card.addEventListener('mousemove', e => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        gsap.to(card, {
            rotateY: x * 6,
            rotateX: -y * 6,
            transformPerspective: 800,
            duration: 0.4,
            ease: 'power2.out'
        });
    });
    card.addEventListener('mouseleave', () => {
        gsap.to(card, { rotateY: 0, rotateX: 0, duration: 0.6, ease: 'power2.out' });
    });
});

// GSAP Scroll Trigger for Cards
gsap.from('.service-card', {
    scrollTrigger: {
        trigger: '#services',
        start: 'top 80%',
        once: true
    },
    opacity: 0,
    y: 50,
    duration: 0.8,
    stagger: 0.1,
    ease: 'power3.out'
});

// Scroll trigger class scrolled on navbar
ScrollTrigger.create({
    start: 'top -80',
    end: 99999,
    toggleClass: { className: 'scrolled', targets: 'nav' }
});

// Pre-footer glitch banner effect
const bannerEl = document.getElementById('banner-glitch');
if (bannerEl) {
    bannerEl.style.opacity = '1';
    ScrollTrigger.create({
        trigger: bannerEl,
        start: 'top 85%',
        once: true,
        onEnter: () => {
            bannerEl.classList.add('glitching');
            setTimeout(() => bannerEl.classList.remove('glitching'), 1200);
        }
    });
}
