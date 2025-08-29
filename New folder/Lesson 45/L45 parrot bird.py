class Parrot:
    species = "bird"

    def __init__(self, nm, h):
        self.name = nm
        self.age = h

blue = Parrot("Blue", 10)
jell = Parrot("Jelly", 15)

print("Blue is a ", blue.species)
print("Jelly is also a ", jell.species)
print()

print(f"{blue.name} is {blue.age} years old")
print(f"{jell.name} is {jell.age} years old")