#continue returns to loop
#break returns outside loop

number = 0
total = 0
average = 0
count = 0
while True:
    print("Enter a number: ")
    number = float(input())
    if number == -1:
        break
    total = total + number
    count = count + 1
average = total/count
print("Average: " + str(average))