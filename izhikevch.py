###Icaro Rodolfo S. C. Paz
###MODELO IZHIKEVCH SIMPLES

## codificacao ASCII
# coding=UTF8

##Bibliotecas
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import set_matplotlib_formats

##INSERCAO DE DADOS
h=0.5 #largura do passo
TI=300 # intervalo de tempo inicial
AC=5 # amplitude da corrente

t = np.arange(0,1000.1,h) # periodo de tempo de 1000ms (1s)

def entrada(TI,AC):
    I=np.zeros(len(t)) # corrente
    
    for k in range (0,len(t)):
        if t[k] > TI:
            I[k]=AC # amplitude de corrente
    return I


###Solucao numerica
def Modelo(a,b,u,v,I):
    v = v + h*(0.04*v*v+5*v+140-u+I) # potencial discreto da membrana do neuronio
    u = u + h*(a*(b*v-u)) # variavel de restituicao
    return u,v

##Codigo principal
def Izhikevich(a,b,c,d):
    v=-65*np.ones(len(t)) # valor inicial do potencial da membrana
    u=np.zeros(len(t)) # variavel de restituicao
    u[0]=b*v[0] # valor inical da variavel de restituicao
    I=entrada(TI,AC)
    
## Metodo de Euler
    for k in range(0, len(t) -1):
        u[k+1], v[k+1]=Modelo(a,b,u[k],v[k],I[k]) # resolvedo a equacao numericamente

        if v[k+1]>30: # restituicao
            v[k+1]=c
            u[k+1]=u[k+1]+d
    plot_entrada_saida(t,v,I,a,b,c,d)

#Resultados do codigo
def plot_entrada_saida(t,v,I,a,b,c,d):
##Plotando
    fig, ax1 = plt.subplots(figsize=(9,4))
    ax1.plot(t, v, 'k-',label='Saida')
    ax1.set_xlabel('tempo (ms)')

    plt.text(0.5,0.5, 'a: %s \nb: %s \nc: %s \nd: %s' %(a,b,c,d), fontsize=13, color='black',bbox=dict(boxstyle='round', facecolor='wheat',alpha=0.5)) #caixa de texto
    
    #plotando saida
    ax1.set_ylabel('Potencial de membrana (mV)')
    ax1.tick_params('y', color='k')
    ax1.set_ylim(-95,40)
    ax2 = ax1.twinx()

    #plotando entrada em eixos diferentes
    ax2.plot(t,I,'orangered',label='Entrada')
    ax2.set_ylim(0,AC*20)
    ax2.set_ylabel('Estímulo (mV)', color='orangered')
    ax2.tick_params('y', colors='orangered')
    fig.tight_layout()
    ax1.set_title('Spiking Regular (RS)')

    #resolucao, formato e armazenamento do grafico
    set_matplotlib_formats('pdf', 'png')
    plt.rcParams['savefig.dpi'] = 300
    #plt.savefig('RS.png')
    
    #exibicao
    plt.show()

Izhikevich(0.02,0.2,-65,8) #RS
#Izhikevich(0.02,0.2,-55,4) #IB
#Izhikevich(0.02,0.2,-50,2) #CH
#Izhikevich(0.02,0.25,-65,0.05) #TC
#Izhikevich(0.02,0.25,-65,2) #LTS
#Izhikevich(0.1,0.2,-65,2) #FS
#Izhikevich(0.1,0.26,-65,2) #RZ
