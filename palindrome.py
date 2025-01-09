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

#------------------------------------------------------------------------------
# Test the functions defined in this file
# --> This code will only run if this file is executed directly
# --> It will not run if this file is imported as a module
if __name__ == "__main__":
    print(f"66 is a palindrome? {is_palindrome('66')}")
    print(f"35 is a palindrome? {is_palindrome('35')}")
    print(f"121 is a palindrome? {is_palindrome('121')}")
    print("\n")
    print(f"10 after 1 depth_step: {depth_step('10')}")
    print(f"35 after 1 depth_step: {depth_step('35')}")
    print(f"233 after 1 depth_step: {depth_step('233')}")
    print("\n")
    print(f"11 has a palindrome depth of {palindrome_depth('11')}")
    print(f"10 has a palindrome depth of {palindrome_depth('10')}")
    print(f"28 has a palindrome depth of {palindrome_depth('28')}")