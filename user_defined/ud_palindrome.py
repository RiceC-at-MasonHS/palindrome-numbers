from time import perf_counter
import sys

# Increase the limit for integer string conversion
sys.set_int_max_str_digits(100000)

# This file is a Python 'Module' 
# read more: https://docs.python.org/3/tutorial/modules.html 

# worth looking up how to reverse a string in Python:
# https://www.w3schools.com/python/python_howto_reverse_string.asp
# this process makes heavy use of string slicing (which we covered): 
# https://www.w3schools.com/python/gloss_python_string_slice.asp

def is_palindrome(num: str) -> bool:
    """
    Given a number as a string, return True if it is a palindrome.
    """
    return num == num[::-1]

def depth_step(num: str) -> str:
    """
    Advance the number one step towards a palindrome.
    Return the new number as a string.
    """
    return str(int(num) + int(num[::-1]))

# Only function used outside of this module
def palindrome_depth(num: str) -> int:
    """
    Given a number, return the number of steps it takes to reach a palindrome.
    Handles the case where the number is already a palindrome.
    """
    counter = 0
    while not is_palindrome(num):
        num = depth_step(num)
        counter += 1
    return counter

def optimized_palindrome_depth(all_nums: dict) -> dict:
    """
    Given a dictionary of numbers, return a dictionary of palindrome depths.
    """
    how_many_steps_saved = 0
    start = perf_counter()
    for num in all_nums:
        # optimization - skip numbers already processed
        if all_nums[num] is not None:
            if __name__ == "__main__":
                how_many_steps_saved += 1
                print(f"skipping {num}")
            continue
        counter = 0
        this_num = num # operate on equivalent, not original
        while this_num != this_num[::-1]:
            counter += 1
            this_num = str(int(this_num) + int(this_num[::-1]))
        all_nums[num] = counter
        # optimization - string-reversed numbers are equal depth
        if num[::-1] in all_nums:
            all_nums[num[::-1]] = counter
    if __name__ == "__main__":
        print(f"optimized_palindrome_depth saved {how_many_steps_saved} operations")
    return all_nums

def performance_wrapper( func, *args, **kwargs):
    """
    Wrapper function to measure the performance of a function.
    """
    start = perf_counter()
    result = func(*args, **kwargs)
    print(f"{func.__name__} took {perf_counter()-start} seconds")
    return result

#------------------------------------------------------------------------------
# Test the functions defined in this file
# --> This code will only run if this file is executed directly
# --> It will not run if this file is imported as a module
if __name__ == "__main__":
    print(f"66 is a palindrome? {is_palindrome('66')}")
    print(f"35 is a palindrome? {is_palindrome('35')}")
    print(f"121 is a palindrome? {is_palindrome('121')}")

    print(f"\n10 after 1 depth_step: {depth_step('10')}")
    print(f"35 after 1 depth_step: {depth_step('35')}")
    print(f"233 after 1 depth_step: {depth_step('233')}")

    print(f"\n11 has a palindrome depth of {palindrome_depth('11')}")
    print(f"10 has a palindrome depth of {palindrome_depth('10')}")
    print(f"28 has a palindrome depth of {palindrome_depth('28')}")

    print("\nTesting optimized_palindrome_depth for numbers 10-99")
    print(optimized_palindrome_depth({str(i):None for i in range(10,100)}))