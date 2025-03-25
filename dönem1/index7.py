def main():
    # Get a list of 10 integers from the user
    numbers = [int(input(f"Enter integer {i + 1}: ")) for i in range(10)]

    # Get a number 'n' from the user
    n = int(input("Enter the number you wish to test if the list elements are greater than: "))

    # Display the original list of numbers
    print("List of numbers:")
    print(numbers)

    # Filter and display numbers greater than 'n'
    filtered_numbers = [num for num in numbers if num > n]
    print(f"List of numbers that are larger than {n}:")
    print(filtered_numbers)

if __name__ == "__main__":
    main()
