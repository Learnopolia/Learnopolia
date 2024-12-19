// // document.addEventListener('DOMContentLoaded', () => {
// //     const form = document.getElementById('subscribe-form');
// //     const formMessage = document.getElementById('form-message');
// //     const submitButton = document.getElementById('submit-btn');

// //     form.addEventListener('submit', async (e) => {
// //         e.preventDefault();

// //         // Disable the submit button and show loading state
// //         submitButton.disabled = true;
// //         submitButton.innerHTML = 'Subscribing...';

// //         const formData = {
// //             fullName: document.getElementById('fullName').value,
// //             email: document.getElementById('email').value
// //         };

// //         try {
// //             const response = await fetch('/api/subscribe', {
// //                 method: 'POST',
// //                 headers: {
// //                     'Content-Type': 'application/json',
// //                 },
// //                 body: JSON.stringify(formData)
// //             });

// //             const data = await response.json();

// //             if (response.ok) {
// //                 // Hide the form with a fade out effect
// //                 form.style.opacity = '0';
// //                 form.style.transition = 'opacity 0.5s ease';

// //                 // Show success message with fade in effect
// //                 setTimeout(() => {
// //                     form.style.display = 'none';
// //                     formMessage.classList.remove('hidden');
// //                     formMessage.style.opacity = '0';
// //                     formMessage.style.display = 'block';

// //                     requestAnimationFrame(() => {
// //                         formMessage.style.opacity = '1';
// //                         formMessage.style.transition = 'opacity 0.5s ease';
// //                     });
// //                 }, 500);
// //             } else {
// //                 throw new Error(data.message || 'Something went wrong');
// //             }
// //         } catch (error) {
// //             // Show error message
// //             formMessage.textContent = 'An error occurred. Please try again.';
// //             formMessage.style.backgroundColor = '#FFEBEE';
// //             formMessage.style.color = '#C62828';
// //             formMessage.classList.remove('hidden');

// //             // Re-enable the submit button
// //             submitButton.disabled = false;
// //             submitButton.innerHTML = 'Subscribe to Stay Updated';
// //         }
// //     });
// // });


// document.addEventListener('DOMContentLoaded', () => {
//     const form = document.getElementById('subscribe-form');
//     const formMessage = document.getElementById('form-message');
//     const submitButton = document.getElementById('submit-btn');

//     if (form) {
//         form.addEventListener('submit', async (e) => {
//             e.preventDefault();

//             // Disable the submit button and show loading state
//             const submitButton = form.querySelector('button[type="submit"]');
//             submitButton.disabled = true;
//             submitButton.innerHTML = 'Subscribing...';

//             const formData = {
//                 fullName: document.getElementById('fullName').value.trim(),
//                 email: document.getElementById('email').value.trim()
//             };

//             try {
//                 const response = await fetch('/api/subscribe', {
//                     method: 'POST',
//                     headers: {
//                         'Content-Type': 'application/json',
//                     },
//                     body: JSON.stringify(formData)
//                 });

//                 const data = await response.json();

//                 if (response.ok) {
//                     // Hide the form with a fade out effect
//                     form.style.opacity = '0';
//                     form.style.transition = 'opacity 0.5s ease';

//                     // Show success message with fade in effect
//                     setTimeout(() => {
//                         form.style.display = 'none';
//                         formMessage.textContent = data.message;
//                         formMessage.classList.remove('hidden');
//                         formMessage.style.opacity = '0';
//                         formMessage.style.display = 'block';

//                         requestAnimationFrame(() => {
//                             formMessage.style.opacity = '1';
//                             formMessage.style.transition = 'opacity 0.5s ease';
//                         });
//                     }, 500);
//                 } else {
//                     // Show error message from server
//                     formMessage.textContent = data.message;
//                     formMessage.style.backgroundColor = '#FFEBEE';
//                     formMessage.style.color = '#C62828';
//                     formMessage.classList.remove('hidden');

//                     // Re-enable the submit button
//                     submitButton.disabled = false;
//                     submitButton.innerHTML = 'Subscribe to Stay Updated';
//                 }
//             } catch (error) {
//                 // Show generic error message
//                 formMessage.textContent = 'An error occurred. Please try again later.';
//                 formMessage.style.backgroundColor = '#FFEBEE';
//                 formMessage.style.color = '#C62828';
//                 formMessage.classList.remove('hidden');

//                 // Re-enable the submit button
//                 submitButton.disabled = false;
//                 submitButton.innerHTML = 'Subscribe to Stay Updated';
//             }
//         });
//     }

//     // Animate the progress bar
//     const progress = document.querySelector('.progress');
//     if (progress) {
//         let width = 0;
//         const interval = setInterval(() => {
//             if (width >= 50) {
//                 clearInterval(interval);
//             } else {
//                 width++;
//                 progress.style.width = width + '%';
//             }
//         }, 40);
//     }
// });

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('subscribe-form');
    const formMessage = document.getElementById('form-message');
    const submitButton = document.getElementById('submit-btn');

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            // Disable the submit button and show loading state
            const submitButton = form.querySelector('button[type="submit"]');
            submitButton.disabled = true;
            submitButton.innerHTML = 'Subscribing...';

            const formData = {
                fullName: document.getElementById('fullName').value.trim(),
                email: document.getElementById('email').value.trim()
            };

            try {
                const response = await fetch('/api/subscribe', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });

                const data = await response.json();

                if (response.ok) {
                    // Hide the form with a fade out effect
                    form.style.opacity = '0';
                    form.style.transition = 'opacity 0.5s ease';

                    // Show success message with fade in effect
                    setTimeout(() => {
                        form.style.display = 'none';
                        formMessage.textContent = data.message;
                        formMessage.classList.remove('hidden');
                        formMessage.style.opacity = '0';
                        formMessage.style.display = 'block';

                        requestAnimationFrame(() => {
                            formMessage.style.opacity = '1';
                            formMessage.style.transition = 'opacity 0.5s ease';
                        });
                    }, 500);
                } else {
                    // Show error message from server
                    formMessage.textContent = data.message;
                    formMessage.style.backgroundColor = '#FFEBEE';
                    formMessage.style.color = '#C62828';
                    formMessage.classList.remove('hidden');

                    // Re-enable the submit button
                    submitButton.disabled = false;
                    submitButton.innerHTML = 'Subscribe to Stay Updated';
                }
            } catch (error) {
                // Show generic error message
                formMessage.textContent = 'An error occurred. Please try again later.';
                formMessage.style.backgroundColor = '#FFEBEE';
                formMessage.style.color = '#C62828';
                formMessage.classList.remove('hidden');

                // Re-enable the submit button
                submitButton.disabled = false;
                submitButton.innerHTML = 'Subscribe to Stay Updated';
            }
        });
    }

    // Animate the progress bar
    const progress = document.querySelector('.progress');
    if (progress) {
        let width = 0;
        const interval = setInterval(() => {
            if (width >= 50) {
                clearInterval(interval);
            } else {
                width++;
                progress.style.width = width + '%';
            }
        }, 40);
    }
});
