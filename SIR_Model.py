import numpy as np
import matplotlib as mplib
import matplotlib.pyplot as plt
from scipy.integrate import odeint

s0 = int(input("Enter total susceptible population: "))
i0 = int(input("Enter the number infected: "))
r0 = int(input("Enter the number of recovered persons: "))
inf_rate = float(input("Enter the infection rate: "))
rec_rate = float(input("Enter the recovery rate: "))
pop = s0 + i0 + r0

# Generally in notation as R0 but called threshold here.
threshold = inf_rate * s0 / rec_rate

