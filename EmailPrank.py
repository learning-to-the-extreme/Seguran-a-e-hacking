import smtplib

# Server and login details
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("youremail@gmail.com", "yourpassword")

# Recipient's email address
to_address = 'recipient@example.com'

# Email subject and message
subject = 'This is an automated email'
message = 'Hello, this is an automated email sent as a prank'

# Send the email
server.sendmail("youremail@gmail.com", to_address, f"Subject: {subject}\n\n{message}")

# Close the server
server.quit()
