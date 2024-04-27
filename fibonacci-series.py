#fibonacci example
# 0+1=1
# 	1+2=3
# 	   2+3=5
# 		  3+5=8	
# 			5+8=13

first,second=0,1
n = int(input("please give a number for fibonacci series : "))
print("fibonacci series are : ")
for i in range(0,n):
    if i<=1:
        print("i",i)
        result=i
    else:
      result = first + second
      first = second
      second = result
    print(result)
