a=eval(input("Enter a number:-"))
b,c,sum=0,0,0
b=a
c=a
count=0
while a>0 :
    count=count+1
    a=a//10
#print(count)
while b>0 :
    r = b % 10
    sum= sum + pow(r,count)
    b = b // 10

if c==sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong" )    