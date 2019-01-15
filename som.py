# som.py: berekent de som van de elementen van een lijst
# auteur: D vd Beek

lijst = [3, 4, 1, 0, 9, 2, 5]
som = 0
for i in range(len(lijst)):
    som = som + lijst[i]
print(som)
