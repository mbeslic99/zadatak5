from likovi import*
from math import pi

def opseg (lik):
    if isinstance(lik,Kruznica):
        return 2*lik.radijus*pi
    if isinstance(lik,Kvadrat):
        return 4*lik.stranica
def povrsina(lik):
    if isinstance(lik,Kruznica):
        return lik.radijus**2*pi
    if isinstance(lik,Kvadrat):
        return lik.stranica**2

if __name__=="__main__":
    print(opseg.__name__)
    print(povrsina.__name__)

