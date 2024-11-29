# Write a generator expression to filter out odd numbers from a list and print the result.

list=[3,2,5,4,12,25,38,49,66,37]

odd_num=(num for num in list if num %2 != 0 )
for i in odd_num:
    print(i)