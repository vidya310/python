len=int(input("How many numbers do you want to save?"))
inputvaluelist=[]
for n in range(0,len):
    inputvalue=int(input("Enter a value:"))
    if inputvalue>=100:
        inputvaluelist.append("OVER")
    else:
        inputvaluelist.append(inputvalue)
print(inputvaluelist)        
