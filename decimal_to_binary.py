from stacks import Stack

# Stack is good for converting decimal to binary using the stack method because it requires poping out the most recent added remainder first
# Most significant bit (MSB) is the top of the stack and Least Significant Bit (LSB) is the bottom of the stack
# This uses the divide by 2 method to convert decimal to binary
# only accepts integer
def toBinary(decimal):
    if (isinstance(decimal,int)==False) or decimal<0:
        raise ValueError('the number must be a positive integer')
    elif decimal==0:
        return str(0)
    
    s = Stack()

    while decimal > 0:
        remainder = decimal % 2
        s.push(remainder)
        decimal = decimal // 2

    output = ""
    # want to pop all the stack contents out
    while not s.isEmpty():
        output += str(s.pop())
    return output

# Testing the toBinary function
# print(toBinary(2)) # should be 10
# print(toBinary(101)) # should be 1100101
# print(toBinary(-2)) # should raise error
# print(toBinary(0)) # should be 0