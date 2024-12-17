document.addEventListener('DOMContentLoaded', function() {
    // Set the date we're counting down to (3 months from now)
    const countDownDate = new Date();
    countDownDate.setMonth(countDownDate.getMonth() + 3);

    // Update the countdown every 1 second
    const countdownTimer = setInterval(function() {
        const now = new Date().getTime();
        const distance = countDownDate - now;

        // Calculate days, hours, minutes and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result
        document.getElementById("days").textContent = days.toString().padStart(2, '0');
        document.getElementById("hours").textContent = hours.toString().padStart(2, '0');
        document.getElementById("minutes").textContent = minutes.toString().padStart(2, '0');
        document.getElementById("seconds").textContent = seconds.toString().padStart(2, '0');

        // If the countdown is finished, display a message
        if (distance < 0) {
            clearInterval(countdownTimer);
            document.querySelector('.countdown').innerHTML = "We're launching soon!";
        }
    }, 1000);

    // Handle form submission
    const form = document.getElementById('subscribe-form');
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('email').value;
        // Here you would typically send the email to your server
        // For this example, we'll just log it to the console
        console.log('Subscribed email:', email);
        alert('Thank you for subscribing! We\'ll notify you when we\'re back online.');
        form.reset();
    });

    // Animate construction icons
    const icons = document.querySelectorAll('.construction-animation i');
    setInterval(() => {
        icons.forEach(icon => {
            icon.style.transform = `translateY(${Math.random() * 10}px)`;
        });
    }, 2000);
});
