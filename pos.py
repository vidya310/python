li=[]
n=int(input("Enter the size of list:"))
for i in range(0,n):
     e=int(input("Enter the elements in the list:"))
     li.append(e)
print("Positive numbers in the given list are:")
for i in li:
    if i>0:
        print(i,end=",")
