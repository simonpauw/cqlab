# Dit programma berekent het gemiddelde en de standaarddeviatie
# van data. Vervolgens wordt de data genormaliseerd.
# Auteur: Jaap Visser

import math

data = [0.1, 1.3, 5.6, 3.1, 2.2, -3.0]

# bereken gemiddelde
som = 0
for i in range(len(data)):
    som += data[i]
gem = som / len(data)

# bereken standaarddeviatie
som_d = 0
for e in data:
    som_d += (e-gem)**2
stdev = math.sqrt(som_d / len(data))

# normaliseer data
data_norm = []
for x in data:
    data_norm.append((x - gem)/stdev)

# print
print('Gemiddelde: {}'.format(gem))
print('Standaarddeviatie: {:.2f}'.format(stdev))
print('Genormaliseerde data: {}'.format(data_norm))
