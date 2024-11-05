document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('#navbar');
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const loginBtn = document.querySelector('.login-btn');
    const hero = document.querySelector('#hero');

    // Change navbar background on scroll
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.backgroundColor = '#FFFFFF';
            navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        } else {
            navbar.style.backgroundColor = 'transparent';
            navbar.style.boxShadow = 'none';
        }
    });

    // Mobile menu toggle
    hamburger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        loginBtn.classList.toggle('active');
        hamburger.classList.toggle('active');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', (event) => {
        if (!navbar.contains(event.target) && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
            loginBtn.classList.remove('active');
            hamburger.classList.remove('active');
        }
    });

    // FAQ accordion
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('h3');
        question.addEventListener('click', () => {
            item.classList.toggle('active');
        });
    });

    // Initialize Swiper for testimonials with infinite scroll
    const swiper = new Swiper('.testimonial-slider', {
        slidesPerView: 1,
        spaceBetween: 30,
        loop: true,
        loopAdditionalSlides: 3,
        speed: 1000,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            640: {
                slidesPerView: 2,
            },
            1024: {
                slidesPerView: 3,
            },
        },
        on: {
            reachEnd: function () {
                // When reaching the end, loop back to the beginning smoothly
                this.slideTo(0, 0, false);
                this.autoplay.start();
            },
        },
    });

    // CTA button animation
    const ctaButton = document.querySelector('.cta-button');
    ctaButton.addEventListener('mouseover', () => {
        ctaButton.style.animation = 'pulse 1s infinite';
    });
    ctaButton.addEventListener('mouseout', () => {
        ctaButton.style.animation = 'none';
    });

    // Scroll Animations
    const animateOnScroll = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                observer.unobserve(entry.target);
            }
        });
    };

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver(animateOnScroll, observerOptions);

    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.animate-fade-in, .animate-slide-left, .animate-slide-right, .animate-slide-up, .animate-zoom-in');
    animatedElements.forEach(el => observer.observe(el));

    // Parallax effect for hero section
    window.addEventListener('scroll', () => {
        const scrollPosition = window.pageYOffset;
        hero.style.backgroundPositionY = `${scrollPosition * 0.7}px`;
    });
});

// Add styles for animations
const style = document.createElement('style');
style.textContent = `
    .animate-fade-in { opacity: 0; transition: opacity 1s; }
    .animate-slide-left { opacity: 0; transform: translateX(-50px); transition: opacity 1s, transform 1s; }
    .animate-slide-right { opacity: 0; transform: translateX(50px); transition: opacity 1s, transform 1s; }
    .animate-slide-up { opacity: 0; transform: translateY(50px); transition: opacity 1s, transform 1s; }
    .animate-zoom-in { opacity: 0; transform: scale(0.5); transition: opacity 1s, transform 1s; }
    .animate { opacity: 1; transform: translate(0, 0) scale(1); }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    #hero { background-attachment: fixed; }
`;
document.head.appendChild(style);

// Apply animation classes to elements
document.querySelector('#hero h1').classList.add('animate-fade-in');
document.querySelector('#hero p').classList.add('animate-fade-in');
document.querySelector('#hero .cta-button').classList.add('animate-fade-in');

document.querySelectorAll('#features .feature').forEach((el, index) => {
    el.classList.add(index % 2 === 0 ? 'animate-slide-left' : 'animate-slide-right');
});

document.querySelectorAll('#courses .course').forEach(el => {
    el.classList.add('animate-slide-up');
});

document.querySelectorAll('#courses .course img').forEach(el => {
    el.classList.add('animate-zoom-in');
});

document.querySelectorAll('#faq .faq-item').forEach(el => {
    el.classList.add('animate-fade-in');
});

document.querySelector('#cta').classList.add('animate-fade-in');

console.log('Scroll animations and parallax effect added successfully.');