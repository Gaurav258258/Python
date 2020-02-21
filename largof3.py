a=eval(input("Enter First no.="))
b=eval(input("Enter Second no.="))
c=eval(input("Enter third no.="))

if(a>b):
    if(a>c):
        print (a,"Is largest")
    else:
            print(c,"Is largest")

elif(b>a):
    if(b>c):
        print (b,"Is largest")
    else:
            print (c,"Is largest")

else:
    print (c,"Is largest")                        