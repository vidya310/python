elem=input("Enter a word:")
vowels=['a','e','i','o','u','A','E','I','O','U']
list1=[]
for x in elem:
    if x in vowels and x not in list1:
        list1.append(x)
print("vowels present in the given word are:",list1)
