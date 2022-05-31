
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



## ./venv/Scripts/activate.ps1   

## activar para ver errores en el navegador
driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')

print('Mail: juanmechulan@gmail.com y la contraseña: n3AfJty@@Xed!*Q')

def acc():

    element_present = EC.presence_of_element_located((By.ID, 'ddls_0'))
    WebDriverWait(driver, 5).until(element_present)

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

    ## DatiAddizionaliPrenotante_5___testo altura
    conyuge = driver.find_element(By.ID,'DatiAddizionaliPrenotante_5___testo')
    conyuge.send_keys('178')

    ## ddls_6 color de ojos
    select = Select(driver.find_element(By.ID,'ddls_6'))
    select.select_by_value('23')

    ## DatiAddizionaliPrenotante_7___testo 
    conyuge = driver.find_element(By.ID,'DatiAddizionaliPrenotante_7___testo')
    conyuge.send_keys('-')

    ## docAddizionale_0
    dni = driver.find_element(By.ID,'File_0')
    dni.send_keys('D:\Documentos\Bot ciudadania\Dnis\mechulan.pdf')

    dni = driver.find_element(By.ID,'File_1')
    dni.send_keys('D:\Documentos\Bot ciudadania\Dnis\mechulan.pdf')

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
    mailBox.send_keys("juanmechulan@gmail.com")


    passBox = driver.find_element(By.ID,"login-password")
    passBox.send_keys("n3AfJty@@Xed!*Q")

    time.sleep(4)
    passBox.send_keys(Keys.RETURN)



driver.get('https://prenotami.esteri.it/Home?ReturnUrl=%2fServices')


## login
login()


## chequeo si entre a la pagina de prenota

if input('si entro apreta 3: ') == '3':

    # redirecciono a la pagina del formulario
    driver.get('https://prenotami.esteri.it/Services/Booking/1021')

    while True:

        entrada = input('Rellenar 1, Cancelar 2, Reintentar a: ')

        if entrada == '1':
            acc()

        elif entrada == '2':
            driver.quit()
            break

        elif entrada == 'a':    
            driver.get('https://prenotami.esteri.it/Services/Booking/1021')