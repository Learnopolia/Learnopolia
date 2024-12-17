document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('cta-form');
    const formMessage = document.getElementById('form-message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
