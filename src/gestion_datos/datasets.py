'''
Created on 12 may. 2019

@author: Luz Maria Martinez
'''


from xml.dom import minidom 
from src.gestion_datos import datos_web
import os
import requests
import json
import xlrd
import shutil
import pandas as pd
from src.gestion_datos import datasets
from datetime import datetime
from lxml import html



def get_estaciones_control ():
    """Descarga el dataset con la estaciones de control de aire, su ubicacion y las magnitudes que mide cada una. Lo guarda en disco.

    Excepciones:
    ValueError -- Si la funcion descargarArchivosUrl propaga algun error. 
    
    """
    
    urlDescargar = "https://datos.madrid.es/egob/catalogo/212629-0-estaciones-control-aire.xls"
    urlGuardar = "../data/estaciones_control/212629-0-estaciones-control-aire.xls"   

    try:     
        datos_web.descargarArchivosUrl (urlDescargar, urlGuardar, 0)     
    except ValueError as descripcion:
        print("Ocurrio un error previsto:", descripcion)

    
def get_historicos ():
    """Descarga los ficheros con los datos historicos de calidad del aire desde el anio 2001 hasta la actualidad
    Los guarda en disco.
    
    Devuelve una lista con las ubicaciones de todos los datasets guardados en local

    Excepciones:
    ValueError -- Si la funcion descargarArchivosUrl propaga algun error. 
    
    """
    
    urlDescargar = 'https://datos.madrid.es/egob/catalogo/201410-0-calidad-aire-diario.dcat'
    urlGuardar = "../data/historico/201410-0-calidad-aire-diario.dcat" 
    
    lista = []
    
    try:     
        datos_web.descargarArchivosUrl (urlDescargar, urlGuardar, 0)     
        lurls = []
        doc = minidom.parse(urlGuardar)
        urls = doc.getElementsByTagName("dcat:accessURL")
        for url in urls:
            u = url.firstChild.data
            if(u[len(u)-3:]=="csv"):
                lurls.append(u)

        for url in lurls:
            datos_web.descargarArchivosUrl (url, "../data/historico/" + os.path.basename(url) , 2) 
            lista.append("../data/historico/" + os.path.basename(url))    
        
        return lista
        
    except ValueError as descripcion:
        print("Ocurrio un error previsto:", descripcion)

 
def get_tiempo_real ():
    """Descarga el dataset con la informacion de las medidas realizadas por la estaciones (actualizaciones cda hora). 
    Lo guarda en disco.

    Excepciones:
    ValueError -- Si la funcion descargarArchivosUrl propaga algun error. 
    
    """
    
    urlDescargar = 'https://datos.madrid.es/egob/catalogo/212531-0-calidad-aire-tiempo-real.dcat'
    urlGuardar = "../data/tiempo_real/212531-0-calidad-aire-tiempo-real.dcat" 
    
    try:     
        datos_web.descargarArchivosUrl (urlDescargar, urlGuardar, 0)     
        doc = minidom.parse(urlGuardar)
        urls = doc.getElementsByTagName("dcat:accessURL")
        url = urls[-1].firstChild.data
        datos_web.descargarArchivosUrl (url[:-3] + "txt", "../data/tiempo_real/" + os.path.basename(url)[:-3] + "txt" , 0)  
        

    except ValueError as descripcion:
        print("Ocurrio un error previsto:", descripcion)


