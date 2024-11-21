input=input("enter the sentence:")
input1=input.lower()
dict={ }
for i in input1.split():
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
