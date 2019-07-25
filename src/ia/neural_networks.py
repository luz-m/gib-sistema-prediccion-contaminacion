'''
Created on 10 jun. 2019

@author: Luz Maria Martinez
'''

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report  
from sklearn.neural_network import MLPClassifier

def generar_red_neuronal (codigo,  estadisticas=True):
    """Genera una red neuronal (clasificadora)

    Devuelve la red neuronal generada y el porcentaje de acierto al validar el modelo con el conjunto de entrenamiento.

    Parametros:
    codigo -- codigo de la estacion de calidad del aire
    estadisticas -- True si se quiere exportar un fichero con estadisticas. False si no se quiere generar. Por defecto True

    
    """
    
    path = "../data/entrenamiento/" + str(codigo) + "/"
    
    f = open(path + "data_neural_network_" + str(codigo) + ".txt")
    cab = str(f.readline())[:-1]
    cab = cab.replace("'","")
    cab = cab.replace(" ","")
    cabeceras = cab[1:-1].split(",")
    l_etiquetas = str(f.readline())[:-1].split(",")
    atributos = str(f.readline())[:-1].split(",,")
    f.close()

    l_atributos = []
    for atributo in atributos:
        l_atributos.append(atributo.split(","))

    etiquetas = set(l_etiquetas) 
    clases = sorted(list(etiquetas))
    
    l_atributos = np.array(l_atributos, "float32")
    l_etiquetas = np.array(l_etiquetas, "float32")
    

    #Separamos los datos que vamos a utilizar de entrenamiento y para realizar el test
    #datos de pruebas (0.25) de los de entrenamiento (0.75)
    X_train, X_test, y_train, y_test = train_test_split(l_atributos,l_etiquetas,test_size = 0.25,random_state = 0)

    red = MLPClassifier(max_iter=100000, hidden_layer_sizes=(50,25))
    
    red.fit(X_train, y_train)

    
    y_pred = red.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)  



    if estadisticas == True:
        f=open(path + "export_neural_network_statistics_" + str(codigo) + ".txt","w")  
        f.write("************************ CLASS *************************\n")
        for i in range(len(clases)):
            f.write(str(clases[i]) + "\n")
        f.write("\n\n")
        f.write("********************** FEATURES  **********************\n")
        for i in range(len(cabeceras[:-1])):
            f.write(str(cabeceras[i]) + "\n")
        f.write("\n\n")
        f.write("************************ SCORE *************************\n")
        f.write("With Test data: " + str(red.score(X_test, y_test)) + "\n")
        f.write("With Training data: " + str(red.score(X_train, y_train)) + "\n")
        f.write("\n\n")
        f.write("****************** CONFUSION MATRIX ********************\n")
        if len(clases)==2:
            f.write("\t0\t1\n")
            f.write("---------------------\n")
            f.write("0 |\t"+ str(cm[0][0]) +"\t"+ str(cm[0][1]) +"\n")
            f.write("1 |\t"+ str(cm[1][0]) +"\t"+ str(cm[1][1]) +"\n")
        if len(clases)==3:
            f.write("\t0\t1\t2\n")
            f.write("--------------------------------\n")
            f.write("0 |\t"+ str(cm[0][0]) +"\t"+ str(cm[0][1]) +"\t"+ str(cm[0][2]) +"\n")
            f.write("1 |\t"+ str(cm[1][0]) +"\t"+ str(cm[1][1]) +"\t"+ str(cm[1][2]) +"\n")
            f.write("2 |\t"+ str(cm[2][0]) +"\t"+ str(cm[2][1]) +"\t"+ str(cm[2][2]) +"\n")
        if len(clases)==4:
            f.write("\t0\t1\t2\t3\n")
            f.write("----------------------------------------------\n")
            f.write("0 |\t"+ str(cm[0][0]) +"\t"+ str(cm[0][1]) +"\t"+ str(cm[0][2]) +"\t"+ str(cm[0][3]) +"\n")
            f.write("1 |\t"+ str(cm[1][0]) +"\t"+ str(cm[1][1]) +"\t"+ str(cm[1][2]) +"\t"+ str(cm[1][3]) +"\n")
            f.write("2 |\t"+ str(cm[2][0]) +"\t"+ str(cm[2][1]) +"\t"+ str(cm[2][2]) +"\t"+ str(cm[2][3]) +"\n")
            f.write("3 |\t"+ str(cm[3][0]) +"\t"+ str(cm[3][1]) +"\t"+ str(cm[3][2]) +"\t"+ str(cm[3][3]) +"\n")
        f.write("\n\n")
        f.write("************************ REPORT ***********************\n")
        f.write(report)
        f.close()
    
    print(str(codigo) + ": neural network created")     
    return (red, red.score(X_test, y_test)) 
