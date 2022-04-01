first,second=0,1
n = int(input("please give a number for fibonacci series : "))
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num -2)


for i in range(n):
    print(fibonacci(i))