from scipy.stats import norm,chi2
from math import sqrt
import matplotlib.pyplot as plt
from scipy import stats

def media(lista):   
    acum = 0
    for i in lista:
        acum += i
        
    return acum / len(lista)  
  
def prueba_media(lista, alfa):
    med = media(lista)
    z = norm.ppf(1 - (alfa / 2))
    
    n = len(lista)
   
    li = 0.5 - z * (1 / sqrt(12 * n))
    ls = 0.5 + z * (1 / sqrt(12 * n))
    
    return med >= li and med <= ls
    
def varianza(lista):
    med = media(lista)
    acum = 0
    for i in lista:
        acum += (i - med) * (i - med)
        
    return acum / (len(lista) - 1)

def prueba_varianza(lista, alfa):
    var = varianza(lista)
    n = len(lista)
    chi_1 = chi2.ppf(1 - (alfa / 2), n - 1)
    
    chi_2 = chi2.ppf(alfa / 2, n - 1)
    ls = chi_1 / (12 * (n - 1))
    li = chi_2 / (12 * (n - 1))
    
    return var >= li and var <= ls

def prueba_uniformidad(lista, alfa):
    n = len(lista)
    m = round(sqrt(n))
    inter = 1 / m
    #ver cuantos datos estan en el intervalo
    lista_ordenada = sorted(lista)
    lista_cantidad = []
    rango = inter
    cont = 0
    cont2 = 0
    
    for i in lista_ordenada:
        cont2 += 1
        
        if i < rango or abs(i - rango) < 0.000001:
            cont += 1

        else:
            lista_cantidad.append(cont)  
            cont = 1
            rango += inter
            
        if(cont2==len(lista)):
            lista_cantidad.append(cont)
            
    #frecuencia esperada        
    ei = n / m
    #chi observada
    chi_observado = 0
    
    for i in lista_cantidad:
        chi_observado += ((ei - i) ** 2) / ei
    
    chi_esperado = chi2.ppf(1 - alfa, m - 1)
  
    return chi_observado < chi_esperado
    
def grafica(lista):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    res = stats.probplot(lista, dist = stats.norm, sparams = (6,), plot = ax)
    plt.show()



