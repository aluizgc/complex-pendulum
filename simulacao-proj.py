import math
import numpy as np
import matplotlib.pyplot as plt
import os, sys, cv2
from scipy.integrate import odeint
from solucaoedo import dU_dx
from os.path import isfile, join

sys.getdefaultencoding()
#Variáveis 
t0 = 0
tf = 500
tp = 0.1
g = 9.81
l = 5
r = 25
w = 0.5

#Tempo para gráfico e simulação
tempo =  np.arange(t0,tf,tp)
tempo2 = np.linspace(t0,tf,250)
ptsSim = len(tempo2)
i = np.arange(0,ptsSim,1)

#Resolve edo
U0 = [math.pi/4,0]
ys = odeint(dU_dx, U0, tempo, args=(g,l,r,w))
phi = ys[:,0]
#Parametrização
x1 = r*np.cos(w*tempo)
y1 = -r*np.sin(w*tempo)
x2 = r*np.cos(w*tempo) + l*np.sin(phi)
y2 = -r*np.sin(w*tempo) + l*np.cos(phi)
x = x1+x2
y = y1+y2

#Plota gráficos
#print('tempo', tempo)
#print('tempo2', tempo2)
'''plt.plot(tempo/10,phi)
plt.xlabel("Tempo (s)")
plt.ylabel("\u03A8 (t)")
#plt.legend()
plt.show()
'''


for point in i:

    plt.figure()
    plt.plot(x2[point],y2[point],'bs',markersize=7)
    plt.plot(x1[point],y1[point],'ro',markersize=7)
    #plt.plot(0,0,'o--',mfc='none',markersize=4*r)
    plt.plot([x1[point],x2[point]], [y1[point],y2[point]], 'k-')
    plt.xlim(-r-50,r+50)
    plt.ylim(-r-50,r+50)
    plt.xlabel('eixo-x')
    plt.ylabel('eixo-y')
    filenumber = point
    filenumber=format(filenumber,"05")
    #filename="image{}.png".format(filenumber)
    plt.savefig("imagens/image{}.png".format(filenumber))
    plt.close()


def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
 
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
 
def main():
    pathIn= './imagens/'
    pathOut = 'video.avi'
    fps = 25.0
    convert_frames_to_video(pathIn, pathOut, fps)
 
if __name__=="__main__":
    main()