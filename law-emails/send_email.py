# filename: send-email-test.py
# author: Abhay Gupta
# date created: 26-05-11
#

def send_email(sender, recipient):

    import smtplib
    import json
    import os
    from email.message import EmailMessage
    #import time

    print("Email sender: ", sender)
    print("Email recipient: ", recipient)

    key_name = 'EMAIL_APP_KEY'
    key_value = os.getenv(key_name)
    #print(key_name + ": " + key_value)

    with open('lawyers_emails.json', 'rb') as jsonfile:
        lawyers_emails = json.load(jsonfile)

    with open('lawyers_names.json', 'rb') as jsonfile:
        lawyers_names = json.load(jsonfile)
    
    total = len(lawyers_emails)
    
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        print(smtp)
        print(type(smtp))
        smtp.starttls()
        smtp.login(sender, key_value)

        #for i in range(2):
        for i in range(400):
            recipient = lawyers_emails.pop(0)
            lawyer_name = lawyers_names.pop(0)

            #time.sleep(10)
            #smtp.sendmail(sender, recipient, 'Subject: This is automated\nweird...')
            print(i, " of ", total, lawyer_name, ", Email: ", recipient)

            msg = EmailMessage()
            msg.set_content(
                'Hi ' + lawyer_name + ',' + '\n\n'
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
            smtp.send_message(msg, to_addrs=recipient)
    
    with open('lawyers_emails.json', 'w') as jsonfile:
        json.dump(lawyers_emails, jsonfile)

    with open('lawyers_names.json', 'w') as jsonfile:
        json.dump(lawyers_names, jsonfile)
 
    print('Email Sent!')

if __name__ == "__main__":
    
    sender = 'ab18gu@gmail.com'
    #recipient = 'madalinc.preda@gmail.com'
    recipient = sender

    send_email(sender, recipient)
