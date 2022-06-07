from re import A
import smtplib
import imghdr
from email.message import EmailMessage
import csv
from time import sleep
import time 
from googleapiclient.discovery import build
from google.oauth2 import service_account



def mailList():

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = 'keys.json'
    
    
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    
    
    # If modifying these scopes, delete the file token.json.
    
    
    # The ID and range of a sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '1vp7ZF68D-f6fCYb3hlK9qmqKTbr7rn5o39Xz2vcwOaM'
    
    
    
    # If there are no (valid) credentials available, let the user log in.
    
        # Save the credentials for the next run
    
    service = build('sheets', 'v4', credentials=creds)
    
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="respuesta!A1:C300").execute()
                                
    values = result.get('values', [])
    
    mails = []
    
    for i in values[2:]:
        mails.append(i[2])
    
    mails = list(dict.fromkeys(mails))

    return mails




def sendoMail(numero, hour):
    
    Reciever_Email1 = mailList()
    i = numero
    Sender_Email = "turnos.prenota.mendoza@gmail.com"
    Reciever_Email = ["gasparmjose@gmail.com", "carmenjose9.m@gmail.com", "carmelilita.jose@gmail.com", "julietasardella@outlook.com", "juanmechulan@gmail.com"]
    Password = 'phrqkmukyijrofnw'
    
    hour = hour
    newMessage = EmailMessage()                         
    newMessage['Subject'] = f"Hay Turno de consulado para Pasaporte Hora: {hour}" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content('Entra ya: https://prenotami.esteri.it/Services/Booking/552') 
    
    ## with open(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png', 'rb') as f:
    ##     image_data = f.read()
    ##     image_type = imghdr.what(f.name)
    ##     image_name = f.name
    ## 
    ## newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
    
    


    time.sleep(100)
    i = numero
    Sender_Email = "turnos.prenota.mendoza@gmail.com"
    
    Password = 'phrqkmukyijrofnw'
    
    hour = hour
    newMessage = EmailMessage()                         
    newMessage['Subject'] = f"Hay Turno de consulado para Pasaporte Hora: {hour}" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email1                   
    newMessage.set_content('Entra ya: https://prenotami.esteri.it/Services/Booking/552') 

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)

