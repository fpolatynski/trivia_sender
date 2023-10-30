import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
#hasło cieszsieciekawostkami
#hasło "lugx tshs vzly hmvo"



# Sends HTML gmails
def send_trivia(sender_email, receiver_email, password, text, html, photo):
    port = 465


    context = ssl.create_default_context()
    message = MIMEMultipart("alternative")
    message["Subject"] = "TRIVIA EXPOSURE"
    message["From"] = sender_email
    message["To"] = receiver_email

    fp = open(photo, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print('send')