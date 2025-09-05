class addThreeNumbers:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def add_them(self):
        result = self.num1 + self.num2 + self.num3

addition = addThreeNumbers(1, 20 ,50)
result = addition.add_them()
print("The sum is:", result)