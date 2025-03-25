def calculate_discount(number_of_packages):
    package_price = 99  # Retail price per package
    discount_rate = 0   # Default discount rate

    # Determine discount rate based on the number of packages
    if 10 <= number_of_packages < 20:
        discount_rate = 0.10  # 10% discount
    elif 20 <= number_of_packages < 50:
        discount_rate = 0.20  # 20% discount
    elif 50 <= number_of_packages < 100:
        discount_rate = 0.30  # 30% discount
    elif number_of_packages >= 100:
        discount_rate = 0.40  # 40% discount

    # Calculate discount and total amount
    discount_amount = package_price * number_of_packages * discount_rate
    total_amount = package_price * number_of_packages - discount_amount

    return discount_amount, total_amount

# User input would be taken here in an interactive Python environment
number_of_packages = int(input("Enter the number of packages purchased: "))
discount, total = calculate_discount(number_of_packages)

print(f"Discount amount: ${discount:,.2f}")
print(f"Total purchase amount after discount: ${total:,.2f}")
