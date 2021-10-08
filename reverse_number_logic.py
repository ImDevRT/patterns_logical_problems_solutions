number = int(input("Enter a number: "))
rev_number = None

while (number):
    if (rev_number):
        digit = number % 10
        rev_number = (rev_number * 10) + digit
    else:
        digit = number % 10
        rev_number = digit
    number = number // 10

print(f"Reversed number: {rev_number}")
