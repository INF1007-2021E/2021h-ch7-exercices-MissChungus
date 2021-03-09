#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys
sys.path.insert(0, 'E:\Poly shit\Session 2\INF1007\\2021h-ch6-1-exercices-MissChungus')
from exercice import frequence
# TODO: Définissez vos fonction ici
def compute_volume_and_mass(a=5, b=8, c=10, masse_vol=1):
    volume = math.pi*a*b*c*4/3
    mass = volume * masse_vol
    return volume, mass
g = lambda x: max(frequence(x))
print(g("bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"))
if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    mass_vol = compute_volume_and_mass()
    print(mass_vol)
    pass
