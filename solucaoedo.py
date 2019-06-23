from math import pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dU_dx(U,t,g,l,r,w):
    # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
        return [U[1], g/l*np.sin(U[0]) - (r*((w/l)**2))*np.cos(U[0] - w*t)]
