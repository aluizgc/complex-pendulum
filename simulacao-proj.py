import pygame, sys, math
import numpy as np 
import time 
from pygame.locals import *
from solucaoedo import dU_dx
from scipy.integrate import odeint 

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption('Simulação de Pêndulo')
screen = pygame.display.set_mode((800,600))

# Definição da função slider 

def slider(xmin,xmax,yposi,yposf,button,b):
    if button[0]!=0:
        pos = pygame.mouse.get_pos()
        xc = pos[0]
        yc = pos[1]
        if (xc < b-xmin) or (xc >b+xmax):
            pass
        if (yc>yposi and yc<yposf):
            if xc<xmin:
                xc = xmin   
            if xc>xmax:
                xc = xmax
            return(xc)
        else:
            return(b)
    if button[0] == 0:
        xc = b   
        return(xc)


t0 = 0
tf = 1000
tp = 0.1
g = 9.81
l = 5
r = 25
w = 0.5
cont = 0
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
isPlaying = False
while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPlaying = True
    if (isPlaying == True):
        U0 = [math.pi/4,0]
        ys = odeint(dU_dx, U0, tempo, args=(g,l,r,w))
        phi = ys[:,0]
        while cont in range(len(tempo)):
            print('oi')
            isPlaying = False
        
    pygame.display.flip()