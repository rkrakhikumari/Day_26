#def find_largest_number(number):
    #return max(number)

#result = find_largest_number([4,3,7,1,9])
#print(result)

def sum_of_squares_of_digits(number):
    # Convert the number to a string to iterate through its digits
    num_str = str(number)

    # Initialize a variable to store the sum of squares
    sum_of_squares = 0

    # Iterate through each digit in the number
    for digit_str in num_str:
        # Convert the digit back to an integer and square it
        digit = int(digit_str)
        square = digit ** 2

        # Add the squared value to the sum
        sum_of_squares += square

    # Return the final sum of squares
    return sum_of_squares

# Example usage:
number = 123
result = sum_of_squares_of_digits(number)
print(f"The sum of squares of digits of {number} is: {result}")
