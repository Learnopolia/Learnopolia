// The email sending function
function emailSend() {
  var firstname = document.getElementById("firstname").value;
  var lastname = document.getElementById("lastname").value;
  var email = document.getElementById("email").value;
  var messageBody = document.getElementById("message").value;
  Email.send({
    Host : "smtp.elasticemail.com",
    Username : "learnopolia@gmail.com",
    Password : "7B6AFEABA25979315C0DCF36F9C4CA8B620F",
    To : 'dohoudanielfavour@gmail.com',
    From : "learnopolia@gmail.com",
    Subject : "This is the subject",
    Body : NamemessageBody
  }).then(
    message => alert(message)
  );
}

/*
function emailSend() {
  var firstname = document.getElementById('firstname').value;
  var lastname = document.getElementById('lastname').value;
  var email = document.getElementById('email').value;
  var messageBody = document.getElementById('message').value;

  Email.send({
    Host: 'smtp.elasticemail.com',
    Username: 'learnopolia@gmail.com',
    Password: '7B6AFEABA25979315C0DCF36F9C4CA8B620F',
    To: 'dohoudanielfavour@gmail.com',
    From: 'learnopolia@gmail.com',
    Subject: 'Contact Form Submission from ' + firstname + ' ' + lastname,
    Body: 'Name: ' + firstname + ' ' + lastname + '<br>Email: ' + email + '<br>Message: ' + messageBody
  }).then(
    message => {
      if (message === 'OK') {
        swal("Email sent successfully: ", "success");
      }
      else {
        swal("Mail sending failed: ", "error");
      }
    }
    // lert("Mail sent successfully: " + message),
    // error => alert("Mail sending failed: " + error)
  );
}

*/
