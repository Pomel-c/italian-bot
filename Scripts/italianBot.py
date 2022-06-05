from lib2to3.pgen2 import driver
from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from datetime import datetime, date
from selenium.webdriver.firefox.options import Options


from sendo import sendoMail
from var_sv import rde, wrt

## ./venv/Scripts/activate.ps1   

## Iniciar firefox minimizado
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'C:\Program Files (x86)\geckodriver.exe', service_log_path="D:\Documentos\Bot ciudadania\geckodriver.log")

## activar para ver errores en el navegador
#driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')


def rellenoDatos():
    
    ## ddls_0 posee pasaporte?  Drop downs
    select = Select(driver.find_element(By.ID,'ddls_0'))
    select.select_by_visible_text('No')
    ## ddls_1 Hijos menores     Drop downs
    select = Select(driver.find_element(By.ID,'ddls_1'))
    select.select_by_value('12')
    ## DatiAddizionaliPrenotante_2___testo cantidad de hijos menores        llenar textos
    hijoMenor = driver.find_element(By.ID,'DatiAddizionaliPrenotante_2___testo')
    hijoMenor.send_keys('0')
    
    ## DatiAddizionaliPrenotante_3___testo direccion completa de residencia llenar textos    
    direccion = driver.find_element(By.ID,'DatiAddizionaliPrenotante_3___testo')
    direccion.send_keys('MZA 64 CASA 30 B° DALVIAN - MENDOZA CAPITAL - MENDOZA')
    
    ## ddls_4 estado civil  Drop downs
    select = Select(driver.find_element(By.ID,'ddls_4'))
    select.select_by_value('16')
    ## DatiAddizionaliPrenotante_5___testo nombre de conyuge    llenar textos
    conyuge = driver.find_element(By.ID,'DatiAddizionaliPrenotante_5___testo')
    conyuge.send_keys('-')
    
    ## File_2 subir primer archivo 
    dni = driver.find_element(By.ID,'File_2')
    dni.send_keys('D:\Documentos\Bot ciudadania\Dnis\mechulan.pdf')
    ## File_3 subir segundo archivo
    dni2 = driver.find_element(By.ID,'File_3')
    dni2.send_keys('D:\Documentos\Bot ciudadania\Dnis\mechulan.pdf')
    ## PrivacyCheck hacer click al boton
    check = driver.find_element(By.ID,'PrivacyCheck')
    check.click()
    
    ## btnAvanti hacer click al avance
    avant = driver.find_element(By.ID,'btnAvanti')
    avant.click()
    
    ##time.sleep(2)
    ## aceptar pop up alert
    obj = driver.switch_to.alert
    obj.accept()
        
def login():
    mailBox = driver.find_element(By.ID,"login-email")
    mailBox.send_keys("turnos.prenota.mendoza@gmail.com")
    
    

    passBox = driver.find_element(By.ID,"login-password")
    passBox.send_keys("turnoMendoza1")
    
    time.sleep(5)
    passBox.send_keys(Keys.RETURN)

    time.sleep(5)

    if driver.title == 'Home Page - Prenot@Mi':
        passBox.send_keys(Keys.RETURN)

def dataHoy():
    ## hora
    now = datetime.now()
    hour = now.strftime("%H:%M")
    
    ## Dia
    today = date.today()
    dia = today.strftime("%d %B")

    return dia, hour

def chequeo(i, hour, dia, url):

    # chequeo si se abrio el index
    if url == 'https://prenotami.esteri.it/Services':
        #driver.get_screenshot_as_file(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png')
        msg = f'No Hay turnos, intento {i} Hora: {hour} del {dia}'
      
    ## chequeo si se abrio el calendario
    elif url == 'https://prenotami.esteri.it/Services/Booking/552':
        driver.get_screenshot_as_file(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png')
        msg = f'Hay turnos, intento {i} Hora: {hour} del {dia}'
        sendoMail(i,hour)

    ## si tira error por cualquier otra cosa
    else:
        driver.get_screenshot_as_file(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png')
        msg = f'Error {i} Hora: {hour} del {dia}'

    return msg


def main():  
    
    driver.get('https://prenotami.esteri.it/Home?ReturnUrl=%2fServices')
    i = rde()

    dia, hour = dataHoy()


    msg = f'Problema de conexion {i} Hora: {hour} del {dia}'

    ## login
    login()
    time.sleep(5)
    
    ## chequeo si entre a la pagina de prenota
    if driver.title == 'Sede - Prenot@Mi':

        # redirecciono a la pagina del formulario
        driver.get('https://prenotami.esteri.it/Services')
        
        time.sleep(5)
        prenota = driver.find_element(By.XPATH,'/html/body/main/div[3]/div/table/tbody/tr[3]/td[4]/a/button')
        prenota.send_keys(Keys.RETURN)
        time.sleep(5)

        url = driver.current_url
        msg = chequeo(i, hour, dia, url)

        
    else:
        driver.get_screenshot_as_file(f'D:\Documentos\Bot ciudadania\screenshots\screen_{i}.png')
        
    
    i = i + 1
    wrt(i, msg)

    driver.quit()


main()
