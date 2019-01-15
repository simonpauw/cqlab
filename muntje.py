# Dit programma gooit herhaaldelijk met een muntje tot er 1000 keer kop is gegooid.
# Auteur: Jacob Bernoulli

import random
import math

kop = 0
munt = 0
worpen = 0
ratio = 0

while kop < 1000:
    # afspraak:
    #    0 <= x < 0.5 -> kop
    #    0.5 <= x < 1 -> munt
    x = random.random()
    if  x < 0.5:
        kop = kop + 1
        worpen = worpen + 1
        ratio = kop/worpen
    else:
        munt = munt + 1
        worpen = worpen + 1
        ratio = kop/worpen

print('Aantal muntworpen: {}, aantal keer kop: {}, aantal keer munt: {}, ratio kop: {}'.format(worpen, kop, munt, ratio))
