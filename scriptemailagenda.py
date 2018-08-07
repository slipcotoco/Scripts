import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
email = 'pythontestemeli@gmail.com'
password = 'Meli1234'
send_to_email ='leonardo.dylan@mercadolivre.com'
#agenda = 
subject = 'Teste'
message = 'Testando topper'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)
text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()

print("E-mail enviado com sucesso") 
