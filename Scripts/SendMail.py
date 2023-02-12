from re import A
import smtplib
import imghdr
from email.message import EmailMessage
from googleapiclient.discovery import build
from google.oauth2 import service_account
from ReadWriteInfo import read
import random
import math
import numpy as np


def mailList():

    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    SERVICE_ACCOUNT_FILE = '.\Scripts\keys.json'
    
    
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
                                range="respuesta!A1:C1000").execute()
                                
    values = result.get('values', [])
    
    mails = []
    
    for i in values[2:]:
        mails.append(i[2])
    
    mails = list(dict.fromkeys(mails))
    return mails


def send_Mail(i, hour):
    
    Sender_Email = read(3) 
    Password = read(4) 

    Reciever_Email = mailList()
    for mail in Reciever_Email:
        mails.append(mail)

    mails = list(dict.fromkeys(mails)) 
    random.shuffle(mails)

    # Divido la lista de mails en partes de menos de 100
    n = math.ceil(len(mails)/100)
    mail_arrays = np.array_split(mails, n)
    
    for j in range(n):
        hour = hour
        newMessage = EmailMessage()                         
        newMessage['Subject'] = f"Hay Turno de consulado para Pasaporte Hora: {hour}" 
        newMessage['From'] = Sender_Email                   
        newMessage['BCC'] = mail_arrays[j]                  
        newMessage.set_content(f'''

Entra ya: https://prenotami.esteri.it/Services/Booking/552
    
Se encontro un turno en el intento {i}.
    

''') 
    
        # with open(f'.\screenshots\screen_{i}.png', 'rb') as f:
        #     image_data = f.read()
        #     image_type = imghdr.what(f.name)
        #     image_name = f.name
    
        # newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)              
            smtp.send_message(newMessage)

    
    
