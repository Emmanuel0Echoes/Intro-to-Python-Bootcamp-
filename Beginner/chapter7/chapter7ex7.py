#infile = open('text.txt', 'r')
#line = infile.readline()
#print(line)
#line = infile.readline()
#print(line)

count = 0
total = 0
infile = open('grades.txt', 'r')
grades = infile.readline()
while(grades):
    print(grades)
    count = count+1
    total = total+int(grades)
    grades = infile.readline()
average = total/count
print("Average: " + str(average))
