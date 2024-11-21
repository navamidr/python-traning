mylist=[4,5,6,7,4,5,8,9,7]
outlist=[]
duplist=[]
for i in mylist:
    if i not in outlist:
        outlist.append(i)
    elif i not in duplist:
        duplist.append(i)
print(duplist)



