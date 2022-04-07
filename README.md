# Bibliotecas utilizadas
![Numpy](https://img.shields.io/badge/Numpy-1.21.5-brightgreen)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.2.2-brightgreen)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-1.13.5-blue)

# Spline Cúbica
Corresponde a um método de interpolação utilizando polinômios de terceiro grau para determina valores faltantes tendo como referência um conjunto de pontos discretos, a função criada corresponde a uma função continua que passara por todos os pontos do conjunto dado inicialmente de forma que ela será capaz de estima os valores para pontos desconhecidos.

# Funções auxiliares
Na construção dos função geral passaremos por três 'funções auxiliares' duas destinadas a construção dos um sistema de equações matriciais, ```coeficientes``` e ```r```, e a função ```solucao``` que apresenta a solução dos sistema linear apresentado.
## Matriz dos coeficientes
```python
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
```
## Matriz com resultados dos sistema matricial
```python
def r(y = []):
  #Número de equações
  n_equacoes = len(y) - 1

  #Lista com resultados não nulos
  z = [y[i] for i in range(len(y)-1)] + [y[i] for i in range(len(y)) if i >= 1]

  #complementado a lista para solução do sistema matricial
  for i in range(4*n_equacoes - len(z)):
    z.append(0)
    
  return z
```
## Solução do sistema matricial 
```python
def solucao(x = [], y = []):
  A = coeficientes(x)
  b = r(y)

  solve = np.linalg.solve(A,b)
  l2 = [i for i in solve]
  
  return l2
```
## Função Spline Cubica geral
Função geral Spline Cúbica apresenta paramentros para apresentação dos **coeficientes do spline**, **gráfico** e um **valor específico** do spline sendo necessário somente informamos qual da informação nos interessa.  
```python
def Spline_Cubica(x = [], y = [], **kwargs):
  
  #Coeficientes do spline cubica
  coeficientes = solucao(x,y)
  
  #Mostra os coeficientes da função spline
  A = kwargs.get('coeficientes')

  if A == True:
    return coeficientes

  #Gráfido da função
  grafico = kwargs.get('grafico')

  #Codígo de construção de gráfico
  if grafico == True:

    plt.plot(x, y, 'ro', label='Dados')
    
    z = [i for i in np.arange(x[0]-0.5,x[len(x)-1] + 0.5,0.01)]
    k = [Spline_Cubica(x,y,valor = i) for i in z]
    plt.plot(z, k, label = 'Curva Spline Cubica')
    
    plt.xlabel('Eixo - x')
    plt.ylabel('Eixo - y')
    plt.title('Eixo : X - Eixo : Y')
    plt.grid(True)

    plt.legend()
    plt.show()

    return
  
  #Determinação do valor de um spline 
  valor = kwargs.get('valor')

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
 ```

# **Referências**

1. [***Cubic Spline Interpolation***](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.03-Cubic-Spline-Interpolation.html)
2. [***Spline Cúbica***](https://estudar.com.vc/conceitos/interpolacao-polinomial/spline-cubica)
3. [***Cálculo de um Spline Cúbica Natural***](https://www.ime.unicamp.br/~valle/Teaching/MS211/Aula17complemento.pdf)
4. [***Métodos Numéricos Splines***](https://homepages.dcc.ufmg.br/~assuncao/an/splines.pdf)
5. [***Interpolação cúbica segmentada - spline***](https://www.ufrgs.br/reamat/CalculoNumerico/livro-py/i1-interpolacao_cubica_segmentada_-_spline.html)
6. [***Interpolação Polinomial Spline Cúbica***](https://www.ime.usp.br/mat/2458/textos/splines.pdf)
7. [***Funções em LaTeX***](https://app.mettzer.com/latex#fun%C3%A7%C3%B5es)
