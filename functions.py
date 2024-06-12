'''Can you create a program to add and multiply two numbers? For this, create two functions
add_numbers() and multiply_numbers(). These functions should compute the result and return them to
the function call. And, the results should be printed from outside the function.'''
def add_numbers(num1,num2):
    addition=num1+num2
    return addition
def multiply_numbers(num1,num2):
    multiply=num1*num2
    return multiply
addition=add_numbers(2,3)
print("the sum is:",addition)
multiply=multiply_numbers(2,3)
print("the multiply is:",multiply)