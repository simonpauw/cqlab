## fahrenheit.py: Converteer een Temperatuur van Fahrenheit naar Celcius
## Auteur: Lord W. T. Kelvin

while True:
    F = input('Temperatuur in Fahranheit (or just press enter to quit): ')
    if F == '':
        break
    F = float(F)
    C = (F - 32) * 5 / 9
    print('Temperatuur in Celcius: {:.1f}'.format(C))
