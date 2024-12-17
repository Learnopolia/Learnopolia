document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('subscribe-form');
    const formMessage = document.getElementById('form-message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);
        const fullName = formData.get('fullName');
        const email = formData.get('email');

        try {
            // Simulate form submission to a Flask backend
            await new Promise(resolve => setTimeout(resolve, 1000));

            // Clear the form
            form.reset();

            // Show the success message
            formMessage.textContent = 'Thank you for subscribing!';
            formMessage.classList.remove('hidden');

            // Hide the message after 5 seconds
            setTimeout(() => {
                formMessage.classList.add('hidden');
            }, 5000);
        } catch (error) {
            console.error('Error submitting form:', error);
            formMessage.textContent = 'An error occurred. Please try again.';
            formMessage.classList.remove('hidden');
        }
    });

    // Animate the progress bar
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
});
