from math import pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dU_dx(U,t,g,l,r,w):
        return [U[1], -g/l*np.sin(U[0]) + (r/l*((w)**2))*np.cos(U[0] - w*t)]
