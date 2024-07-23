import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()

    username = "luciusfremon@gmail.com"
    password = "thqdidpzbkxacvgb"

    receiver = "ckcraig2006@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=None) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)