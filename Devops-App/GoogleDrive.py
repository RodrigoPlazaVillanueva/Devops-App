

import csv
import logging
import psycopg2
import time
from datetime import date
from datetime import datetime

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from datetime import date
from datetime import datetime

#Exportar tablas
#Logs


while True:

    logging.basicConfig(filename="logFile.txt",
                format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                   datefmt="%d-%m-%Y %H:%M:%S %p",
                   level=logging.DEBUG
                   )


    logging.info('Ejecuntando la aplicación')

    conn = psycopg2.connect(
    host="192.168.113.132",
    database="rest-market",
    user="postgres",
    password="postgres",
    port="5432")

    if(not conn):
        logging.eror('No se pudo conectar a la base de datos')

    logging.debug('Conexión exitosa')

    def consulta_tablas():
        cur1=conn.cursor()

        cur1.execute('SELECT * FROM "Customers"')

        datosCustomer = cur1.fetchall()

        cur1.close()
        logging.debug('Select * FROM "Customers" Exitoso')
        return datosCustomer



    def consulta_tablas2():
        cur2=conn.cursor()

        cur2.execute('SELECT * FROM "Employees"')

        datosEmployees = cur2.fetchall()
        
        cur2.close()    
        logging.debug('Select * FROM "Employees" Exitoso')
        return datosEmployees

    def consulta_tablas3():
        cur3=conn.cursor()

        cur3.execute('SELECT * FROM "Foods"')

        datosFoods = cur3.fetchall()
        
        cur3.close()    
        logging.debug('Select * FROM "Foods" Exitoso')
        return datosFoods

    def consulta_tablas4():
        cur4=conn.cursor()

        cur4.execute('SELECT * FROM "Products"')

        datosProducts = cur4.fetchall()
        
        cur4.close()    
        logging.debug('Select * FROM "Products" Exitoso')
        conn.close()
        return datosProducts

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
        logging.warning('Necesitas estar conectado a internet')
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

    time.sleep(600)
