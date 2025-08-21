# import smtplib
# from email.message import EmailMessage
#
# email = EmailMessage()
# email['from'] = 'Akan'
# email['to'] = 'godfred.adusei@wayne.edu'
# email['subject'] = 'Low Power of the Laser beam'
#
# email.set_content('We have to measure the pump power to see if our power gives the reference output required')
#
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('phoenixdark466@gmail.com', 'pbahsvsjmutgbcol')
#     smtp.send_message(email)
#     print('Email sent')


import smtplib
from email.message import EmailMessage

# List of recipients with names and emails
recipients = [
    {'name': 'Godfred', 'email': 'godfred.adusei@wayne.edu'},
    {'name': 'Akan', 'email': 'udoikono@gmail.com'},
    {'name': 'David', 'email': 'udoikono@wayne.edu'},
]

# Your sender details
sender_name = 'Akan'
sender_email = 'phoenixdark466@gmail.com'
app_password = 'pbahsvsjmutgbcol'  # Your Gmail App Password

# Connect to Gmail's SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(sender_email, app_password)

    for person in recipients:
        email = EmailMessage()
        email['from'] = sender_name
        email['to'] = person['email']
        email['subject'] = 'Low Power of the Laser Beam'

        # Personalize the message using their name
        body = f"""
        Dear {person['name']},

        We have to measure the pump power to see if our power gives the reference output required {person['name']}.

        Best regards,  
        {sender_name}
        """
        email.set_content(body)

        smtp.send_message(email)
        print(f"Email sent to {person['name']} at {person['email']}")
