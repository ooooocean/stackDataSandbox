"""
Playing around with stack data structure, using it to reverse letters.
"""


def create_text_stack(stack):
    stack=[x for x in stack]
    return stack

def stack_is_empty(stack):
    if stack == []:
        return True
    else:
        return False

test = 'text'
print(create_text_stack(test))