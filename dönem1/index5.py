#Outer loop for each line
for i in range(8, -1, -1):
    # nner loop for printing numbers
    for j in range(i + 1):
        print(j, end="")
    #New line after each row
    print()
