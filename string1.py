def abc(word,letter):
	a=0
	for i in range(len(word)):
		if(word[i]==letter):
			a=a+1
	return a
word=input("Enter the word")

print(abc("Gaurav","G"))			
