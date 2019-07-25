'''
Created on 12 may. 2019

@author: Luz Maria Martinez
'''
from src.gestion_datos import datasets
from src.ia import trees
from src.ia import neural_networks
import pandas as pd
import time
import numpy as np
import datetime 
from datetime import timedelta
import os

if __name__ == '__main__':
  
    #Descargamos el dataset con la estaciones de control
    datasets.get_estaciones_control()
    
    #Descargamos los historicos de las estaciones de control
    datasets.get_historicos()
    
    #Descargamos el historico de la climatologia
    datasets.get_climatologia_historico()
    
    #Procesamos el fichero de las estaciones de control y obtenemos el listado de estaciones
    estaciones = datasets.tratar_dataset_estaciones_control()

    #Procesamos el archivo historico de la climatologia
    datasets.tratar_dataset_climatologia_historico()
    
    #Procesamos los historicos de las estaciones de calidad del aire 
    #e incluimos las variables climatologicas procesadas previamente
    datasets.tratar_dataset_historicos_training()

    #Creamos los inputs para los clasificadores
    datasets.crear_input_clasificadores_dataset()


    #Generamos los arboles para cada estacion
    (arbol_28079017, score_arbol_28079017) = trees.generar_arbol (28079017, 6, True)
    (arbol_28079018, score_arbol_28079018) = trees.generar_arbol (28079018, 6, True)
    (arbol_28079024, score_arbol_28079024) = trees.generar_arbol (28079024, 6, True)
    (arbol_28079027, score_arbol_28079027) = trees.generar_arbol (28079027, 6, True)
    (arbol_28079035, score_arbol_28079035) = trees.generar_arbol (28079035, 6, True)
    (arbol_28079036, score_arbol_28079036) = trees.generar_arbol (28079036, 6, True)
    (arbol_28079038, score_arbol_28079038) = trees.generar_arbol (28079038, 6, True)
    (arbol_28079039, score_arbol_28079039) = trees.generar_arbol (28079039, 6, True)
    (arbol_28079040, score_arbol_28079040) = trees.generar_arbol (28079040, 6, True)
    (arbol_28079047, score_arbol_28079047) = trees.generar_arbol (28079047, 6, True)
    (arbol_28079048, score_arbol_28079048) = trees.generar_arbol (28079048, 6, True)
    (arbol_28079049, score_arbol_28079049) = trees.generar_arbol (28079049, 6, True)
    (arbol_28079050, score_arbol_28079050) = trees.generar_arbol (28079050, 6, True)
    (arbol_28079054, score_arbol_28079054) = trees.generar_arbol (28079054, 6, True)
    (arbol_28079055, score_arbol_28079055) = trees.generar_arbol (28079055, 6, True)
    (arbol_28079056, score_arbol_28079056) = trees.generar_arbol (28079056, 6, True)
    (arbol_28079057, score_arbol_28079057) = trees.generar_arbol (28079057, 6, True)
    (arbol_28079058, score_arbol_28079058) = trees.generar_arbol (28079058, 6, True)
    (arbol_28079059, score_arbol_28079059) = trees.generar_arbol (28079059, 6, True)
    (arbol_28079060, score_arbol_28079060) = trees.generar_arbol (28079060, 6, True)
    
    
    #Generamos las redes para cada estacion
    (red_28079017, score_red_28079017) = neural_networks.generar_red_neuronal (28079017, True)
    (red_28079018, score_red_28079018) = neural_networks.generar_red_neuronal (28079018, True)
    (red_28079024, score_red_28079024) = neural_networks.generar_red_neuronal (28079024, True)
    (red_28079027, score_red_28079027) = neural_networks.generar_red_neuronal (28079027, True)
    (red_28079035, score_red_28079035) = neural_networks.generar_red_neuronal (28079035, True)
    (red_28079036, score_red_28079036) = neural_networks.generar_red_neuronal (28079036, True)
    (red_28079038, score_red_28079038) = neural_networks.generar_red_neuronal (28079038, True)
    (red_28079039, score_red_28079039) = neural_networks.generar_red_neuronal (28079039, True)
    (red_28079040, score_red_28079040) = neural_networks.generar_red_neuronal (28079040, True)
    (red_28079047, score_red_28079047) = neural_networks.generar_red_neuronal (28079047, True)
    (red_28079048, score_red_28079048) = neural_networks.generar_red_neuronal (28079048, True)
    (red_28079049, score_red_28079049) = neural_networks.generar_red_neuronal (28079049, True)
    (red_28079050, score_red_28079050) = neural_networks.generar_red_neuronal (28079050, True)
    (red_28079054, score_red_28079054) = neural_networks.generar_red_neuronal (28079054, True)
    (red_28079055, score_red_28079055) = neural_networks.generar_red_neuronal (28079055, True)
    (red_28079056, score_red_28079056) = neural_networks.generar_red_neuronal (28079056, True)
    (red_28079057, score_red_28079057) = neural_networks.generar_red_neuronal (28079057, True)
    (red_28079058, score_red_28079058) = neural_networks.generar_red_neuronal (28079058, True)
    (red_28079059, score_red_28079059) = neural_networks.generar_red_neuronal (28079059, True)
    (red_28079060, score_red_28079060) = neural_networks.generar_red_neuronal (28079060, True)   
    
    #Nos quedamos con el clasficador que tenga mejor score
    if score_arbol_28079017 > score_red_28079017:
        pred_28079017 = arbol_28079017
    else:
        pred_28079017 = red_28079017
        
    if score_arbol_28079018 > score_red_28079018:
        pred_28079018 = arbol_28079018
    else:
        pred_28079018 = red_28079018
        
    if score_arbol_28079024 > score_red_28079024:
        pred_28079024 = arbol_28079024
    else:
        pred_28079024 = red_28079024
        
    if score_arbol_28079027 > score_red_28079027:
        pred_28079027 = arbol_28079027
    else:
        pred_28079027 = red_28079027
        
    if score_arbol_28079035 > score_red_28079035:
        pred_28079035 = arbol_28079035
    else:
        pred_28079035 = red_28079035
        
    if score_arbol_28079036 > score_red_28079036:
        pred_28079036 = arbol_28079036
    else:
        pred_28079036 = red_28079036
        
    if score_arbol_28079038 > score_red_28079038:
        pred_28079038 = arbol_28079038
    else:
        pred_28079038 = red_28079038
        
    if score_arbol_28079039 > score_red_28079039:
        pred_28079039 = arbol_28079039
    else:
        pred_28079039 = red_28079039
        
    if score_arbol_28079040 > score_red_28079040:
        pred_28079040 = arbol_28079040
    else:
        pred_28079040 = red_28079040
        
    if score_arbol_28079047 > score_red_28079047:
        pred_28079047 = arbol_28079047
    else:
        pred_28079047 = red_28079047
        
    if score_arbol_28079048 > score_red_28079048:
        pred_28079048 = arbol_28079048
    else:
        pred_28079048 = red_28079048
        
    if score_arbol_28079049 > score_red_28079049:
        pred_28079049 = arbol_28079049
    else:
        pred_28079049 = red_28079049
        
    if score_arbol_28079050 > score_red_28079050:
        pred_28079050 = arbol_28079050
    else:
        pred_28079050 = red_28079050
        
    if score_arbol_28079054 > score_red_28079054:
        pred_28079054 = arbol_28079054
    else:
        pred_28079054 = red_28079054
        
    if score_arbol_28079055 > score_red_28079055:
        pred_28079055 = arbol_28079055
    else:
        pred_28079055 = red_28079055
        
    if score_arbol_28079056 > score_red_28079056:
        pred_28079056 = arbol_28079056
    else:
        pred_28079056 = red_28079056
        
    if score_arbol_28079057 > score_red_28079057:
        pred_28079057 = arbol_28079057
    else:
        pred_28079057 = red_28079057
        
    if score_arbol_28079058 > score_red_28079058:
        pred_28079058 = arbol_28079058
    else:
        pred_28079058 = red_28079058
        
    if score_arbol_28079059 > score_red_28079059:
        pred_28079059 = arbol_28079059
    else:
        pred_28079059 = red_28079059
        
    if score_arbol_28079060 > score_red_28079060:
        pred_28079060 = arbol_28079060
    else:
        pred_28079060 = red_28079060


    if os.path.exists("../data/dashboard") == False:
        os.mkdir("../data/dashboard")  
        
    print("\n")
    while True:    
        
        try:
            url = datasets.tratar_dataset_tiempo_real()
            (temp, viento, precip) = datasets.tratar_dataset_climatologia_tiempo_real()
            
                
            cab = True
            cab3 = True
            fw=open("../data/dashboard/datos_magnitudes.csv", "a")
            fw.close()
            fw3=open("../data/dashboard/predicion_total.csv", "a")
            fw3.close()
            
            fr=open("../data/dashboard/datos_magnitudes.csv")
            contenido = fr.read()
            if contenido=='':
                cab = False
            fr.close()
            fr=open("../data/dashboard/datos_magnitudes.csv")
            contenido = fr.read()
            if contenido=='':
                cab3 = False
            fr.close()
                
            fw=open("../data/dashboard/datos_magnitudes.csv", "a")
            fw2=open("../data/dashboard/predicciones.csv", "w")
            fw3=open("../data/dashboard/predicion_total.csv", "a")
            
                
            if cab == False:
                fw.write('ESTACION;MAGNITUD;VALOR;FECHA;HORA\n')
                cab = True
                
             
            datos = pd.read_csv (url, delimiter=";")
            df = pd.DataFrame(datos)
            df = df.sort_values(['ESTACION'], ascending=[True])
            
            try:
                df2 = df[df['ESTACION'] == 28079017]
                so2 = str(df2[df2['MAGNITUD'] == 'so2']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'so2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'so2']['HORA'].tolist()[0])
                fw.write("28079017;so2;"+so2+";"+fecha+";"+hora+"\n")
                fw.write("28079017;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079017;o3;"+o3+";"+fecha+";"+hora+"\n")
            
                #Prediccion
                atributos = [float(so2),float(no2),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079017.predict(l_atributos)
                prediccion = float(pr[0])
                fw2.write("28079017;" + str(float(pr[0])) + '\n')        
                del l_atributos
                del atributos
                
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079017))
            
            try:
                df2 = df[df['ESTACION'] == 28079018]
                so2 = str(df2[df2['MAGNITUD'] == 'so2']['VALOR'].tolist()[0])
                co = str(df2[df2['MAGNITUD'] == 'co']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'so2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'so2']['HORA'].tolist()[0])
                fw.write("28079018;so2;"+so2+";"+fecha+";"+hora+"\n")
                fw.write("28079018;co;"+co+";"+fecha+";"+hora+"\n")
                fw.write("28079018;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079018;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                fw.write("28079018;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(so2),float(co),float(no2),float(pm2_5),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079018.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079018;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
                     
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079018))
            
            
            try:
                df2 = df[df['ESTACION'] == 28079024]
                so2 = str(df2[df2['MAGNITUD'] == 'so2']['VALOR'].tolist()[0])
                co = str(df2[df2['MAGNITUD'] == 'co']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm10 = str(df2[df2['MAGNITUD'] == 'pm10']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'so2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'so2']['HORA'].tolist()[0])
                fw.write("28079024;so2;"+so2+";"+fecha+";"+hora+"\n")
                fw.write("28079024;co;"+co+";"+fecha+";"+hora+"\n")
                fw.write("28079024;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079024;pm10;"+pm10+";"+fecha+";"+hora+"\n")
                fw.write("28079024;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                fw.write("28079024;o3;"+o3+";"+fecha+";"+hora+"\n")
            
                #prediccion
                atributos = [float(so2),float(co),float(no2),float(pm10),float(pm2_5),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079024.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079024;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
                
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079024))
                    
            
            try:
                df2 = df[df['ESTACION'] == 28079027]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079027;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079027;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(no2),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079027.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079027;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079027))
            
            
            try:
                df2 = df[df['ESTACION'] == 28079035]
                so2 = str(df2[df2['MAGNITUD'] == 'so2']['VALOR'].tolist()[0])
                co = str(df2[df2['MAGNITUD'] == 'co']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'so2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'so2']['HORA'].tolist()[0])
                fw.write("28079035;so2;"+so2+";"+fecha+";"+hora+"\n")
                fw.write("28079035;co;"+co+";"+fecha+";"+hora+"\n")
                fw.write("28079035;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079035;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(so2),float(co),float(no2),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079035.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079035;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079035))
            
            try:
                df2 = df[df['ESTACION'] == 28079036]
                so2 = str(df2[df2['MAGNITUD'] == 'so2']['VALOR'].tolist()[0])
                co = str(df2[df2['MAGNITUD'] == 'co']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'so2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'so2']['HORA'].tolist()[0])
                fw.write("28079036;so2;"+so2+";"+fecha+";"+hora+"\n")
                fw.write("28079036;co;"+co+";"+fecha+";"+hora+"\n")
                fw.write("28079036;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079036;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(so2),float(co),float(no2),float(pm2_5),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079036.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079036;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079036)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079038]
                so2 = str(df2[df2['MAGNITUD'] == 'so2']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm10 = str(df2[df2['MAGNITUD'] == 'pm10']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'so2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'so2']['HORA'].tolist()[0])
                fw.write("28079038;so2;"+so2+";"+fecha+";"+hora+"\n")
                fw.write("28079038;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079038;pm10;"+pm10+";"+fecha+";"+hora+"\n")
                fw.write("28079038;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                
                
                #prediccion
                atributos = [float(so2),float(no2),float(pm10),float(pm2_5),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079038.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079038;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079038)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079039]
                co = str(df2[df2['MAGNITUD'] == 'co']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'co']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'co']['HORA'].tolist()[0])
                fw.write("28079039;co;"+co+";"+fecha+";"+hora+"\n")
                fw.write("28079039;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079039;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(co),float(no2),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079039.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079039;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079039)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079040]
                so2 = str(df2[df2['MAGNITUD'] == 'so2']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'so2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'so2']['HORA'].tolist()[0])
                fw.write("28079040;so2;"+so2+";"+fecha+";"+hora+"\n")
                fw.write("28079040;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079040;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(so2),float(no2),float(pm2_5),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079040.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079040;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079040)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079047]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm10 = str(df2[df2['MAGNITUD'] == 'pm10']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079047;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079047;pm10;"+pm10+";"+fecha+";"+hora+"\n")
                fw.write("28079047;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(no2),float(pm10),float(pm2_5),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079047.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079047;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079047)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079048]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm10 = str(df2[df2['MAGNITUD'] == 'pm10']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079048;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079048;pm10;"+pm10+";"+fecha+";"+hora+"\n")
                fw.write("28079048;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(no2),float(pm10),float(pm2_5),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079048.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079048;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079048)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079049]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079049;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079049;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(no2),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079049.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079049;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
                
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079049)) 
            
            
            try:
                df2 = df[df['ESTACION'] == 28079050]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm10 = str(df2[df2['MAGNITUD'] == 'pm10']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079050;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079050;pm10;"+pm10+";"+fecha+";"+hora+"\n")
                fw.write("28079050;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                
                
                #prediccion
                atributos = [float(no2),float(pm10),float(pm2_5),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079050.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079050;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079050)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079054]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079054;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079054;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(no2),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079054.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079054;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079054)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079055]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079055;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079055;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(no2),float(pm2_5),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079055.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079055;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079055)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079056]
                co = str(df2[df2['MAGNITUD'] == 'co']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'co']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'co']['HORA'].tolist()[0])
                fw.write("28079056;co;"+co+";"+fecha+";"+hora+"\n")
                fw.write("28079056;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079056;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(co),float(no2),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079056.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079056;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079056)) 
            
            try: 
                df2 = df[df['ESTACION'] == 28079057]
                so2 = str(df2[df2['MAGNITUD'] == 'so2']['VALOR'].tolist()[0])
                co = str(df2[df2['MAGNITUD'] == 'co']['VALOR'].tolist()[0])
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'so2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'so2']['HORA'].tolist()[0])
                fw.write("28079057;so2;"+so2+";"+fecha+";"+hora+"\n")
                fw.write("28079057;co;"+co+";"+fecha+";"+hora+"\n")
                fw.write("28079057;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079057;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(so2),float(co),float(no2),float(pm2_5),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079057.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079057;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079057)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079058]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079058;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079058;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(no2),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079058.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079058;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079058)) 
            
            try:
                df2 = df[df['ESTACION'] == 28079059]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079059;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079059;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(no2),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079059.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079059;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
            
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079059))
            
            try:
                df2 = df[df['ESTACION'] == 28079060]
                no2 = str(df2[df2['MAGNITUD'] == 'no2']['VALOR'].tolist()[0])
                pm2_5 = str(df2[df2['MAGNITUD'] == 'pm2_5']['VALOR'].tolist()[0])
                o3 = str(df2[df2['MAGNITUD'] == 'o3']['VALOR'].tolist()[0])
                fecha = str(df2[df2['MAGNITUD'] == 'no2']['FECHA'].tolist()[0])
                hora = str(df2[df2['MAGNITUD'] == 'no2']['HORA'].tolist()[0])
                fw.write("28079060;no2;"+no2+";"+fecha+";"+hora+"\n")
                fw.write("28079060;pm2_5;"+pm2_5+";"+fecha+";"+hora+"\n")
                fw.write("28079060;o3;"+o3+";"+fecha+";"+hora+"\n")
                
                #prediccion
                atributos = [float(no2),float(pm2_5),float(o3),float(temp),float(viento),float(precip)]
                l_atributos=[]
                l_atributos.append(atributos)
                l_atributos = np.array(l_atributos, "float32")
                pr = pred_28079060.predict(l_atributos)
                if float(pr[0]) > float(prediccion):
                    prediccion = float(pr[0])
                fw2.write("28079060;" + str(float(pr[0])) + '\n')
                del l_atributos
                del atributos  
                
            except IndexError:
                print("--> WARNING: Sin medidas para la estacion " + str(28079060))
            
            if cab3 == False:
                fw3.write("Prediccion;Fecha\n")
                cab3 = True
            
            date = datetime.datetime.strptime(fecha, '%d/%m/%Y').date()
            date = date + timedelta(days=3)
            if date.day < 10:
                dia = "0" + str(date.day)
            else:
                dia = str(date.day)
            if date.month < 10:
                mes = "0" + str(date.month)
            else:
                mes = str(date.month)
            anio = str(date.year)       
            fw3.write(str(prediccion)+";"+ dia + "/" + mes + "/" + anio + "\n")
            
            fw.close()
            fw2.close()
            fw3.close()
            
            localtime = time.asctime( time.localtime(time.time()) )
            print("--> UPDATE: Datos actualizados " + str(localtime))
            
            time.sleep(3598)
        
        except:
            localtime = time.asctime( time.localtime(time.time()) )
            print("--> ERROR: No se han podido obtener medidas para actualizar " + str(localtime))
            time.sleep(300)
