from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from os import walk
import pytesseract
from datetime import datetime, date
from selenium.webdriver.firefox.options import Options


from sendo import sendoMail
from var_sv import rde, wrt
from mod_bot import tele

# ./venv/Scripts/activate.ps1   

# Iniciar firefox minimizado
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\Program Files (x86)\geckodriver.exe', service_log_path="D:\Documentos\Bot ciudadania\geckodriver.log")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def login(): 

    # Obtengo mail y contrasela
    mailR = rde(0)
    passW = rde(1)
    
    # Logeo
    mailBox = driver.find_element(By.ID,"login-email")    
    mailBox.send_keys(mailR)
    
    

    passBox = driver.find_element(By.ID,"login-password")
    passBox.send_keys(passW)
    
    time.sleep(5)
    passBox.send_keys(Keys.RETURN)

    time.sleep(20)

def dataHoy():
    ## hora
    now = datetime.now()
    hour = now.strftime("%H:%M")
    
    ## Dia
    today = date.today()
    dia = today.strftime("%d %B")

    return dia, hour

def verf(i, hour, dia, intento):
    verf1 = False
    verf2 = False

    # Chequeo si estan las palabras en el html
    check = 0
    html = driver.page_source
    frases = ['Informazioni sulla prenotazione', 'Tipo Prenotazion', 'Prenotazione Signola', 'Dati Richiedente', 'In possesso di passaporto italiano scaduto/in scadenza', 'Figli minorenni', 'Numero figli minorenni', 'Stai prenotando per 1 Appuntamento']
    for frase in frases:
        if frase in html:
            check += 1
        
        if check == 4:
            verf1 = True
            break


    # Chequeo de seguridad, palabras escritas de la imagen
    
    text = pytesseract.image_to_string(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png')
    frases = ['Dati Richiedente', 'Figii minorenni', 'Numero figii minorenni', 'Servizio di rilascio passaporti', 'prenotando per 1 Appuntamento', 'Figli minorenni', 'Informazioni sulla prenotazione', 'Numero figli minorenni', 'Prenotazione Singola']

    check = 0
    
    for frase in frases:    
        if frase in text:
            print(frase)
            check += 1
        
        if check == 3:
            verf2 = True
            break

    if verf1 and verf2:
        msg = f'Hay turnos,  intento {i} Hora: {hour} del {dia}. Recursion: {intento}'
        tele(i, hour)
        #time.sleep(60)
        sendoMail(i, hour)
        return msg

    else:
        msg = f'No Hay turnos, intento {i} Hora: {hour} del {dia}. Recursion: {intento}'
        return msg

    

def main():  

    # Obtengo datos iniciales y mensaje default
    intento = 0
    bandera = 0
    dia, hour = dataHoy()
    i = int(rde("intento"))
    msg = f'Problema de conexion {i} Hora: {hour} del {dia}'


    # Entro a la pagina de Prenota
    driver.get('https://prenotami.esteri.it/Home?ReturnUrl=%2fUserArea')

    # Chequeo si tiro error
    if driver.title == 'Runtime Error':
                while driver.title != 'Home Page - Prenot@Mi':
                    driver.get('https://prenotami.esteri.it/Home?ReturnUrl=%2fUserArea')

    # Loop de logeo y chequeo 
    # Intento Logear
    while driver.title == 'Home Page - Prenot@Mi' or driver.title == 'Sede - Prenot@Mi':
        time.sleep(5)
    
        if driver.title == 'Home Page - Prenot@Mi':
            login()

        if driver.title == 'Sede - Prenot@Mi': 
            if len(driver.find_elements(By.ID,'advanced')) != 0:
                # redirecciono a la pagina del formulario
                prenota = driver.find_element(By.ID,'advanced')
                prenota.send_keys(Keys.RETURN)
                time.sleep(15)

            elif len(driver.find_elements(By.ID,'advanced')) == 0:
                # Chequeo si esta presente el boton de prenota, si no esta, recargo la pagina
                driver.get('https://prenotami.esteri.it/UserArea')

        while driver.title == 'Index - Prenot@Mi':

            # una vez que entro en el index, veo si aparece el boton de prenota. Si no recargo la pagina
            if len(driver.find_elements(By.XPATH, '/html/body/main/div[3]/div/table/tbody/tr[3]/td[4]/a/button')) == 0:
                driver.get('https://prenotami.esteri.it/Services')
                time.sleep(5)


            if len(driver.find_elements(By.XPATH, '/html/body/main/div[3]/div/table/tbody/tr[3]/td[4]/a/button')) != 0:
                prenota = driver.find_element(By.XPATH,'/html/body/main/div[3]/div/table/tbody/tr[3]/td[4]/a/button')
                prenota.send_keys(Keys.RETURN)
                time.sleep(40)

                # Chequeo si al apretar el boton de prenota entro al formulario o si me tira error de que no hay turnos
                if driver.current_url == 'https://prenotami.esteri.it/Services' or driver.current_url == 'https://prenotami.esteri.it/Services/Booking/552':
                    url = driver.current_url
                    suma = 0
                    i = int(rde("intento"))

                    prenota_error = 'Al momento non ci sono date disponibili per il servizio richiesto'
                    
                    # Chequeo si me tira el cartel de que no hay turno disponibles
                    while driver.current_url == 'https://prenotami.esteri.it/Services':

                        driver.get_screenshot_as_file(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png')
                        texto = pytesseract.image_to_string(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png')
                        html = driver.page_source

                        if prenota_error in texto or prenota_error in html:
                            break

                        else:
                            if len(driver.find_elements(By.XPATH, '/html/body/main/div[3]/div/table/tbody/tr[3]/td[4]/a/button')) != 0:
                                prenota = driver.find_element(By.XPATH,'/html/body/main/div[3]/div/table/tbody/tr[3]/td[4]/a/button')
                                prenota.send_keys(Keys.RETURN)
                                time.sleep(20)
                            suma += 1

                            if suma == 7:
                                break
                
                    if url == 'https://prenotami.esteri.it/Services/Booking/552':
                        driver.get_screenshot_as_file(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png')
                        #msg = f'Hay turnos,  intento {i} Hora: {hour} del {dia} en el intento: {intento}'
                        #sendoMail(i,hour)
                    
                    break

        while driver.title == 'Si è verificato un errore durante l’elaborazione della richiesta - Prenot@Mi':
            driver.get('https://prenotami.esteri.it/Home?ReturnUrl=%2fUserArea')

        # 10 intentos de logear y chequear turnos, si no tiro mensaje de error
        intento += 1
        if intento == 10:
            bandera = 1
            driver.get_screenshot_as_file(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png')
            break
    
    # Escribo en el Log

    msg = verf(i, hour, dia, intento)

    if bandera == 1:
        msg = f'Error de conexion, intento {i} Hora: {hour} del {dia}. Recursion: {intento}'

    i = i + 1
    wrt(i, msg)

    driver.quit()

main()


# Borro screens de mas de un dia 672 = 1 dia
#mypath = "D:\Documentos\Bot ciudadania\screenshots"
#items = next(walk(mypath), (None, None, []))[2]
#if len(items) >= 750:    
#    for item in items:
#        os.remove(f"D:\Documentos\Bot ciudadania\sceenshots\{item}")
