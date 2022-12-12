x=int(input("enter the limit:"))
count=0
sum=0
lst=[]
while(count<x):
    a=int(input("Enter the value:"))
    lst.append(a)
    count=count+1
print("The given list is:",lst)
for i in  lst:
    sum=sum+i
print("sum of items in the given list=",sum)
