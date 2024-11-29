# Write a generator function to yield squares of numbers from 1 to n.


n=int(input("enter the number:"))
def squares(n):
    for i in range(1,n+1):
        yield i*i

for i in squares(n):
    print(i)