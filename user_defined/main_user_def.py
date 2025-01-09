# best practice to only import the functions you need from a module
from ud_palindrome import optimized_palindrome_depth

min, max = 0, 0
while True:
    try:
        min = int(input("set bottom of range (must be zero or larger): "))
        if min < 0:
            print("Please enter a non-negative number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")
while True:
    try:
        max = int(input(f"set top of range (must be larger than {min}): "))
        if max < min:
            print(f"Please enter a number larger than {min}.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# create and empty dictionary
all_numbers = {str(i):None for i in range(min,max+1)}

# Fill the dictionary with the palindrome depth of each number
all_numbers = optimized_palindrome_depth(all_numbers)

# Print the dictionary
print(all_numbers)

# Perhaps more readable output
for num in all_numbers:
    print(f"{num}: depth-{all_numbers[num]}")
    