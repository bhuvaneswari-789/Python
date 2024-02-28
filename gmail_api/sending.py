import yagmail

# Initialize yagmail with your email credentials
yag = yagmail.SMTP('bhuvaneswarisiddamreddy@gmail.com', 'anandha@123')

# Send an email
yag.send(to='r190583@rguktrkv.ac.in', subject='Test Email', contents='Hello, this is a test email from yagmail!')

# Close the connection
yag.close()

