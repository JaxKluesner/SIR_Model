# This is a program for basic SIR Model.
# Thanks to professor Hans-Werner Van Wyck for an introduction to the subject matter and a basic version of code.

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
t = np.linspace(0, T, 1000)


y0 = [susc, inf, rec]

# The function of population over time f[susc, inf, rec].
# First term is susceptible and so on separated by commas.
f = lambda y,t: [inf_rate * y[0] * y[1],
                 inf_rate * y[0] * y[1] - rec_rate * y[1],
                 rec_rate * y[1]]

# Throws excess work warning (Apparently for R0> 1).
# Calculates the solution to f over time.
y_sol = odeint(f, y0, t)

# Beginning of graphing.
fig = plt.figure(figsize=(15, 10));
plt.plot(t, y_sol[:,0],'-', label= 'Susceptible')
plt.plot(t, y_sol[:,1],'--', label= 'Infected')
plt.plot(t, y_sol[:,2],'-.', label= 'Recovered')
plt.ylim(0,pop)
plt.xlim(0,100)
plt.title("Population Over Time")
plt.xlabel("Time (days)")
plt.ylabel("Population")
plt.legend()