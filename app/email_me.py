import os
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
MY_EMAIL_ADDRESS = os.environ.get('MY_EMAIL_ADDRESS')



# CONFIGURE SENDGRID SERVICE

sg = sendgrid.SendGridAPIClient(apikey = SENDGRID_API_KEY)

# COMPILE EMAIL RESOURCE

my_email = Email(MY_EMAIL_ADDRESS)

subject = "A record has been added or changed"
from_email = my_email
to_email = my_email
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)

print("SUBJECT:", subject)
print("MESSAGE:", content)

# ISSUE A REQUEST FOR THE SENDGRID SERVICE TO SEND THE EMAIL

response = sg.client.mail.send.post(request_body=mail.get())

# PARSE RESPONSE

print(response.status_code)
print(response.body)
print(response.headers)
