def is_armstrong(num):
    digits = str(num)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == num 

num = int(input("Enter number here: "))

if is_armstrong(num):
    print("{num} is an armstrong number.")

else:
    print("{num} is not an armstrong number.")