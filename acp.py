#write a program to calculate the power of a number using a for loop
number = int(input("Enter a number: "))
power = int(input("Enter the power: "))

result = 1

for i in range(power):
    result = result * number

print("Result:", result)
