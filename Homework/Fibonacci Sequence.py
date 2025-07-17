def fibsequence(n):
    
    a=0
    b=1
   
    if n <= 1:
        print (a)
    
    else:
        print(a)
        print(b)
    
        for i in range(2,n):

            c = a + b
            a=b
            b=c
            print(a+b)

num = int(input("How many numbers would you like in the Fibonacci sequence : "))

fibsequence(num)