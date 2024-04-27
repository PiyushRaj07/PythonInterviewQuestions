example of factorial= n! = (n - 1)! × n
FACTORIAL	MULTIPLICATION	RESULT
0!	1	1
1!	1	1
2!	1 × 2	2
3!	1 × 2 × 3	6
4!	1 × 2 × 3 × 4	24
5!	1 × 2 × 3 × 4 × 5	120
6!	1 × 2 × 3 × 4 × 5 × 6	720
7!	1 × 2 × 3 × 4 × 5 × 6 × 7	5040
8!	1 × 2 × 3 × 4 × 5 × 6 × 7 × 8	40,320
9!	1 × 2 × 3 × 4 × 5 × 6 × 7 × 8 × 9	362,880

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
