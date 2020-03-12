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