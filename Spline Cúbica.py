#Bibliotecas utilizadas
import matplotlib.pyplot as plt
import numpy as np

#Coeficientes da matriz
def coeficientes(x = []):
    #Número de equações
    n_equacao = len(x) - 1
    
    #Matriz dos coeficientes
    coeficientes = []
    
    #Condição I
    i = 1
    j = 0
    while i <= n_equacao:
        k = [0 for i in range(4*n_equacao)]
        k[j] = 1
        
        coeficientes.append(k)
        
        j += 4
        i += 1
    
    #Condição II
    i = 0
    j = 0
    while i < n_equacao:
        k = [0 for i in range(4*n_equacao)]
        k[j]  = 1
        k[j+1] = x[i+1] - x[i]
        k[j+2] = (x[i+1] - x[i])**2
        k[j+3] = (x[i+1] - x[i])**3
        coeficientes.append(k)
        j += 4
        i += 1
    
    #Condição III
    i = 0
    j = 0
    while i < n_equacao - 1:
        k = [0 for i in range(4*n_equacao)]
        k[j+1] = 1
        k[j+2] = 2*(x[i+1] - x[i])
        k[j+3] = 3*(x[i+1] - x[i])**2
        k[j+5] = -1
        coeficientes.append(k)
        j += 4
        i += 1
    
    #Condição IV
    i = 0
    j = 0
    while i < n_equacao-1:
        k = [0 for i in range(4*n_equacao)]
        k[j+2] = 2
        k[j+3] = 6*(x[i+1] - x[i])
        k[j+6] = -2
        
        if i < n_equacao -1:
            coeficientes.append(k)
        
        j += 4
        i += 1
    
    #Condição V
    i = 0
    j = 0
    while i < n_equacao:
        k = [0 for i in range(4*n_equacao)]
        if i == 0:
            k[j+2] = 2
            k[j+3] = 0
            coeficientes.append(k)
        if i == n_equacao - 1:
            k[j+2] = 2
            k[j+3] = 6*(x[i+1] - x[i])
            coeficientes.append(k)
        j += 4
        i += 1
    
    return coeficientes

def r(y = []):
    #Número de equações
    n_equacoes = len(y) - 1
    
    #Lista com resultados não nulos
    z = [y[i] for i in range(len(y)-1)] + [y[i] for i in range(len(y)) if i >= 1]
    
    #complementado a lista para solução do sistema matricial
    for i in range(4*n_equacoes - len(z)):
        z.append(0)
    
    return z

#Solução do sistema matricial
def solucao(x = [], y = []):
    
    #Matriz dos coeficientes
    A = coeficientes(x)
    
    #Matriz dos termos independentes
    b = r(y)
    
    #Solução pelo numpy
    solve = np.linalg.solve(A,b)
    l2 = [i for i in solve]
    
    return l2

#Função Spline cubico natural
def Spline_Cubica(x = [], y = [], **kwargs):
    
    #Coeficientes do spline cubica
    coeficientes = solucao(x,y)
    
    #Mostra os coeficientes
    Coef = kwargs.get('coeficientes')
    if Coef == True:
        return coeficientes
    
    #Determinação do valor de um spline 
    valor = kwargs.get('valor')
    
    if valor != None:
        #Determinação dos coeficientes a serem utilizados
        count = 0
        while count < len(x):
            if count == len(x) - 2:
                break
            if valor <= x[count]:
                break
            if x[count] < valor <= x[count+1]:
                break
            count += 1
        
        #resultados
        s0 = coeficientes[4*count + 0]
        s1 = coeficientes[4*count + 1]*(valor - x[count])
        s2 = coeficientes[4*count + 2]*(valor - x[count])**2
        s3 = coeficientes[4*count + 3]*(valor - x[count])**3
        
        #Valor do Spline para valor
        s = s0 + s1 + s2 + s3 
        
        return s
