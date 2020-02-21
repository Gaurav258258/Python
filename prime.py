a=eval(input("Enter a no:- "))
for i in range(2,a-1):
    if(a%i==0):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("Number is not a prime no.")
else:
    print("Number is prime")