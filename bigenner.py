# find sum of digit in a number
def sum_of_digit(number):
    return sum(int(digit) for digit in str(abs(number)))

result = sum_of_digit(123)
print(result)

