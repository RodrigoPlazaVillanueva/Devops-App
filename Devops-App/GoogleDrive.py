
import csv
import logging
from datetime import date
from datetime import datetime

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from datetime import date
from datetime import datetime

#Exportar tablas

customer = [
    ['Customer','Plaza','rodri@gmail.com'],
    ['Pamela','Caballero','pame@gmail.com'],
]

employe = [
    ['Employe','Plaza','rodri@gmail.com'],
    ['Carla','Caballero','pame@gmail.com'],
]

food = [
    ['Food','Plaza','rodri@gmail.com'],
    ['Carla','Caballero','pame@gmail.com'],
]

product = [
    ['Product','Plaza','rodri@gmail.com'],
    ['Carla','Caballero','pame@gmail.com'],
]


with open('Tablas.csv','w', newline='') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerows(customer)
    writer.writerows(employe)
    writer.writerows(food)
    writer.writerows(product)
   #Día actual
today = date.today()

#Fecha actual
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

hour = now.strftime("%H")
minute = now.strftime("%M")
second = now.strftime("%S")

Fecha = '{'+year+'}-{'+month+'}-{'+day+'}-{'+month+'}-{'+hour+'}-{'+minute+'}-{'+second+'}'

#INICIAR SESION
directorio_credencial = 'credentials_module.json'


def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credencial)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(directorio_credencial)
    else:
        gauth.Authorize()

    return GoogleDrive(gauth)

#Crear archivo
def crear_archivo_texto(nombre_archivo,contenido,id_folder):
    credenciales = login()
    archivo = credenciales.CreateFile({'title': nombre_archivo,\
                                       'parents': [{"kind": "drive#fileLink",\
                                                    "id": id_folder}]})
    archivo.SetContentString(contenido)
    archivo.Upload()

crear_archivo_texto('customer_'+Fecha +'.csv',customer.__str__(),'1vfyZ75fwotCgiNWWE5rifmGLTZjqaRdJ')
crear_archivo_texto('employee_'+Fecha +'.csv',employe.__str__(),'1vfyZ75fwotCgiNWWE5rifmGLTZjqaRdJ')
crear_archivo_texto('food_'+Fecha +'.csv',food.__str__(),'1vfyZ75fwotCgiNWWE5rifmGLTZjqaRdJ')
crear_archivo_texto('product_'+Fecha +'.csv',product.__str__(),'1vfyZ75fwotCgiNWWE5rifmGLTZjqaRdJ')



#Logs

logging.basicConfig(filename="logFile.txt",
                format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                   datefmt="%d-%m-%Y %H:%M:%S %p",
                   level=logging.DEBUG

                   )

logging.debug('Este mensaje es para DEBUG')
logging.info('Este mensaje es para INFO')
logging.warning('Este mensaje es para ADVERTENCIA')
logging.error('Este mensaje es un ERROR')