# Print een aantal puntjes boven elkaar
# User input: Hoogte (tussen 1 en 24)

i = input('Hoogte: ')
x =int(i)
while(x<1 or x> 24):
    i = input('Hoogte: ')
    x =int(i)

for i in range(x):
        print('.')
