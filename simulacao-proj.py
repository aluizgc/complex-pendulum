# Importação das bibliotecas necessárias

import math
import numpy as np
import matplotlib.pyplot as plt
import os, sys, cv2
from scipy.integrate import odeint
from solucaoedo import dU_dx
from os.path import isfile, join
sys.getdefaultencoding()

# Definição das variáveis. Estes valores podem e devem ser alterados
# para que resultados variados sejam obtidos

t0 = 0 # Tempo inicial
tf = 500 # Tempo final
tp = 0.1 # Passo de iteração do tempo
g = 9.81 # Gravidade
l = 9 # Comprimento da haste
r = 30 # Raio da espira
w = 1.1 # Frequência

# Definição dos tempoe para gráfico e simulação

tempo =  np.arange(t0,tf,tp)
tempo2 = np.linspace(t0,tf,250)
ptsSim = len(tempo2)
i = np.arange(0,ptsSim,1)

# Resolve a EDO

U0 = [math.pi/4,0]
ys = odeint(dU_dx, U0, tempo, args=(g,l,r,w))
phi = ys[:,0]

# Parametrização do problema

x1 = r*np.cos(w*tempo)
y1 = -r*np.sin(w*tempo)
x2 = r*np.cos(w*tempo) + l*np.sin(phi)
y2 = -r*np.sin(w*tempo) + l*np.cos(phi)
x = x1+x2
y = y1+y2

# As seguintes linhas de código são responsáveis pela plotagem 
# de cada imagem com os valores das parametrizações para os 
# resultados obtidos com a resolução da EDO
#  
for point in i:
    plt.figure()
    plt.plot(x2[point],y2[point],'bs',label='Massa', markersize=7)
    plt.plot(x1[point],y1[point],'ro',label='Ponto de suspenção',markersize=7)
    plt.plot([x1[point],x2[point]], [y1[point],y2[point]], 'k-')
    plt.legend(loc='upper right', frameon=False)
    plt.xlim(-r-50,r+50)
    plt.ylim(-r-50,r+50)
    plt.text(-65,60,'Gravidade (g): {}'.format(g))
    plt.text(-65,52,'Comprimento (l): {}'.format(l))
    plt.text(-65,44,'Raio (r): {}'.format(r))
    plt.text(-65,36,'Frequência (w): {}'.format(w))
    plt.xlabel('eixo-x')
    plt.ylabel('eixo-y')
    filenumber = point
    filenumber=format(filenumber,"05")
    plt.savefig("imagens/image{}.png".format(filenumber))
    plt.close()

# Definição da função para conversão das imagens em video

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    files.sort(key = lambda x: int(x[5:-4]))
    for i in range(len(files)):
        filename=pathIn + files[i]
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()
 
def main():
    pathIn= './imagens/'
    pathOut = 'video.avi'
    fps = 25.0
    convert_frames_to_video(pathIn, pathOut, fps)
 
if __name__=="__main__":
    main()