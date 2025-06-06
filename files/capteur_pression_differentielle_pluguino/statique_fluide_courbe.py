import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from physapp.modelisation import ajustement_affine

h, P = np.loadtxt("data.txt",delimiter='\t',skiprows=5, unpack=True)
h = h*1E-2

modele = ajustement_affine(h, P)


plt.title("Loi de la statique des fluides - Module Plug'Uino")
plt.plot(h, P, '+', label='Mesures')
modele.plot()
plt.legend()
#plt.text(60,230,r'$P\times(V+V_0) = K$', size='x-large', backgroundcolor="white")
#plt.text(60,200,r'$K\approx 6830~\rm kPa\cdot mL$   ', size='large', backgroundcolor="white")
#plt.text(60,175,r'$V_0\approx 6,03~\rm ml$', size='large', backgroundcolor="white")
plt.xlabel('h (m)')
#plt.xlim(0,100)
plt.ylabel(r'$\Delta P~\rm(Pa)$')
#plt.ylim(0,300)
plt.grid()


plt.tight_layout()
plt.savefig("statique fluide_courbe.png")
plt.show()
