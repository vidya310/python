list1=[10,11,12,13,14,15,16,17,18,19,20]
list2=[]
print("The given list is:",list1)
for i in list1:
    if(i%2!=0):
        list2.append(i)
print("The new list after removing even numbers is:",list2)        
