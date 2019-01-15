# Bereken het minimaal aantal benodigde muntjes voor een gegeven bedrag
# Auteur: Piet Paaltjes

# input gebruiker
wisselgeld = -1
while wisselgeld < 0:
    wisselgeld = input('Wisselgeld: ')
    wisselgeld = float(wisselgeld)

# conversie naar centen
wisselgeld = round(wisselgeld*100)
munten = 0

# 25 cent
while(wisselgeld >= 25):
    wisselgeld = wisselgeld - 25
    munten = munten + 1

# 10 cent
while(wisselgeld >= 10):
    wisselgeld = wisselgeld - 10
    munten = munten + 1

# 5 cent
while(wisselgeld >= 5):
    wisselgeld = wisselgeld - 5
    munten = munten + 1

# 1 cent
while(wisselgeld >= 1):
    wisselgeld = wisselgeld - 1
    munten = munten + 1

# output
print('Munten: {}'.format(munten))
