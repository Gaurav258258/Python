a=eval(input("Enter a number"))
sum=0
while a>0 :
    r= a%10
    sum = sum + r
    a = a//10

print(sum)