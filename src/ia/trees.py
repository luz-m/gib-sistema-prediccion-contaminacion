'''
Created on 10 jun. 2019

@author: Luz Maria Martinez
'''

from sklearn import tree
from sklearn.tree.export import export_text
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report  
import numpy as np



def generar_arbol (codigo, profundidad=5, estadisticas=True):
    """Genera un arbol de decision (clasificador)

    Devuelve el arbol generado y el porcentaje de acierto al validar el modelo con el conjunto de entrenamiento.

    Parametros:
    codigo -- codigo de la estacion de calidad del aire
    profundidad -- profundidad maxima del arbol. Por defecto 5
    estadisticas -- True si se quiere exportar un fichero con estadisticas. False si no se quiere generar. Por defecto True

    
    """
    
    path = "../data/entrenamiento/" + str(codigo) + "/"
    
    f = open(path + "data_tree_" + str(codigo) + ".txt")
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
    
    l_etiquetas = np.array(l_etiquetas)
    l_atributos = np.array(l_atributos)
    
    etiquetas = set(l_etiquetas) 
    clases = sorted(list(etiquetas))

        
    #Separamos los datos que vamos a utilizar para entrenar y para validar.
    #datos de validacion (0.25) / datos de entrenamiento (0.75)
    X_train, X_test, y_train, y_test = train_test_split(l_atributos,l_etiquetas,test_size = 0.25,random_state = 0)
    
    #Normalizacion de los datos
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    
    #Creamos el arbol con la profundidad indicada
    arbol = tree.DecisionTreeClassifier(max_depth=profundidad, criterion = 'entropy', random_state = 0) 
    
    
    #Entrenamos el arbol
    arbol.fit(X_train, y_train)
  
    #Exportar el arbol en texto
    r = export_text(arbol, feature_names=cabeceras[:-1]) 
'''
Created on 10 jun. 2019

@author: Luz Maria Martinez
'''

from sklearn import tree
from sklearn.tree.export import export_text
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report  
import numpy as np



def generar_arbol (codigo, profundidad=5, estadisticas=True):
    """Genera un arbol de decision (clasificador)

    Devuelve el arbol generado y el porcentaje de acierto al validar el modelo con el conjunto de entrenamiento.

    Parametros:
    codigo -- codigo de la estacion de calidad del aire
    profundidad -- profundidad maxima del arbol. Por defecto 5
    estadisticas -- True si se quiere exportar un fichero con estadisticas. False si no se quiere generar. Por defecto True

    
    """
    
    path = "../data/entrenamiento/" + str(codigo) + "/"
    
    f = open(path + "data_tree_" + str(codigo) + ".txt")
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
    
    l_etiquetas = np.array(l_etiquetas)
    l_atributos = np.array(l_atributos)
    
    etiquetas = set(l_etiquetas) 
    clases = sorted(list(etiquetas))

        
    #Separamos los datos que vamos a utilizar para entrenar y para validar.
    #datos de validacion (0.25) / datos de entrenamiento (0.75)
    X_train, X_test, y_train, y_test = train_test_split(l_atributos,l_etiquetas,test_size = 0.25,random_state = 0)
    
    #Normalizacion de los datos
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    
    #Creamos el arbol con la profundidad indicada
    arbol = tree.DecisionTreeClassifier(max_depth=profundidad, criterion = 'entropy', random_state = 0) 
    
    
    #Entrenamos el arbol
    arbol.fit(X_train, y_train)
  
    #Exportar el arbol en texto
    r = export_text(arbol, feature_names=cabeceras[:-1]) 
    f=open(path + "export_tree_text_" + str(codigo) + ".txt","w")  
    f.write(r)
    f.close()
    
    #Exportar datos del arbol .dot
    export_graphviz(arbol,out_file=path + 'export_tree_' + str(codigo) + '.dot',class_names=clases,
                feature_names=cabeceras[:-1],impurity=False,filled=True)
    

    
    # Predicion de los resultados del bloque test
    y_pred = arbol.predict(X_test)
    #Matriz de confusion
    cm = confusion_matrix(y_test, y_pred)

    #Reportes
    report = classification_report(y_test, y_pred)
    

    if estadisticas == True:
        f=open(path + "export_tree_statistics_" + str(codigo) + ".txt","w")  
        f.write("************************ CLASS *************************\n")
        for i in range(len(clases)):
            f.write(str(clases[i]) + "\n")
        f.write("\n\n")
        f.write("********************* MAX DEPTH ************************\n")
        f.write(str(profundidad) + "\n")
        f.write("\n\n")
        f.write("***************** FEATURE IMPORTANCES ******************\n")
        featur_imp = arbol.feature_importances_
        for i in range(len(cabeceras[:-1])):
            f.write(str(cabeceras[i]) + ": " + str(featur_imp[i]) + "\n")
        f.write("\n\n")
        f.write("************************ SCORE *************************\n")
        f.write("With Test data: " + str(arbol.score(X_test, y_test)) + "\n")
        f.write("With Training data: " + str(arbol.score(X_train, y_train)) + "\n")
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
    
    print(str(codigo) + ": tree created")  
    return (arbol, arbol.score(X_test, y_test))
