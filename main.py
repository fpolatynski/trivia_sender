import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import codecs

port = 465  # For SSL
password = "lugx tshs vzly hmvo"
sender_email = "enjoydailytrivia@gmail.com"
receiver_email = "nikstaskiewicz@gmail.com"


# Create a secure SSL context
context = ssl.create_default_context()

message = MIMEMultipart("alternative")
message["Subject"] = "TRIVIA EXPOSURE"
message["From"] = sender_email
message["To"] = receiver_email


# Create the plain-text and HTML version of your message
text = """\
Hi, How are you? Real Python has many great tutorials: www.realpython.com"""
html = codecs.open("eiffel.html", 'r')
print(html)
# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")


message.attach(part1)
message.attach(part2)


with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("enjoy.daily.trivia@gmail.com", "lugx tshs vzly hmvo")
    server.sendmail(sender_email, receiver_email, message.as_string())
    print('send')
