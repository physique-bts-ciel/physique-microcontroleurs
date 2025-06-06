''' David THERINCOURT - Mai 2025
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

##### IMPORTATION DONNEES CSV ######
T, R = np.loadtxt('data_ctn_1.txt', delimiter='\t', skiprows=2, unpack=True)

##### MODELE #### beta = 3285.800975703323 	R0 = 10357.192752653316
T0 = 25
beta = 3286
R0 = 10360
Tmod = np.linspace(0,90,100)
Rmod = R0*np.exp(beta*(1/(Tmod+273.15)-1/(T0+273.15)))


#### COURBES ####
plt.rcParams["figure.figsize"] = (7,5)  # width, height in inches (100 dpi)

plt.plot(T, R, "+")
plt.plot(Tmod, Rmod)
plt.title(r"Caractéristique $R=f(T)$ d'une CTN 10K")
plt.xlim(0,90)
plt.xlabel(r'$T$ (°)')
plt.ylim()
plt.ylabel(r'$R~(\Omega)$')
plt.grid()

plt.tight_layout() # Reglage automatique des marges
plt.savefig("CTN_courbe_ctn10k.png")
plt.show()