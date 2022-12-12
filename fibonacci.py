x=int(input("Enter the limit:"))
def fibon(x):
    n1=0
    n2=1
    count=0
    print("The series is:")
    if(x==0):
        print(n1)
    elif(x==1):
        print(n1)
        print(n2)
    else:
        print(n1)
        print(n2)
        while(count<x-2):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3
            count=count+1
fibon(x)
