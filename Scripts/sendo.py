import smtplib
import imghdr
from email.message import EmailMessage



def sendoMail(numero, hour):
    
    i = numero
    Sender_Email = "juansarde@gmail.com"
    Reciever_Email = ["gasparmjose@gmail.com", "carmenjose9.m@gmail.com", "carmelilita.jose@gmail.com", "julietasardella@outlook.com", "juanmechulan@gmail.com"] 
    Password = 'pxagdiwohcfdglah'
    
    hour = hour
    newMessage = EmailMessage()                         
    newMessage['Subject'] = f"Hay Turno de consulado para Pasaporte Hora: {hour}" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content('Entra ya: https://prenotami.esteri.it/Services/Booking/552') 
    
    with open(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)


