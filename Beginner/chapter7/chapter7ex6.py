#outfile = open('text.txt', 'w')
#outfile.write("Welcome to Zaria \n")
#outfile.write("The place to be \n")
#outfile.close()


outfile = open('grades.txt', 'w')
print("Enter a grade (q) to quit: ")
grade = input()
while (grade != 'q'):
    outfile.write(grade+"\n")
    print("Enter a grade (q) to quit: ")
    grade = input()

outfile.close()