document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('subscribe-form');
    const thankYouMessage = document.getElementById('thank-you-message');
    const progressBar = document.getElementById('progress');
    const progressText = document.querySelector('.progress-text');

    // Animate progress bar on page load
    setTimeout(() => {
        progressBar.style.width = '50%';
    }, 500);

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const fullName = formData.get('fullName');
        const email = formData.get('email');

        // Simulate form submission to a Flask backend
        try {
            const response = await fetch('/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ fullName, email }),
            });

            if (response.ok) {
                form.reset();
                thankYouMessage.classList.remove('hidden');
                thankYouMessage.style.opacity = '1';
                setTimeout(() => {
                    thankYouMessage.style.opacity = '0';
                    setTimeout(() => {
                        thankYouMessage.classList.add('hidden');
                    }, 500);
                }, 3000);
            } else {
                throw new Error('Form submission failed');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred. Please try again later.');
        }
    });

    // Add subtle animation to the progress bar
    let progress = 50;
    setInterval(() => {
        progress += (Math.random() * 2 - 1);
        progress = Math.max(0, Math.min(100, progress));
        progressBar.style.width = `${progress}%`;
        progressText.textContent = `${Math.round(progress)}% Complete`;
    }, 2000);

    // Add parallax effect to background
    document.addEventListener('mousemove', (e) => {
        const moveX = (e.clientX - window.innerWidth / 2) * 0.01;
        const moveY = (e.clientY - window.innerHeight / 2) * 0.01;
        document.querySelector('.background-image').style.transform = `translate(${moveX}px, ${moveY}px)`;
    });
});
