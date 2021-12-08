
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

    cur1.execute('SELECT * FROM "Customers"')

    datosCustomer = cur1.fetchall()

    cur1.close()
    return datosCustomer

def consulta_tablas2():
    cur2=conn.cursor()

    cur2.execute('SELECT * FROM "Employees"')

    datosEmployees = cur2.fetchall()
    
    cur2.close()    
   
    return datosEmployees

def consulta_tablas3():
    cur3=conn.cursor()

    cur3.execute('SELECT * FROM "Foods"')

    datosFoods = cur3.fetchall()
    
    cur3.close()    
   
    return datosFoods

def consulta_tablas4():
    cur4=conn.cursor()

    cur4.execute('SELECT * FROM "Foods"')

    datosFoods = cur4.fetchall()
    
    cur4.close()    
   
    conn.close()
    return datosFoods

Tablas = consulta_tablas()
Tablas2 = consulta_tablas2()
Tablas3 = consulta_tablas3()
Tablas4 = consulta_tablas4()

with open('Tablas.csv','w', newline='') as file:
    writer = csv.writer(file,delimiter=';')
    writer.writerows(Tablas)
    writer.writerows(Tablas2)
    writer.writerows(Tablas3)
    writer.writerows(Tablas4)


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

crear_archivo_texto('customers_'+Fecha +'.csv',Tablas.__str__(),'1vfyZ75fwotCgiNWWE5rifmGLTZjqaRdJ')
crear_archivo_texto('employees_'+Fecha +'.csv',Tablas2.__str__(),'1vfyZ75fwotCgiNWWE5rifmGLTZjqaRdJ')
crear_archivo_texto('foods_'+Fecha +'.csv',Tablas3.__str__(),'1vfyZ75fwotCgiNWWE5rifmGLTZjqaRdJ')
crear_archivo_texto('products_'+Fecha +'.csv',Tablas4.__str__(),'1vfyZ75fwotCgiNWWE5rifmGLTZjqaRdJ')

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
