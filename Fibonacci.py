num=int(input("Enter the number of terms you need:"))
n,m=0,1
count=0
if num<=0:
  print("Please enter Positive number")
elif num==1:
  print("Fibonacci series upto",num,":")
  print(n)
else:
  print("Fibonacci Series:")
  while count<num:
    print(n)
    a=n+m
    n=m
    m=a
    count+=1
