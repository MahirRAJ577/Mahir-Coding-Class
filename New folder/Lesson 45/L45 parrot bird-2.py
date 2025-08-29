class Parrot:
    def __init__(self, nm, h):
        self.name = nm
        self.age = h

    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)
    
blu = Parrot("Blue", 10)

print(blu.sing("'Happy'"))
print(blu.dance())