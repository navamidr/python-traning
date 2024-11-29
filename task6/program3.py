# Add elements of two lists pairwise using map and a lambda function.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

list1 = [1,2,3]
list2 = [4,5,6]
output=list(map( lambda x,y: [x,y],list1,list2 ))
print(output)