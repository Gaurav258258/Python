def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
for i in range(1,11):
    n=eval(input("Enter the number : "))
    j=factorial(n)
    print("Factorial is : ",j)