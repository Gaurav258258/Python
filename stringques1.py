# write the function say replace vovels with in bracit word
# remove all the vowles and return remmaning word
def rem_vowel(string): 
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string.lower(): 
        if x in vowels: 
            string = string.replace(x, "") 
              
    
    print(string) 
  

string = "welcome to python"
rem_vowel(string)