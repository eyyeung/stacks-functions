# Stacks
## Description
Stacks implemented as a class written in Python and some uses of the Stack class
## Content
* stacks.py : contains the Stack class
* balanced_parenthesis.py : contains functions to check if a string of parenthesis has balanced parenthesis, only accepts {} , () , []
    * parenthesisMatches(open,close) : function to check whether the opening parenthesis and the closing parenthesis match
    * parenthesisChecker(parString) : function to check if the string of parenthesis has balanced parenthesis
* decimal_to_binary.py : contains a function to convert decimal integer to binary
    * toBinary(decimal) : only accepts positive integer or 0, converts decimal integer to binary
* decimal_to_any_base.py: contains a function to convert decimal integer to base up to 16 (hex)
    * toBase(decimal,base) : only accepts postiive integer or 0 along with a base up to 16
## Testing
* Stack :
```python
testStack = Stack()
testStack.push("a")
testStack.push("b")
testStack.push("c")
testStack.push("d")

print("Stack Size: ", testStack.size()) # should be 4
print("Top Item of the Stack: ", testStack.top()) # should be d
print("Popping out one element: ", testStack.pop())# should pop out d
print("Stack Size: ",testStack.size()) # should be 3
```

* parenthesisMatches(open,close) :
```python
print(parenthesisMatches('{','}')) #should be true
print(parenthesisMatches('{',']')) #shoudl be false
```

* parenthesisChecker(parString) :
```python
print(parenthesisChecker('{[([][])]()}')) # should be true
print(parenthesisChecker('[{()]')) # shoudl be false
print(parenthesisChecker("[{(abc)}]")) # should ignore the abc and return true
```

* toBinary(decimal) :
```python
print(toBinary(2)) # should be 10
print(toBinary(101)) # should be 1100101
print(toBinary(-2)) # should raise error
print(toBinary(0)) # should be 0
```

* toBase(decimal,base):
```python
print(toBase(101,2)) # should be 1100101
print(toBase(101,16)) # should be 65
print(toBase(188,16)) # should be BC
```