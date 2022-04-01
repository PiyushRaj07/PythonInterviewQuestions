str = input("please enter a string : ")
ch = input("please enter a character : ")
print(str.replace(ch," ")) 


string = input("Please enter String : ")
char = input("Please enter a Character : ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print("Total Number of occurence of ", char, "is :" , count)
 

# str1 == str2
 def anagramCheck(str1, str2):
    if (sorted(str1) == sorted(str2)) :  
	    return True 
    else :  
	    return False 
    
str1 = input("Please enter String 1 : ")
str2 = input("Please enter String 2 : ")
if anagramCheck(str1,str2):
    print("Anagram")
else:
    print("Not an anagram")
 