# filename: send-email-test.py
# author: Abhay Gupta
# date creatd: 26-05-11
#

def send_email(sender, recipient):

    import smtplib

    #print(EMAIL_APP_KEY)

    print("Email sender: ", sender)
    print("Email recipient: ", recipient)
    print('Email Sent!')



if __name__ == "__main__":
    
    sender = 'ab18gu@gmail.com'
    recipient = 'madalinc.preda@gmail.com'
    recipient = sender

    send_email(sender, recipient)
