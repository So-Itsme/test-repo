num1 = input("ENTER 1st NUMBER\n")
num2 = input("ENTER 2nd NUMBER\n")
num3 = input("ENTER 3rd NUMBER\n")


if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print(largest,"is the largest number")
