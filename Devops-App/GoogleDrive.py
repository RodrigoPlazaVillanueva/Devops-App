
import csv
import logging
import psycopg2
from datetime import date
from datetime import datetime

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from datetime import date
from datetime import datetime

#Exportar tablas


conn = psycopg2.connect(
    host="localhost",
    database="rest-market",
    user="Rodrigo",
    password="password",
    port= "5432")

def consulta_tablas():
    cur1=conn.cursor()
    cur2=conn.cursor()
    cur3=conn.cursor()
    cur4=conn.cursor()

    cur1.execute('SELECT * FROM "Customers"')
    cur2.execute('SELECT * FROM "Employees"')
    cur3.execute('SELECT * FROM "Foods"')
    cur4.execute('SELECT * FROM "Products"')
    
    datosCustomer = cur1.fetchall()
    datosEmployees = cur2.fetchall()
    datosFoods = cur3.fetchall()
    datosProducts = cur4.fetchall()

    cur1.close()
    cur2.close()
    cur3.close()
    cur4.close()

    conn.close()
    return datosCustomer ,datosEmployees,datosFoods, datosProducts

Tablas = consulta_tablas()
with open('Tablas.csv','w', newline='') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerows(Tablas)

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

crear_archivo_texto('tablas_'+Fecha +'.csv',Tablas.__str__(),'1vfyZ75fwotCgiNWWE5rifmGLTZjqaRdJ')




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
