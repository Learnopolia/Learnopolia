document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('subscribe-form');
    const formMessage = document.getElementById('form-message');

    // Handle form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const fullName = formData.get('fullName');
        const email = formData.get('email');

        try {
            // Simulate form submission delay
            await new Promise(resolve => setTimeout(resolve, 1000));

            // Clear the form
            form.reset();

            // Show success message with animation
            formMessage.textContent = 'Thank you for subscribing!';
            formMessage.style.animation = 'slideUp 0.3s ease-out';
            formMessage.classList.remove('hidden');

            // Hide the message after 5 seconds
            setTimeout(() => {
                formMessage.style.animation = 'slideDown 0.3s ease-out';
                setTimeout(() => {
                    formMessage.classList.add('hidden');
                }, 300);
            }, 5000);
        } catch (error) {
            console.error('Error submitting form:', error);
            formMessage.textContent = 'An error occurred. Please try again.';
            formMessage.style.backgroundColor = '#FFEBEE';
            formMessage.style.color = '#C62828';
            formMessage.classList.remove('hidden');
        }
    });

    // Animate progress bar
    const progress = document.querySelector('.progress');
    let width = 0;
    const interval = setInterval(() => {
        if (width >= 50) {
            clearInterval(interval);
        } else {
            width++;
            progress.style.width = width + '%';
        }
    }, 40);

    // Add smooth scroll behavior
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});
