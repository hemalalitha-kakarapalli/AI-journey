#implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
print("What is the Answer to the Great Question of Life, the Universe, and Everything?")
n = input().lower()
if n=="42" :
    print("Yes")
elif n=="forty two"or n== "forty-two":
    print("Yes")
else: 
    print("NO")