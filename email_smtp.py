import smtplib
from email.mime.text import MIMEText

def send_email(sender, recipient, password, subject, body):
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, recipient, message.as_string())
            print(f"O email foi enviado!")
    except Exception as e:
        print(f"Ocorreu um erro no envio do email: {e}")

sender = "afranio.a164@gmail.com"
recipient_list = ["alfredobarros@bemol.com.br", "juanoliveira@bemol.com.br","emariellealmeida@bemol.com.br"]
password = "dqessemhwqqqnkov"
subject = "DESAFIO TALENT LAB ITACOATIARA"
body = "Olá, meu nome é Afrânio Esquerdo Viana e estou participando do processo seletivo do PROGRAMA DE ESTÁGIO TALENT LAB ITACOATIARA (Nível Superior)!"

for recipient in recipient_list:
    send_email(sender, recipient, password, subject, body)
