# our own functions
def main():
    name = input("What is your name? ")
    hello(name)

    # keyword return to return a value
    return name

# def key words for making functions
# def function_name(arguments):
# : indeted code part of this
def hello(name , to = "World"):
    print("Hello ,", name , to)

returned = main() # call the function main()
print("Returned: ", returned)

