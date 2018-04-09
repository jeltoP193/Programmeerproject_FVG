import scipy
import numpy
import math


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




