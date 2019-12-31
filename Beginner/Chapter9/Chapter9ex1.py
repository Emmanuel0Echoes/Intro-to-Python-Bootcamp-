numbers = [1,2,3,4]
it = iter(numbers)
#print(it.__next__())

#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))

fileIt = open('grades.txt', 'r')
print(next(fileIt), end='')