#Q2 Write a Python program to print a dictionary whose keys should be the alphabet from a-z 
#and the value should be corresponding ASCII values


a = {}
 

for i in range(97, 97 + 26):
    # Map character to ascii value
    a[chr(i)] = i
 
print(a)


#ASCII stands for American Standard Code for Information Interchange.
#It is a numeric value given to different characters and symbols, for computers to store and manipulate. 
# For example, the ASCII value of the letter 'A' is 65.
#A Dictionary in Python is the unordered and changeable collection of data values that holds key-value pairs. 
#Each key-value pair in the dictionary maps the key to its associated value making it more optimized.
#A Dictionary in python is declared by enclosing a comma-separated list of key-value pairs using ' curly braces({}) '.
# Python Dictionary is classified into two elements: Keys and Values.
#More than one entry per key is not allowed ( no duplicate key is allowed)
#The values in the dictionary can be of any type, while the keys must be immutable like numbers, tuples, or strings.
#Dictionary keys are case sensitive ,