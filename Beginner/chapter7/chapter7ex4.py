numerator = 0
denomator = 0
while denomator != -1:
    print("Enter a numerator: ")
    numerator = float(input())
    print("Enter a denomator")
    denomator = float(input())
    if denomator == 0:
        continue
    print(numerator/denomator)