n= eval(input("enter the no:- "))
a=-1
b=1
for x in range(1,n+1):
        c=a+b                           
        #print(next,end=" ")
        a=b
        b=c
        #sum=sum+next
        print(c,end=" ")