# Palindrome Numbers
Computational thinking is a skill you improve with practice, this exercise is one way to sharpen those skills. 

Consider the following definition of palindrome depth, for any number:
>75 is not a palindrome. 
>
>→ so reverse it, and add it to itself: 75 + 57 = 132
>
>132 is also not a palindrome. 
>
>→ so reverse it, and add it to itself: 132 + 231 = 363
>
>363 is a palindrome. 
>So we can call 75 a depth-2 palindrome. 

Using this Scheme for defining palindrome-depth of a given number, **find the palindrome-depth of all two-digit numbers.**

---

The two top-level files represent a solution to this problem that is well defined, with lots of comments and `Pythonic` best-practice. 

The sub-folders represent variations on this solution that achieve different goals. 
- `isolated`: is an example that does not use modules, and focuses on being a relatively short solution (by line-count)
- `most_mini`: is an example that goes for shortest-possible line count, sacrificing readability
- `user_defined`: is a variant where a user is prompted to provide the range of numbers (be warned: somewhere around 190-200 is a number that crashes the program. no promises above 200...)

---

This was written in `Python 3.12.8` but it doesn't do anything fancy: most python versions after 3.5 (where they introduced typing) would work. 