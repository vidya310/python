def longestlength(a):
    max1=len(a[0])
    temp=a[0]
    for i in a:
        if(len(i))>max1:
            max1=len(i)
            temp=i
    print("word with longest length is:",temp,"and length is",max1)
a=["ant","bee","elephant","butterfly","bull"]
longestlength(a)
