import math
def clases_grouped(datos):
    
    # Calcula el rango de los datos
    rango = max(datos) - min(datos)
    
    # Calcula el número de clases utilizando la fórmula de Sturges
    clases = 1+math.log((6))*3.3
    
    mostrar = clases
    print(clases)
    
    # Redondea el número de clases al entero más cercano y resta 1 para evitar clases vacías
    clases_redondear = round(clases)-1
    
    # Calcula el ancho de cada clase
    ancho = rango / clases_redondear
    
    # Inicializa listas para los límites inferiores, superiores y marcas de clase
    lim_inf = [min(datos)]
    lim_sup = []
    mrks = []
    
    # Itera sobre el número de clases y calcula los límites inferiores, superiores y marcas de clase para cada clase
    for i in range(clases_redondear - 1):
        lim_inf.append(round(lim_inf[-1] + ancho, 3))
        lim_sup.append(round(lim_inf[-2] + ancho, 3))
        mrks.append(round((lim_inf[-1] + lim_sup[-1]) / 2, 3))
    
    # Agrega el límite superior máximo y la marca de clase correspondiente a la última clase
    lim_sup.append(max(datos))
    mrks.append(round((lim_sup[-1] + lim_inf[-1]) / 2, 3))
    
    # Convierte la lista de clases en una lista de números enteros (1, 2, 3,...)
    clases_num = list(range(1, clases_redondear + 1))
    
    # Devuelve las clases, límites inferiores, superiores y marcas de clase
    return clases_num, [round(x, 3) for x in lim_inf], [round(x, 3) for x in lim_sup], [round(x, 3) for x in mrks]