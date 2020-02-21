a=eval(input("Enter a number:-"))
b=0
a=b
rev=0
while a>0 :
    r= a% 10
    rev=rev*10+r
    a=a//10

if b==rev:
    print("No is palindrom")
else:
    print("No is not palindrom")