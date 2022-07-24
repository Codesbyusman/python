# comments by the # symbol

# taking the input from the user
from tracemalloc import start
from turtle import begin_fill


name = input("What is your name : " )

"""
multiline comment

"""
# printing the output
print("hello ," , name) # single line

# printing the output multiple lines
print("hello , " , end = "") # removing the default end='\n'
print(name)


print("hello ," , name, sep = " ::: i am sep ::: " ) # removing the default sep(separator to -)


# using the curly braces to print the output the name
# the format strings
print(f"hello , {name} " )


# strings data type power
name = name.strip() # removing the spaces from the start and end of the string
print(name)


