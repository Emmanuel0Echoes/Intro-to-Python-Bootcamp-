import functools
def square(number):
    return number * number

def even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def sum(x,y):
    return x + y
#numbers = [1,2,3]
#numberssq = list(map(square, numbers))
#print(numberssq)


#filter
numbers = list(range(1,11))
print(numbers)
evens = list(filter(even, numbers))
print(evens)

#reduce
numbers = list(range(1,11))
sum = functools.reduce(sum, numbers)
print('The sum is of the range is '+ str(sum))