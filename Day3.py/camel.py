x = input("enter camelCase string: ")#hemaLalitha
i=0
for letter in x:
    if x[i].isupper():
     print("_"+x[i].lower(),end="")
    else:
        print(letter,end="")
    i=i+1