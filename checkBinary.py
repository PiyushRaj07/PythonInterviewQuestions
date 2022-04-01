num = int(input("please give a number : "))
while(num>0):
    j=num%10
    print("2 // meas",num//10)

    print("j",j)
    if j!=0 and j!=1:
        print("num is not binary")
        break

    num=num//10
    if num==0:
        print("num is binary")