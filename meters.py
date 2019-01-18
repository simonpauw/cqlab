# Converteer imperial (feet en inches) naar metriek (meters)

# input foot
foot = None
while foot == None:
    inp = input('Foot: ')
    if inp.isdigit():
        foot = int(inp)

# input inch
inch = None
while inch == None:
    inp = input('Inch: ')
    if inp.isdigit():
        inch = int(inp)

# definieer conversiefunctie
def imperiaal_naar_metriek(foot, inch):
    meter = foot * 0.3048 + inch * 0.0254
    print(meter)

# voer conversie uit
imperiaal_naar_metriek(foot, inch)
