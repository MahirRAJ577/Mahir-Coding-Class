class Robot:
    def __init__(self, nm, m):
        self.name = nm
        self.model = m

PythonAi = Robot("PythonAi", 6)

print("Hello there!")
print(f"My name is {PythonAi.name} and I am model {PythonAi.model}")