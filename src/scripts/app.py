from flask import Flask, request, render_template
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Set up the email server and send the email
        try:
            smtp_server = 'smtp.example.com'  # Replace with your SMTP server
            smtp_port = 587  # Replace with your SMTP port
            smtp_username = 'your-username'  # Replace with your SMTP username
            smtp_password = 'your-password'  # Replace with your SMTP password

            sender_email = 'your-email@example.com'
            recipient_email = 'your-email@example.com'  # Your email address

            subject = f'Contact Form Submission from {name}'

            email_text = f"Name: {name}\n"
            email_text += f"Email: {email}\n\n"
            email_text += f"Subject: {subject}\n\n"
            email_text += f"Message:\n{message}"

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_email, email_text)
            server.quit()

            return 'Thank you for your message. We will get back to you soon!'
        except Exception as e:
            return f'Oops! Something went wrong: {str(e)}'

    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)
