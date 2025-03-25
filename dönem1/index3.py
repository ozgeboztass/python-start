def is_palindrome(number):
    return str(number) == str(number)[::-1]

# User input would be taken here in an interactive Python environment
number_to_test = int(input("Enter a three-digit integer: "))
palindrome_result = is_palindrome(number_to_test)

print(f"The number {number_to_test} is a palindrome: {palindrome_result}")

