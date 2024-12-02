# basic closure question
# Write a function make_multiplier(n) that returns another function. The returned function should take a single argument x and return the product of x and n


def make_multiplier(n):
    def product(x):
        return x * n
    return product

output= make_multiplier(6)  
print(output(4))  
