from stacks import Stack

# converts a decimal number to a number with base up to base 16
def toBase(decimal,base):
    # if base is greater than 16, raise error
    if base >16 or base <=0:
        raise ValueError ('base must be between 1 and 16')
    elif isinstance(decimal,int)==False:
        raise ValueError('the number must be a integer')
    elif decimal==0:
        return str(0)
    
    hex_num = "0123456789ABCDEF"
    
    s = Stack()

    while decimal > 0:
        remainder = decimal % base
        s.push(remainder)
        decimal = decimal // base

    output = ""
    # want to pop all the stack contents out
    while not s.isEmpty():
    #hex_num[s.pop()] would make sure base>10, the alphabet would be used
        output += hex_num[s.pop()]
    
    return output

#testing
# print(toBase(101,2)) # should be 1100101
# print(toBase(101,16)) # should be 65
# print(toBase(188,16)) # should be BC