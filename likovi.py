class Kruznica(object):
    def __init__(self,r):
        self.radijus = r

    def __str__(self):
        return "kruznica radijusa %.2f" % (self.radijus)

class Kvadrat(object):
    def __init__(self,a):
        self.stranica = a

    def __str__(self):
        return "kvadrat stranice %.2f" % (self.stranica)


kruznica = Kruznica(3)
kvadrat = Kvadrat(4.5)
print(kruznica)
print(kvadrat) 

