'''
Created on 12 may. 2019

@author: Luz Maria Martinez
'''

import wget
from unipath import Path
import os

def descargarArchivosUrl (urlDescargar = None, urlGuardar = None, accion = 0):
    """Descarga un archivo de la web mediante la url y lo guarda en disco.

    Devuelve True si se ha descargado y guardado el archivo correctamente, sino devolvera False.

    Parametros:
    urlDescargar -- url del archivo a descargar
    urlGuardar -- ruta donde se desea guardar el dataset (incluido el nombre del fichero)
    accion -- 0 = reemplazar el archivo si existe, 1 = guardar con otro nombre sin reemplazar (nombre (n), n=1,2,3...), 2 = no sustituir ni guardar el archivo si existe. 

    Excepciones:
    ValueError -- Si (urlDescargar = None) o (urlGuardar = None) 
    
    """
    
    if (urlDescargar == None) or (urlGuardar == None):
        raise ValueError('Error en las rutas')
    else:
        f = Path(urlGuardar)
        existe = f.exists()
        
        if (accion == 2) and (existe == True):
            return False
        else:
            if (accion == 0) and (existe == True):
                os.remove(urlGuardar)
            wget.download(urlDescargar, urlGuardar)  
            return True

