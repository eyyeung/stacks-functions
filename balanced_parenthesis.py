from stacks import Stack

def parenthesisChecker(parString):
    s = Stack()
    for sym in parString:
        # if it is a open parenthesis, push in
        if sym in "([{":
            s.push(sym)
        elif sym in ")]}":
            # if it is a close parenthesis but the stack is empty, return false
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                # the close parenthesis needs to match, if not match, return false
                if not parenthesisMatches(top, sym):
                    return False
    # if everything goes well and did not return False early then the parString is fine and return True    
    return True

def parenthesisMatches(open,close):
    openings ="([{"
    closings = ")]}"
    # should return True or False
    return openings.index(open) == closings.index(close)

#Testing the parenthesisMatches
# print(parenthesisMatches('{','}')) #should be true
# print(parenthesisMatches('{',']')) #shoudl be false

#Testing the parenthesisChecker
# print(parenthesisChecker('{[([][])]()}')) # should be true
# print(parenthesisChecker('[{()]')) # shoudl be false
# print(parenthesisChecker("[{(abc)}]")) # should ignore the abc and return true
