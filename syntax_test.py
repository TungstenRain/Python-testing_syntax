"""
    This module contains code from
    Think Python, 2nd Edition
    by Allen Downey
    http://thinkpython2.com

    This is to try out syntax errors and determine how the interpreter will handle them
    
    Note: Although this is saved in a .py file, code was run on an interpreter to get results
    Note: Using Python 3.8.5
"""

# Using the print function normally
>>> print("Hello")
"""
 Hello
"""

# Print function without quotation marks
>>> print(Hello)
"""
 Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
 NameError: name 'hello' is not defined
"""

# Print function without closing parenthesis
>>> print("Hello"
"""
...
# Note: Command line is waiting for more code to complete the print function.
"""

# Print function without closing quotation marks
>>> print("Hello)
"""
File "<stdin>", line 1
    print("Hello)
                ^
SyntaxError: EOL while scanning string literal
"""

# Print function without parentheses. Note: Using Python 3.8.5
>>> print"Hello"
"""
File "<stdin>", line 1
    print"Hello"
         ^
SyntaxError: invalid syntax
"""

# Print function without opening parenthesis
>>> print"Hello")
"""
 File "<stdin>", line 1
     print"Hello")
          ^
 SyntaxError: invalid syntax
"""

# Mathematical operation of 8 minus negative 8
>>> 8--8
"""
 16
"""

# Mathematical operation of 8 plus positive 8
>>> 8++8
"""
 16
"""

# Mathematical operation of 8 plus negative 10
>>> 8+-10
"""
 -2
"""

# Using 0 at the beginning of an integer
>>> 03
"""
  File "<stdin>", line 1
   03
    ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
"""

# Using 0 at the beginning of an integer in a mathematical operation
>>> 03+10
"""
  File "<stdin>", line 1
    03+10
     ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
"""

# Using 0 at the beginning of an integer in a mathematical operation
>>> 7+06
"""
  File "<stdin>", line 1
    7+06
       ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
"""

# Storing a variable to a variable beginning with a mumber
>>> 42 = n
"""
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
"""

# Storing a number into multiple variables
>>> x = y = 1
"""
>>> print(x)
1
>>> print(y)
1
"""

# Ending a line with a semi-colon
>>> x = 42;
"""
>>> print(x)
42
"""

# Adding a period to the end of a mathematical statement
>>> x = 42.
"""
>>> print(x)
42.0

Note: The integer is converted to a float
"""

# Mathematical notation without the multiplication symbol. In mathematics, xy is the same as x * y
>>> x = 6
>>> y = 10
>>> z = xy
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'xy' is not defined
"""