from stacks_and_queue.stacks import Stack

def validate(string):
    list = []
    
    for bracket in string:
        if bracket in '[' and ']' or '{' and '}' or '(' and ')':
            list.append(string)
            return True
        else:
            return False