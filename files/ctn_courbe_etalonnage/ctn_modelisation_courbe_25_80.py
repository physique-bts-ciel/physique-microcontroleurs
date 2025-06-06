''' David THERINCOURT - Mai 2025
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

##### IMPORTATION DONNEES CSV ######
T, R = np.loadtxt('data_ctn_1.txt', delimiter='\t', skiprows=2, unpack=True)
T = T[5:]
R = R[5:]

#### THEORIE ####
def fct(T, beta, R0):
    T0 = 25
    return R0*np.exp(beta*(1/(T+273.15)-1/(T0+273.15)))

(beta, R0), pcov = curve_fit(fct, T, R)
print("beta =", beta, "\tR0 =", R0) # B=3291 R0=10358
Tmod = np.linspace(0,90,100)
Rmod = fct(Tmod, beta, R0)


#### COURBES ####
plt.rcParams["figure.figsize"] = (7,5)  # width, height in inches (100 dpi)

plt.plot(T, R, "+", label='Mesures')
plt.plot(Tmod, Rmod, label='Modélisation')
plt.axvspan(25,80, color='C3', alpha=0.1)
plt.text(30,20E3,r'$R = R_0 \times e^{\beta(\frac{1}{T+273.15}-\frac{1}{25+273.15})}$', size='xx-large', backgroundcolor="white")
plt.text(30,15E3,r'$\beta\approx3440\rm~K$', size='large', backgroundcolor="white")
plt.text(50,15E3,r'$R_0\approx10,6\rm~k\Omega$', size='large', backgroundcolor="white")
plt.legend(loc=1)
plt.title(r"Modélisation de la caractéristique d'une CTN")
plt.xlim(0,90)
plt.xlabel(r'$T$ (°)')
plt.ylim()
plt.ylabel(r'$R~(\Omega)$')
plt.grid()

plt.tight_layout() # Reglage automatique des marges
plt.savefig("CTN_modelisation_courbe_ctn10k.png")
plt.show()