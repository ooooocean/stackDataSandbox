"""
Playing around with stack data structure, using it to reverse letters.
"""


def create_stack(stack):
    stack = [x for x in str(stack)]
    return stack


def peek_stack(stack):
    return stack[len(stack) - 1]


def stack_is_empty(stack):
    if not stack:
        return True
    else:
        return False


def pop_stack(stack):
    if stack_is_empty(stack):
        print('Stack is empty.')
    return stack.pop()


def push_stack(stack, item):
    stack.append(item)
    print(f'Pushed item: {item}')


def reverse_stack(input):
    stack = create_stack(input)
    new_word = ''
    while stack_is_empty(stack) is False:
        new_word += pop_stack(stack)
    print(f'"{input}" was reversed to "{new_word}"')
    return new_word


def reverse_stack_with_recursion(stack, string):
    """This needs to take the input as a stack already for the recursion to work."""
    if not stack:
        print(string)
        return (string)
    else:
        string += pop_stack(stack)
        reverse_stack_with_recursion(stack, string)


def reverse_individual_words_in_stack(words):
    words_stack = create_stack(words)
    new_words = []
    buffer_stack = []
    # iterate until the stack is empty
    while words_stack:
        # add letters to the new stack from our input
        print(f'Original Stack is {words_stack}')
        new_words.append(pop_stack(words_stack))
        print(f'New stack is {new_words}\n'
              f'Original stack is now {words_stack}.\n')
        # when a space is found, pop the stack to a buffer for later
        if not stack_is_empty(words_stack) and peek_stack(words_stack) == ' ':
            # pop the space from the original stack to retain word order
            # iterate through our new stack until it is empty
            print('Space found.')
            pop_stack(words_stack)
            print(f'Removed space from new words stack. It is now {words_stack}')
            while new_words:
                # move words to buffer
                buffer_stack += pop_stack(new_words)
                print(f'New words is {new_words}.\n'
                      f'Buffer stack is {buffer_stack}')
            # once input is empty, add a space to the top of the buffer stack to preserve spacing
            else:
                push_stack(buffer_stack, ' ')
                print(f'Added space. Buffer stack is {buffer_stack}')
        # once words have all been iterated through, add words back in from the buffer
        elif stack_is_empty(words_stack):
            print(f'Original list is empty - {words_stack}')
            while buffer_stack:
                new_words.append(pop_stack(buffer_stack))
                print(f'New words is now {new_words}')
            # once buffer_stack is empty, print the new stack
            else:
                return new_words


