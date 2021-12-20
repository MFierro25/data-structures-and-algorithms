from stacks_and_queue.stacks import Stack

open_brackets = ['(','[','{']
close_brackets = [')',']','}']    

def validate(string):
    list_1 = []
    list_2 = []
    
    for i in string:
        if i in open_brackets:
            list_1.append(i)
        elif i in close_brackets:
            list_2.append(i)
             
    if set(list_1) == set(list_2):
        return True
    
    else:
        return False