def get_climatologia_historico():  
    """Descarga el fichero JSON con los datos historicos de la climatologia de Madrid desde el anio 2001 
    hasta la actualidad. Lo guarda en disco.

    Excepciones:
    ValueError -- Si la funcion descargarArchivosUrl propaga algun error. 
    
    """
    
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsdXptYXJpYS5tdHRAZ21haWwuY29tIiwianRpIjoiN2RhMTJlNmUtZjQwYy00MzM0LTg3ZjQtZDQyYWMyZTVkNDllIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE1NjE0MDA5ODksInVzZXJJZCI6IjdkYTEyZTZlLWY0MGMtNDMzNC04N2Y0LWQ0MmFjMmU1ZDQ5ZSIsInJvbGUiOiIifQ.qW9CktlZH6615wTVZEZrAwM8RZgKPk5KyXRJrQv7PE4" 
    url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2014-06-01T00%3A00%3A00UTC/fechafin/2019-05-31T23%3A59%3A59UTC/estacion/3195"
    url2 = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2009-06-01T00%3A00%3A00UTC/fechafin/2014-05-31T23%3A59%3A59UTC/estacion/3195"
    url3 = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2004-06-01T00%3A00%3A00UTC/fechafin/2009-05-31T23%3A59%3A59UTC/estacion/3195"
    url4 = "https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/2001-01-01T00%3A00%3A00UTC/fechafin/2004-05-31T23%3A59%3A59UTC/estacion/3195"    
    
    querystring = {"api_key":api_key}
    
    headers = {
        'cache-control': "no-cache"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    decoded = json.loads(response.content)
    response2 = requests.request("GET", url2, headers=headers, params=querystring)
    decoded2 = json.loads(response2.content)
    response3 = requests.request("GET", url3, headers=headers, params=querystring)
    decoded3 = json.loads(response3.content)
    response4 = requests.request("GET", url4, headers=headers, params=querystring)
    decoded4 = json.loads(response4.content)
    
    try:
        datos_web.descargarArchivosUrl(decoded["datos"], "../data/clima_historico/aemet_historico_datos_1.json", 0)  
        datos_web.descargarArchivosUrl(decoded["metadatos"], "../data/clima_historico/aemet_historico_metadatos_1.json", 0) 
        datos_web.descargarArchivosUrl(decoded2["datos"], "../data/clima_historico/aemet_historico_datos_2.json", 0)  
        datos_web.descargarArchivosUrl(decoded2["metadatos"], "../data/clima_historico/aemet_historico_metadatos_2.json", 0) 
        datos_web.descargarArchivosUrl(decoded3["datos"], "../data/clima_historico/aemet_historico_datos_3.json", 0)  
        datos_web.descargarArchivosUrl(decoded3["metadatos"], "../data/clima_historico/aemet_historico_metadatos_3.json", 0) 
        datos_web.descargarArchivosUrl(decoded4["datos"], "../data/clima_historico/aemet_historico_datos_4.json", 0)  
        datos_web.descargarArchivosUrl(decoded4["metadatos"], "../data/clima_historico/aemet_historico_metadatos_4.json", 0) 
    except ValueError as descripcion:
        print("Ocurrio un error previsto:", descripcion)
        

def get_climatologia_tiempo_real():  
    """Descarga el dataset con la informacion de la climatologia en el dia. Lo guarda en disco.
    El valor de las precipitaciones en mm, se obtiene de la web www.eltiempo.es ya que el dataset
    anterior cuenta con el porcentaje de probabilidad de lluvia, pero no con el valor en mm

    Devuelve el valor de las precipitaciones obtenidas por web scrapping
    
    Excepciones:
    ValueError -- Si la funcion descargarArchivosUrl propaga algun error. 
    
    """
    
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJsdXptYXJpYS5tdHRAZ21haWwuY29tIiwianRpIjoiN2RhMTJlNmUtZjQwYy00MzM0LTg3ZjQtZDQyYWMyZTVkNDllIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE1NjE0MDA5ODksInVzZXJJZCI6IjdkYTEyZTZlLWY0MGMtNDMzNC04N2Y0LWQ0MmFjMmU1ZDQ5ZSIsInJvbGUiOiIifQ.qW9CktlZH6615wTVZEZrAwM8RZgKPk5KyXRJrQv7PE4" 
    url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/28079"
    
    querystring = {"api_key":api_key}

    headers = {
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    decoded = json.loads(response.content)
    
    try:
        datos_web.descargarArchivosUrl(decoded["datos"], "../data/clima_real/predicion_diaria.json", 0)  
        datos_web.descargarArchivosUrl(decoded["metadatos"], "../data/clima_real/metadatos_predicion_diaria.json", 0)
         
    except ValueError as descripcion:
        print("Ocurri\xf3 un error previsto:", descripcion)
    
    page = requests.get('https://www.eltiempo.es/madrid.html')
    tree = html.fromstring(page.content)
    
    precip = tree.xpath('//*[@id="cityTable"]/div/article/div[1]/div[2]/div[1]/div[7]/span[2]/text()')
        
    return str(precip)[2:-5]


def tratar_dataset_estaciones_control():
    """Procesa el dataset de la estaciones de control. 
    Crea una lista con diccionarios donde cada diccionario son los datos de una estacion.
    
    Devuelve un objeto lista con los diccionarios con la informacion sobre las estaciones
    
    """
    
    doc = xlrd.open_workbook("../data/estaciones_control/212629-0-estaciones-control-aire.xls")
    estaciones = doc.sheet_by_index(0)
    
    lestaciones =[]
   
    for i in range(estaciones.nrows): 
        if (i > 4) and (i < 29):
            fila = estaciones.row(i) 
            for j in range(len(fila)):
                if (j == 1):
                    numero = int(fila[j].value)
                    codigo = int(28079000 + numero)
                elif (j == 2):
                    estacion = fila[j].value
                elif (j == 3):
                    direccion = fila[j].value
                elif (j == 4):
                    longitud = fila[j].value
                elif (j == 5):
                    latitud = fila[j].value
                elif (j == 6):
                    altitud = int(fila[j].value)
                elif (j == 7):
                    tipo_estacion = fila[j].value  
                elif (j == 8):
                    no2 = False
                    if fila[j].value == "X":
                        no2 = True
                elif (j == 9):
                    so2 = False
                    if fila[j].value == "X":
                        so2 = True
                elif (j == 10):
                    co = False
                    if fila[j].value == "X":
                        co = True  
                elif (j == 11):
                    pm10 = False
                    if fila[j].value == "X":
                        pm10 = True                     
                elif (j == 12):
                    pm2_5 = False
                    if fila[j].value == "X":
                        pm2_5 = True 
                elif (j == 13):
                    o3 = False
                    if fila[j].value == "X":
                        o3 = True
                elif (j == 14):
                    btx = False
                    if fila[j].value == "X":
                        btx = True 
                elif (j == 15):
                    hc = False
                    if fila[j].value == "X":
                        hc = True  
                elif (j == 16):
                    uv = False
                    if fila[j].value == "X":
                        uv = True
                elif (j == 17):
                    vv = False
                    if fila[j].value == "X":
                        vv = True
                elif (j == 18):
                    dv = False
                    if fila[j].value == "X":
                        dv = True  
                elif (j == 19):
                    tmp = False
                    if fila[j].value == "X":
                        tmp = True
                elif (j == 20):
                    hr = False
                    if fila[j].value == "X":
                        hr = True 
                elif (j == 21):
                    prb = False
                    if fila[j].value == "X":
                        prb = True 
                elif (j == 22):
                    rs = False
                    if fila[j].value == "X":
                        rs = True  
                elif (j == 23):
                    ll = False
                    if fila[j].value == "X":
                        ll = True
                          
            est = {'codigo' : codigo, 'numero' : numero, 'estacion' : estacion, 'direccion' : direccion, 'longitud' : longitud, 'latitud' : latitud, 'altitud' : altitud, 'tipo_estacion' : tipo_estacion, 'no2' : no2, 'so2' : so2, 'co' : co, 'pm10' : pm10, 'pm2_5' : pm2_5, 'o3' : o3, 'btx' : btx, 'hc' : hc, 'uv' : uv, 'vv' : vv, 'dv' : dv, 'tmp' : tmp, 'hr' : hr, 'prb' : prb, 'rs' : rs, 'll' : ll}                         
            lestaciones.append(est)            
        
    return lestaciones


def tratar_dataset_climatologia_historico ():
    """Procesa el dataset historico de la climatologia. 
    Crea una nuevo fichero llamado clima_hist.csv con los datos relevantes.
    Deja los registros ordenados por fecha, desde el mas actual al mas antiguo. 
    
    """    
    
    cont_ficher = 1
    
    f=open("../data/clima_historico/clima_hist.csv","w")
    f.write("anio;mes;dia;temperatura;viento;precipitacion\n")
        
    while cont_ficher < 5:
        with open("../data/clima_historico/aemet_historico_datos_"+ str(cont_ficher) +".json") as file:
            data = json.load(file)
            
            for elemento in data:
                
                try:
                    fecha = elemento['fecha']
                    
                    try:
                        temp = elemento['tmed']
                    except KeyError:
                        temp = ""
                    try:
                        precip = elemento['prec']
                    except KeyError:
                        precip = ""
                    try:
                        viento = elemento['velmedia']
                    except KeyError:
                        viento = ""
                    
                except KeyError:
                    pass
                
                linea = fecha[:4] + ";" + fecha[5:7] + ";" + fecha[8:] + ";" + temp + ";" + viento + ";" + precip
                linea = linea.replace(",",".")
                f.write(linea + "\n") 
    
        cont_ficher += 1
    
    f.close()
       
    datos = pd.read_csv ("../data/clima_historico/clima_hist.csv", delimiter=";")
    df = pd.DataFrame(datos)
    df2 = df.sort_values(['anio', 'mes', 'dia'], ascending=[False, False, False])
    os.remove("../data/clima_historico/clima_hist.csv")
    df2.to_csv("../data/clima_historico/clima_hist.csv", index=False, sep=";")


def tratar_dataset_historicos_training():
    """Procesa los datasets resultados de tratar los datos historicos. Unifica tanto las medidas de las magnitudes como los valores del clima. 
    Genera una carpeta llamada entrenamiento en la que dentro se hayara una carpeta con el codigo de cada estacion que a su vez contendra un 
    fichero con los datos historicos completos de esa estacion.
    Preparados para su posterior procesado como datos de entrenamiento.
    
    """    
        
    lista_his_estaciones = get_historicos()
    
    f=open("../data/entrenamiento/fase1.csv","w")
    
    f.write('ESTACION;MAGNITUD;ANO;MES;DIA;VALOR\n')
    
    for archivo in lista_his_estaciones:
        datos = pd.read_csv (archivo, delimiter=";")
        df = pd.DataFrame(datos)
       
        size = df.shape
        for i in range(size[0]):
            estacion = str(df['PUNTO_MUESTREO'][i])[0:8]
            magnitud = str(df['PUNTO_MUESTREO'][i])[9:11]
            if magnitud[1] == "_":
                magnitud = magnitud[0]
            anio = df['ANO'][i]
            mes = df['MES'][i]          
            
            d1 = df['D01'][i]
            if df['V01'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';1;' + str(d1) + '\n')
            d2 = df['D02'][i]
            if df['V02'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';2;' + str(d2) + '\n')
            d3 = df['D03'][i]
            if df['V03'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';3;' + str(d3) + '\n')
            d4 = df['D04'][i]
            if df['V04'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';4;' + str(d4) + '\n')
            d5 = df['D05'][i]
            if df['V05'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';5;' + str(d5) + '\n')
            d6 = df['D06'][i]
            if df['V06'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';6;' + str(d6) + '\n')
            d7 = df['D07'][i]
            if df['V07'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';7;' + str(d7) + '\n')
            d8 = df['D08'][i]
            if df['V08'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';8;' + str(d8) + '\n')    
            d9 = df['D09'][i]
            if df['V09'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';9;' + str(d9) + '\n')
            d10 = df['D10'][i]
            if df['V10'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';10;' + str(d10) + '\n')
            d11 = df['D11'][i]
            if df['V11'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';11;' + str(d11) + '\n')    
            d12 = df['D12'][i]
            if df['V12'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';12;' + str(d12) + '\n')
            d13 = df['D13'][i]
            if df['V13'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';13;' + str(d13) + '\n')
            d14 = df['D14'][i]
            if df['V14'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';14;' + str(d14) + '\n')
            d15 = df['D15'][i]
            if df['V15'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';15;' + str(d15) + '\n')
            d16 = df['D16'][i]
            if df['V16'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';16;' + str(d16) + '\n')
            d17 = df['D17'][i]
            if df['V17'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';17;' + str(d17) + '\n')
            d18 = df['D18'][i]
            if df['V18'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';18;' + str(d18) + '\n')
            d19 = df['D19'][i]
            if df['V19'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';19;' + str(d19) + '\n')
            d20 = df['D20'][i]
            if df['V20'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';20;' + str(d20) + '\n')
            d21 = df['D21'][i]
            if df['V21'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';21;' + str(d21) + '\n')
            d22 = df['D22'][i]
            if df['V22'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';22;' + str(d22) + '\n')
            d23 = df['D23'][i]
            if df['V23'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';23;' + str(d23) + '\n')    
            d24 = df['D24'][i]
            if df['V24'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';24;' + str(d24) + '\n')
            d25 = df['D25'][i]
            if df['V25'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';25;' + str(d25) + '\n')
            d26 = df['D26'][i]
            if df['V26'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';26;' + str(d26) + '\n')
            d27 = df['D27'][i]
            if df['V27'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';27;' + str(d27) + '\n')
            d28 = df['D28'][i]
            if df['V28'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';28;' + str(d28) + '\n')
            d29 = df['D29'][i]
            if df['V29'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';29;' + str(d29) + '\n')
            d30 = df['D30'][i]
            if df['V30'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';30;' + str(d30) + '\n')
            d31 = df['D31'][i]
            if df['V31'][i] == "V":
                f.write(str(estacion) + ';' + str(magnitud) + ';' + str(anio) + ';' + str(mes) + ';31;' + str(d31) + '\n')
       
    f.close()   


    datos = pd.read_csv ("../data/entrenamiento/fase1.csv", delimiter=";")
    df = pd.DataFrame(datos)
    
    
    estaciones = datasets.tratar_dataset_estaciones_control()
    
    #Guardamos un fichero por cada estacion
    if os.path.exists("../data/entrenamiento/estaciones") == False:
        os.mkdir("../data/entrenamiento/estaciones")
    
    for estacion in estaciones:
        codigo = int(estacion['codigo'])
        df2 = df[df['ESTACION'] == codigo]
        df2 = df2.sort_values(['ANO', 'MES', 'DIA', 'MAGNITUD'], ascending=[False, False, False, True])
        df2.to_csv("../data/entrenamiento/estaciones/" + str(codigo) + ".csv", index=False, sep =";")
    
    
    
    #**************************
    
    datos_clima = pd.read_csv ("../data/clima_historico/clima_hist.csv", delimiter=";")   
    df_clima = pd.DataFrame(datos_clima)

    dic_clima = {}
    size = df_clima.shape
    for n in range(size[0]):
        key = str(df_clima['anio'][n]) + "-" + str(df_clima['mes'][n]) + "-" + str(df_clima['dia'][n])
        valor = str(df_clima['temperatura'][n]) + ";" + str(df_clima['viento'][n]) + ";" + str(df_clima['precipitacion'][n])
        dic_clima.update({key:valor})
    
    #*************************
    
    for estacion in estaciones:

        pathw = "../data/entrenamiento/" + str(estacion['codigo'])
        pathr = "../data/entrenamiento/estaciones/"
        
        cab = False
        if os.path.exists(pathw) == False:
            os.mkdir(pathw)
        f=open(pathw + "/data_test_" + str(estacion['codigo']) + ".csv","w")
        
        no2 = "NaN"
        no2_c = False
        no2_c_2 = False
        so2 = "NaN"
        so2_c = False
        so2_c_2 = False
        co = "NaN"
        co_c = False
        co_c_2 = False
        pm10 = "NaN"
        pm10_c = False
        pm10_c_2 = False
        pm2_5 = "NaN"
        pm2_5_c = False
        pm2_5_c_2 = False
        o3 = "NaN"
        o3_c = False 
        o3_c_2 = False
        
        cab = False  
    
        datos = pd.read_csv (pathr + str(estacion['codigo']) + '.csv', delimiter=";")   
        df = pd.DataFrame(datos)
                
        size = df.shape
        

        
        for k in range(size[0]):
            
            if k == 0:
                anio = str(df['ANO'][k])
                mes = str(df['MES'][k])
                dia = str(df['DIA'][k])
            
            if dia == str(df['DIA'][k]):
                
                magnitud = str(df['MAGNITUD'][k])
                valor = str(df['VALOR'][k])
                
                if magnitud == "1":
                    so2 = valor
                    so2_c = True
                elif magnitud == "6":
                    co = valor
                    co_c = True
                elif magnitud == "8":
                    no2 = valor
                    no2_c = True
                elif magnitud == "9":
                    pm10 = valor
                    pm10_c = True
                elif magnitud == "10":
                    pm2_5 = valor
                    pm2_5_c = True
                elif magnitud == "14":
                    o3 = valor
                    o3_c = True       
                
            else:
                #escribimos la cabecera primero
                if cab == False:
                    cabecera = ""
                    if so2_c == True:
                        cabecera = cabecera + 'so2;'
                        so2_c_2 = True
                    if co_c == True:
                        cabecera = cabecera + 'co;'
                        co_c_2 = True
                    if no2_c == True:
                        cabecera = cabecera + 'no2;'
                        no2_c_2 = True
                    if pm10_c == True:
                        cabecera = cabecera + 'pm10;'
                        pm10_c_2 = True
                    if pm2_5_c == True:
                        cabecera = cabecera + 'pm2_5;'
                        pm2_5_c_2 = True
                    if o3_c == True:
                        cabecera = cabecera + 'o3;'
                        o3_c_2 = True
                    cabecera = cabecera + "temp;viento;precipitacion"
                    f.write(cabecera + "\n")
                    cab = True   
                
                #escribimos la linea
                linea = ""
                if so2_c_2 == True:
                    linea = linea + str(so2) + ';'
                if co_c_2 == True:
                    linea = linea + str(co) + ';'
                if no2_c_2 == True:
                    linea = linea + str(no2) + ';'
                if pm10_c_2 == True:
                    linea = linea + str(pm10) + ';'
                if pm2_5_c_2 == True:
                    linea = linea + str(pm2_5) + ';'
                if o3_c_2 == True:
                    linea = linea + str(o3) + ';'
             
                clave = anio + "-" + mes + "-" + dia
                    
                if clave in dic_clima:
                    linea = linea + dic_clima[clave]
                    f.write(linea + "\n") 
            
                anio = str(df['ANO'][k])
                mes = str(df['MES'][k])
                dia = str(df['DIA'][k])

                magnitud = str(df['MAGNITUD'][k])
                valor = str(df['VALOR'][k])                
                
                if magnitud == "1":
                    so2 = valor
                elif magnitud == "6":
                    co = valor
                elif magnitud == "8":
                    no2 = valor
                elif magnitud == "9":
                    pm10 = valor
                elif magnitud == "10":
                    pm2_5 = valor
                elif magnitud == "14":
                    o3 = valor
        
        f.close()               
            
    
    os.remove("../data/entrenamiento/fase1.csv")
    shutil.rmtree("../data/entrenamiento/estaciones")
    
    for estacion in estaciones:
        codigo = int(estacion['codigo'])
        path = "../data/entrenamiento/" + str(codigo) + "/"
       
        datoss = pd.read_csv (path + "data_test_" + str(codigo) + ".csv", delimiter=";")
        df = pd.DataFrame(datoss)
        
        
        f=open(path + "/data_totest_" + str(estacion['codigo']) + ".csv","w")
        cabeceras = df.dtypes.index.tolist()
        cab = ""
        for cabecera in cabeceras:
            cab = cab + cabecera + ";"
        cab = cab + "n_predicion"
        f.write(cab + "\n")
        
        size = df.shape 
        for k in range(size[0]): 
            if k < 3:
                linea=""
                for i in range(size[1]):
                    linea = linea + str(df[cabeceras[i]][k]) + ";"
                prediccion = 'NaN'
                linea = linea + str(prediccion)
                f.write(linea + "\n")
            
            if k >= 4:
                linea=""
                for i in range(size[1]):
                    linea = linea + str(df[cabeceras[i]][k]) + ";"
                v_umbral = df['no2'][k-3] 
                if v_umbral >= 50:
                    prediccion = 1
                elif v_umbral >= 100:
                    prediccion = 2
                elif v_umbral >= 150:
                    prediccion = 3
                elif v_umbral >= 200:
                    prediccion = 4
                else:
                    prediccion = 0
                linea = linea + str(prediccion)
                linea = linea.replace('nan','NaN')
                linea = linea.replace('Ip','NaN')
                f.write(linea + "\n")
            
        f.close()   
        
        os.remove(path + "data_test_" + str(codigo) + ".csv")

         
def crear_input_clasificadores_dataset ():
    """Procesado final en el que se eliminan los registros nulos y se da formato a los datos por cada estacion.
    Partiendo del archivo de cada estacion data_totest_<estacion>.csv se formatearan los datos y se guardaran en dos ficheros, 
    uno para el arbol y el otro para la red neuronal (data_tree_<estacion>.txt y data_neuronal_network_<estaccion>.txt)
    
    """  
    
    estaciones = datasets.tratar_dataset_estaciones_control()
    for estacion in estaciones:
        codigo = int(estacion['codigo'])
        
        path = "../data/entrenamiento/" + str(codigo) + "/"
        
        datos = pd.read_csv (path + "data_totest_" + str(codigo) + ".csv", delimiter=";")
        df = pd.DataFrame(datos)
        #Eliminamos valores nulos
        df = df.dropna()
        
        cabeceras = df.dtypes.index.tolist()
        #reseteamos los indices
        df = df.reset_index(drop = True)
        #obtenemos el tamanio del df
        size = df.shape
        
        
        lineaAtributos = ""
        lineaEtiquetas = ""
        
        for k in range(size[0]):
        
            lineaEtiquetas = lineaEtiquetas + str(df['n_predicion'][k]) + ","
            for i in range(len(cabeceras)-1):
                cab = cabeceras[i]
                valor = df[cab][k]
                lineaAtributos = lineaAtributos + str(valor) + ","
                
            lineaAtributos = lineaAtributos[:-1] + ",,"

        lineaEtiquetas = lineaEtiquetas[:-1]
        lineaAtributos = lineaAtributos[:-2]
                     
    
        f=open(path + "data_tree_" + str(codigo) + ".txt","w")
        f.write(str(cabeceras) + "\n")
        f.write(lineaEtiquetas + "\n")
        f.write(lineaAtributos + "\n")
        f.close()

        f=open(path + "data_neural_network_" + str(codigo) + ".txt","w")
        f.write(str(cabeceras) + "\n")
        f.write(lineaEtiquetas + "\n")
        f.write(lineaAtributos + "\n")
        f.close()
        

def tratar_dataset_climatologia_tiempo_real():
    """Tras invocar a la funcion get_climatologia_tiempo_real() para la descarga del dataset con las medidas en tiempo real de la climatologia, lo procesa. 
    
    Devuelve tres valores, la temperatura, el viento y las precipitaciones.
    
    """ 
 
    
    precip = float(datasets.get_climatologia_tiempo_real())
    
    
    with open("../data/clima_real/predicion_diaria.json") as file:
        data = json.load(file)
        
        #viento
        contador = 0
        viento = 0
        for elemento in data[0]['prediccion']['dia'][0]['viento']:
            viento = viento + int(elemento['velocidad'])
            contador += 1
        viento = round(viento / contador, 5)
        
        #temperatura
        contador = 0
        temp = 0
        for elemento in data[0]['prediccion']['dia'][0]['temperatura']['dato']:
            temp = temp + elemento['value']
            if int(elemento['value']) != 0:   
                contador += 1
        temp = round(temp / contador, 5)
        
        return (temp, viento, precip)


def tratar_dataset_tiempo_real():
    """Tras invocar a la funcion get_tiempo_real() para la descarga del dataset con las medidas en tiempo real de las estaciones, lo procesa. 
    Genera un nuevo fichero unico con las medidas de todas las estaciones.
    
    Devuelve un string con la url donde se encuentra almacenado el fichero salida
    
    """
        
    get_tiempo_real()
    
    fw=open("../data/tiempo_real/calidad_aire_real_procesado.csv","w")
    fw.write('ESTACION;MAGNITUD;FECHA;HORA;VALOR\n')
    
    fr=open("../data/tiempo_real/212531-7916318-calidad-aire-tiempo-real.txt")
    for linea in fr:
        datos = linea.split(',')
        magnitud=""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        if int(datos[3]) == 1:
            magnitud = 'so2'
        elif int(datos[3]) == 6:
            magnitud = 'co'
        elif int(datos[3]) == 8:
            magnitud = 'no2'
        elif int(datos[3]) == 9:
            magnitud = 'pm10'
        elif int(datos[3]) == 10:
            magnitud = 'pm2_5'
        elif int(datos[3]) == 14:
            magnitud = 'o3'
        
        ahora = datetime.now()
        hora = ahora.hour
        if ahora.minute < 35:
            if hora == 0:
                hora = 22
            elif hora == 1:
                hora = 23
            else:
                hora = hora - 2
        else:
            if hora == 0:
                hora = 23
            else:
                hora = hora -1
        
        
        valor = str(datos[int(hora)*2+9]) 
        if magnitud != "":    
            fw.write(str(datos[0]) + str(datos[1]) + str(datos[2]) + ";" + magnitud + ";" + str(datos[8]) + "/" + str(datos[7]) + "/" + str(datos[6]) + ";" + str(hora) + ":00" + ";" + str(valor) + "\n")
        
    fr.close()
    fw.close()

    return "../data/tiempo_real/calidad_aire_real_procesado.csv"

