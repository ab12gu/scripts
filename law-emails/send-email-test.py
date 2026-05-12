# filename: send-email-test.py
# author: Abhay Gupta
# date creatd: 26-05-11
#

def send_email(sender, recipient):

    import smtplib
    import json
    import os
    from email.message import EmailMessage

    print("Email sender: ", sender)
    print("Email recipient: ", recipient)

    key_name = 'EMAIL_APP_KEY'
    key_value = os.getenv(key_name)
    #print(key_name + ": " + key_value)

    msg = EmailMessage()
    msg.set_content(
        'Hi,\n\n'
        'I am reaching out to see if I can '
        'have a consultation on this case?\n'
        'I was just contacted by a personal '
        'injury lawyer a couple weeks back suddenly.\n'
        '(See attached) \n\n'
        'Sincerely,\n\n' 
        'Abhay Gupta'
    )

    msg['Subject'] = f'Request for consultation'
    #msg['From'] = sender
    #msg['To'] = recipient

    with open('./docs/JRothschild_AGupta_NKenny.pdf', 'rb') as pdf:
        pdf = pdf.read()
        msg.add_attachment(
            pdf, 
            maintype='application',
            subtype='pdf',
            filename='JRothschild_AGupta_NKenny.pdf'
        )

    with open('lawyer_emails.json', 'rb') as jsonfile:
        lawyers_emails = json.load(jsonfile)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        print(smtp)
        print(type(smtp))
        smtp.starttls()
        smtp.login(sender, key_value)
        #for i in range(2):
        for lawyer_email in lawyers_emails:
            #recipient = lawyer_email
            print(i)
            #smtp.sendmail(sender, recipient, 'Subject: This is automated\nweird...')
            smtp.send_message(msg, to_addrs=recipient)
    
    print('Email Sent!')

if __name__ == "__main__":
    
    sender = 'ab18gu@gmail.com'
    #recipient = 'madalinc.preda@gmail.com'
    recipient = sender

    send_email(sender, recipient)
