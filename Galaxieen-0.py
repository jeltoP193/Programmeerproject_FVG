# -*- coding: utf-8 -*-
import scipy
import numpy
import math
from scipy import integrate

# stap 1:
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
halveMassaStraal = 1+ math.sqrt(2)    




# Stap 2:


# 2a) Stel E,L gegeven:
L = 3    # plug in L
E = 2    # plug in E

radiusSolutions = numpy.roots([2*E, 2*E-2, -L**2, -L**2])
realsolutions =[]

for i in range(len(radiusSolutions)):
    if numpy.isreal.radiusSolutions[i]:
        realsolutions.append(radiusSolutions[i])
        
r_p = min(realsolutions)
r_a = max(realsolutions)





# 2b) Stel r_a, r_p gegeven:
r_a = 1 # plug in value for r_a
r_p = 0.3 # plug in value for r_p
r = r_a


LSolutions = numpy.roots([(r**2)-1, 0, 2*(r**2)*(   ((r**2)/(1+r)) + (r/(1+r)) -1             ) ])



# 2c) Integreren voor T_r
integrandum = lambda r: 2/ (math.sqrt(    (2*(E-(1/(r+1))) - ((L**2)/(r**2))       )))
T_rad = integrate.quad(integrandum, r_p, r_a)






















