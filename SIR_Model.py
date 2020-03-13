import numpy as np
import matplotlib as mplib
import matplotlib.pyplot as plt
from scipy.integrate import odeint

susc = int(input("Enter initial susceptible population: "))
inf = int(input("Enter the initial number infected: "))
rec = int(input("Enter the initial number of recovered persons: "))
inf_rate = float(input("Enter the infection rate: "))
rec_rate = float(input("Enter the recovery rate: "))
pop = susc + inf + rec

# Generally in notation as R0 but called threshold here.
threshold = inf_rate * susc / rec_rate

s_prime = lambda susc: susc * inf_rate
i_prime = lambda susc, inf: susc * inf_rate - inf * rec_rate
r_prime = lambda inf: inf * rec_rate

#Timescale
T = 100
t = np.linspace(0,T,1000)


y0 = [susc, inf, rec]
#print(y0)

f = lambda y,t: [inf_rate * y[0] * y[1],
                 inf_rate * y[0] * y[1] - rec_rate * y[1],
                 rec_rate * y[1]]

y_sol = odeint(f, y0, t)