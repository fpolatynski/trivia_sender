import include
import contains
import adresses

if __name__ == '__main__':
    send_to =['Send_to_1', 'Send_to_2']
    for reciver in send_to:
        include.send_trivia(adresses.gmail, adresses.adresses[reciver], adresses.password, contains.email_trivia_contents[1])
    