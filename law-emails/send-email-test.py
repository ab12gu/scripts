# filename: send-email-test.py
# author: Abhay Gupta
# date creatd: 26-05-11
#

def send_email(sender, recipient):

    import smtplib
    import os
    from email.message import EmailMessage

    print("Email sender: ", sender)
    print("Email recipient: ", recipient)

    key_name = 'EMAIL_APP_KEY'
    key_value = os.getenv(key_name)
    #print(key_name + ": " + key_value)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        print(smtp)
        print(type(smtp))
        smtp.starttls()
        smtp.login(sender, key_value)
        smtp.sendmail(sender, recipient, 'Subject: This is automated\nweird...')
    
    print('Email Sent!')

if __name__ == "__main__":
    
    sender = 'ab18gu@gmail.com'
    recipient = 'madalinc.preda@gmail.com'
    recipient = sender

    send_email(sender, recipient)
