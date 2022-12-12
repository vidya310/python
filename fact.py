x=int(input("Enter a value:"))
def fact(x):
    f=1
    if(x==0 or x==1):
        return 1
    for i in range(1,x+1):
        f=f*i;
        i=i+1
    return f
fl=fact(x)
print("factorial=",fl)
