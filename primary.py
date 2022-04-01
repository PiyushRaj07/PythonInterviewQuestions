i,temp=0,0
n = int(input("please give a number : "))
print("n",n//2)
for i in range(2,n//2):
    print("i is",i)
    print("i",n%i)
    if n%i == 0:
        temp=1
        break
if temp == 1:
    print("given number is not prime")
else:
    print("given number is prime")