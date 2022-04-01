n = int(input())

pallindrome = 0
reverse = 0

while n!=0:
    pallindrome = pallindrome*10 + n%10
    n = n//10

print("pallindrome",pallindrome)

if pallindrome == n:
    print("its a pallindrome")
else:
    print("its not  a pallindrome")

