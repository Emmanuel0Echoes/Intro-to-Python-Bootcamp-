def square(number):
    return number * number

num = 2
sqnum = square(num)
sqnumber = square
sqnum = sqnumber(2)
print(sqnum)

#map higher-order functions
numbers = [1,2,3,4,5]
numberssq = list(map(square, numbers))
print(numberssq)