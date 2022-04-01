n= int(input("input number you want factorial off"))


temp = 1

# for data in range(1,n+1):
#     temp = temp*data
#     print(temp)

# print("temp num is:",temp)

#----with recursion--------


def fact(n):  
   print(n)
   if n == 1:  
       return n  
   else:  
#recursion
       return n*fact(n-1)

print("Factorial of",n,"is",fact(n))  
