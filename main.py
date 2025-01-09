# best practice to only import the functions you need from a module
from palindrome import palindrome_depth

# create and empty dictionary
all_numbers = {str(i):None for i in range(10,100)}

# Fill the dictionary with the palindrome depth of each number
for num in all_numbers:
    all_numbers[num] = palindrome_depth(num)

# Print the dictionary
print(all_numbers)

# Perhaps more readable (duplicate) output
for num in all_numbers:
    print(f"{num}: depth-{all_numbers[num]}")
    