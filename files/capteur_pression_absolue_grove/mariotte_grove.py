import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from physapp.modelisation import ajustement_affine

V, P = np.loadtxt("data.txt",delimiter='\t',skiprows=2, unpack=True)

def fct1(V,A,Vo):       # Vo = volume manquant contenu dans le tube
    return A/(V+Vo)

(A, Vo), pcov = curve_fit(fct1,V,P)

V2 = np.linspace(0,100,100)
P2 = fct1(V2,A,Vo)

def fct2(x,K):
    return K*x

(K), pcov = curve_fit(fct2,1/(V+Vo),P)

Vinv = np.linspace(0,0.06,101)
P3 = fct2(Vinv,K)


plt.title("Loi de Mariotte avec module Grove MPX5700AP")
plt.plot(V, P, '+', label='Mesures')
plt.plot(V2, P2, label='Modélisation')
plt.legend()
plt.text(60,230,r'$P\times(V+V_0) = K$', size='x-large', backgroundcolor="white")
plt.text(60,200,r'$K\approx 6830~\rm kPa\cdot mL$   ', size='large', backgroundcolor="white")
plt.text(60,175,r'$V_0\approx 6,03~\rm ml$', size='large', backgroundcolor="white")
plt.xlabel('V (mL)')
plt.xlim(0,100)
plt.ylabel('P (kPa)')
plt.ylim(0,300)
plt.grid()
plt.tight_layout()
plt.savefig("mariotte_grove_courbe_1.png")

plt.figure()
plt.title("Loi de Mariotte avec module Grove MPX5700AP")
plt.plot(1/(V+Vo), P, '+', label='Mesures')
plt.plot(Vinv,P3, label='Modélisation')
plt.legend()
plt.text(0.03,135,r'$P = K \times\dfrac{1}{V+V_0}$', size='x-large', backgroundcolor="white")
plt.text(0.03,100,r'$K\approx 6830~\rm kPa\cdot mL$   ', size='large', backgroundcolor="white")
plt.text(0.03,75,r'$V_0\approx 6,03~\rm mL$', size='large', backgroundcolor="white")
plt.grid()
plt.xlabel(r'$\dfrac{1}{V+V_0}~\rm(ml^{-1})$')
plt.xlim(0,0.05)
plt.ylabel('P (kPa)')
plt.ylim(0,300)
plt.tight_layout()
plt.savefig("mariotte_grove_courbe_2.png")

plt.show()
