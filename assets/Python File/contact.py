import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cgi

# Read JSON data from the form submission
form = cgi.FieldStorage()
data = form.getvalue('data')
data = json.loads(data)

# Email details
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "your-email@example.com"
smtp_password = "your-email-password"
recipient_email = "recipient@example.com"

name = data['name']
email = data['email']
message = data['message']

subject = "New Contact Form Submission"
body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = recipient_email
msg['Subject'] = subject

msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, recipient_email, msg.as_string())
    server.close()
    print("Email sent successfully.")
except Exception as e:
    print(f"Failed to send email: {e}")
