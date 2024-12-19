document.addEventListener('DOMContentLoaded', () => {
    const errorCode = document.querySelector('.error-code');
    let shakeInterval;

    errorCode.addEventListener('mouseenter', () => {
        errorCode.classList.add('interactive-404');
        clearInterval(shakeInterval);
    });

    errorCode.addEventListener('mouseleave', () => {
        errorCode.classList.remove('interactive-404');
        startShaking();
    });

    errorCode.addEventListener('click', () => {
        errorCode.style.animation = 'none';
        errorCode.offsetHeight; // Trigger reflow
        errorCode.style.animation = null;

        const colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1'];
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        errorCode.style.color = randomColor;
    });

    function startShaking() {
        shakeInterval = setInterval(() => {
            errorCode.style.animation = 'none';
            errorCode.offsetHeight; // Trigger reflow
            errorCode.style.animation = null;
        }, 4100); // Restart animation every 4.1 seconds (animation duration + small delay)
    }

    startShaking();
});

// console.log('404 page script loaded successfully.');
