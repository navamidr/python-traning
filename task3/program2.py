f=open("source.txt","w")
f.write("Hello! This is source file.")


f = open("source.txt", "r")
data=f.read()
print(data)

f2=open("destination.txt","w")
for file in data:
    f2.write(file)
f.close()
f2.close() 


# another method


