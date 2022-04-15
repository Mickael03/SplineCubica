# Bibliotecas utilizadas
![Numpy](https://img.shields.io/badge/Numpy-1.21.5-brightgreen)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.2.2-brightgreen)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-1.13.5-blue)

# Spline Cúbica
Corresponde a um método de interpolação utilizando polinômios de terceiro grau para determina valores faltantes tendo como referência um conjunto de pontos discretos, a função criada corresponde a uma função continua que passara por todos os pontos do conjunto dado inicialmente de forma que ela será capaz de estima os valores para pontos desconhecidos.

# Funções auxiliares
Na construção da função geral passaremos por três funções auxiliares, ```coeficientes``` função que gerar a matriz dos coeficientes, ```r``` a função que gera a matriz dos termos independentes e ```solucao``` que tem como resultado a solução do sistema linear.

# Função Geral
Por meio das funções auxiliares ela pode retorna dois valores:
1. Os coeficientes da função spline
2. Estima o valor de um ponto

# **Referências**

1. [***Cubic Spline Interpolation***](https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.03-Cubic-Spline-Interpolation.html)
2. [***Spline Cúbica***](https://estudar.com.vc/conceitos/interpolacao-polinomial/spline-cubica)
3. [***Cálculo de um Spline Cúbica Natural***](https://www.ime.unicamp.br/~valle/Teaching/MS211/Aula17complemento.pdf)
4. [***Métodos Numéricos Splines***](https://homepages.dcc.ufmg.br/~assuncao/an/splines.pdf)
5. [***Interpolação cúbica segmentada - spline***](https://www.ufrgs.br/reamat/CalculoNumerico/livro-py/i1-interpolacao_cubica_segmentada_-_spline.html)
6. [***Interpolação Polinomial Spline Cúbica***](https://www.ime.usp.br/mat/2458/textos/splines.pdf)
7. [***Funções em LaTeX***](https://app.mettzer.com/latex#fun%C3%A7%C3%B5es)
