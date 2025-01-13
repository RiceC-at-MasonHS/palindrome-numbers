# best practice to only import the functions you need from a module
from ud_palindrome import optimized_palindrome_depth, performance_wrapper
from ud_output import print_dict_raw, print_dict_simple, print_dict_sorted_keys, print_dict_sorted_values

#generate default values
min, max = 0, 10

#ask user for range of numbers
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

#ask user if they want to measure performance
while True:
    measure_performance = input("Do you want to measure performance? (y/n): ")
    if measure_performance.lower() == 'y':
        # same operation, but with performance measurement
        all_numbers = performance_wrapper(optimized_palindrome_depth, all_numbers)
        break
    elif measure_performance.lower() == 'n':
        # Fill the dictionary with the palindrome depth of each number
        all_numbers = optimized_palindrome_depth(all_numbers)
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# ask the user if they would like output as a raw dictionary, unsorted, sorted by keys, or sorted by values
while True:
    output_type = input("How would you like the output sorted? (raw, unsorted, keys, values): ")
    if output_type in ['raw', 'unsorted', 'keys', 'values']:
        if output_type == 'raw':
            print_dict_raw(all_numbers)
        elif output_type == 'unsorted':
            print_dict_simple(all_numbers)
        elif output_type == 'keys':
            print_dict_sorted_keys(all_numbers)
        elif output_type == 'values':
            print_dict_sorted_values(all_numbers)
        break
    else:
        print("Invalid input. Please enter 'raw', 'unsorted', 'keys', or 'values'.")
