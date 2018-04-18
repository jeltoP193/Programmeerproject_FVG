# -*- coding: utf-8 -*-
import scipy as sc
import numpy as np
import math
from scipy import integrate
import matplotlib.pyplot as plt
from scipy.integrate import odeint

halveMassaStraal = 1+ math.sqrt(2)   

def dichtheid(r):
    return(1 / (2 * math.pi) * 1/(r*((r+1)**3)          ))

def potentiaal(r):
    return(1/(r+1))

def FirstDerivpotentiaal(r):
    return -(    1/  ((r+1)**2)    )

def SecondDerivpotentiaal(r):
    return 2/  ((r+1)**3)    

def massa(r):
    return (r**2)/((1+r)**2)
    
def apsidale_afstanden(E,L):
    coeff = [2*E, 2*E+2, -L**2, -L**2]
    oplossingen = np.roots(coeff)
    geldige_oplossingen = [oplossing for oplossing in oplossingen if np.isreal(oplossing) and oplossing >=0]
    return geldige_oplossingen
        
def omzetten_ongelijke_afstanden(r_apo,r_peri):
    coeff = [1/2 *(1/r_apo**2 - 1/r_peri**2), 0, 1/(r_peri+1) - 1/(r_apo+1)]
    L = np.roots(coeff)[1]
    E = lambda L: -1/(r_apo+1) + (L)**2/(2*r_apo**2)
    return [E(L),L]

def omzetten_gelijke_afstanden(straal):
    L = math.sqrt((straal**3)/((straal+1)**2))
    E = lambda L: -1/(straal+1) + (L)**2/(2*straal**2) #Code duplicatie op lijn 32 mogelijkheid om hulpfunctie te schrijven
    return [E(L),L] 
    
def test_apsidale_afstanden():
    # Allicht later libraries voor unit testen gebruiken
    E = float(input("E:"))
    L = float(input("L:"))
    opl = apsidale_afstanden(E,L)
    print(opl)
    
def radiele_periode(r_apo,r_peri,E,L):
    # Nog geen sanity checks geschreven MOET NOG GEDAAN WORDEN
    integrandum = lambda r: 1/ (math.sqrt(    (2*(E+(1/(r+1))) - ((L**2)/(r**2))       )))
    return sc.integrate.quad(integrandum, r_apo, r_peri)
'''    
if __name__ =="__main__":
    #test_apsidale_afstanden()
    #print(omzetten_ongelijke_afstanden(0.27794281273882032,3.9281392510731887))
    #print(omzetten_gelijke_afstanden(1.205))
    #print(radiele_periode(0.27794281273882032,3.9281392510731887,-0.20000000000000018,0.29999999999999993))

'''
# Integreren vd Rosettebanen:
L = 0.3
E = -0.2
r_apo = 3.9281392510731887
r_peri = 0.27794281273882032

T_r = radiele_periode(r_apo,r_peri,E,L)


def IntegratieR(y, t, L, E):
    r, v, theta = y
    
    if 2*E - (L/r)**2 + 2/(1+r) >= 0:
        print("good")
        dydt = [math.sqrt(2*E - (L/r)**2 + 2/(1+r))  , L**2/(r**3) + 1/((r+1)**2), L/(r**2)]
    else:
        print("Oh crap")
        dydt = [0, L**2/(r**3) + 1/((r+1)**2), L/(r**2)]
    return dydt

y0 = [0.6, 0.0, 0]
t = np.linspace(0, 24, 101)

sol = odeint(IntegratieR, y0, t, args=(L, E))


plt.plot(t, sol[:, 0], 'b', label='r(t)')
plt.plot(t, sol[:, 1], 'g', label='v(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()


# stap 4:

r_max = 19 + 2 * math.sqrt(95)   # Omvat 95% van totale galaxiemassa
stappenlijst = np.linspace(0, r_max, 300)


# stap 5:

massaToenameLijst = []
for i in range(1, len(stappenlijst) ):
    massaToenameLijst.append( massa(stappenlijst[i]) - massa(stappenlijst[i-1]))

print(massaToenameLijst)



'''
Enkele testwaarden
E=-0.2
L=0.3
r_apo = 3.9281392510731887 
r_peri = 0.27794281273882032
E = -0.32959517896349766
L = 0.5998904891637343
r_circ = 1.205
'''

