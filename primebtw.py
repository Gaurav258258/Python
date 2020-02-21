def prime():
	flag=0
	for a in range(100,300+1):
		for i in range(2,a-1):
			if(a%i==0):
				flag=1
				break
        else:
        	flag=0
if(flag==0):
   	print(a)
prime()    