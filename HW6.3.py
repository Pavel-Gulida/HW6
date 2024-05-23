
number = input("Enter a number: ")

result = int(number)
while result > 9:
    number = str(result)
    result = 1
    for num in number:
        result *= int(num)

print(result)
