"""
Playing around with stack data structure, using it to reverse letters.
"""

import copy

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


def reverse_stack(stack):
    # take in stack as input.
    # initialise output variable
    # create a loop that continues until the original stack is empty
    new_stack = []
    while not stack_is_empty(stack):
        new_stack.append(pop_stack(stack))
    return new_stack


# define a function that will be used to recurse and reverse an entire stack
# this function will add an entry to the bottom of a stack
def add_to_bottom_of_stack(stack, item):
    # if the stack is not empty, then we want to pop the entries and add to a temporary
    # stack until the original stack is empty
    if not stack_is_empty(stack):
        # save the top item on the stack and remove it
        temp = pop_stack(stack)
        # call the function again so that we iterate until the stack is empty
        add_to_bottom_of_stack(stack, item)
        # once we break out of the recursion to end the loop,
        # elements will be adding back in, in reverse order
        push_stack(stack, temp)
    # if the stack is empty, add the element
    else:
        push_stack(stack, item)


def reverse_stack_with_recursion(stack):
    """This needs to take the input as a stack already for the recursion to work."""
    # if the stack is not empty
    if not stack_is_empty(stack):
        # pop the input stack
        temp = pop_stack(stack)
        # recurse, which will pop and store all values in memory
        # with the bottom of the stack being most recent in memory
        reverse_stack_with_recursion(stack)
        # we now want to add each element to the bottom of the stack as we
        # exit the recursion
        add_to_bottom_of_stack(stack, temp)


def reverse_individual_words_in_stack(words):
    words_stack = create_stack(words)
    new_words = []
    buffer_stack = []
    # iterate until the stack is empty
    while words_stack:
        # add letters to the new stack from our input
        new_words.append(pop_stack(words_stack))
        # when a space is found, pop the stack to a buffer for later
        if not stack_is_empty(words_stack) and peek_stack(words_stack) == ' ':
            # pop the space from the original stack to retain word order
            # iterate through our new stack until it is empty
            pop_stack(words_stack)
            while new_words:
                # move words to buffer
                buffer_stack += pop_stack(new_words)
                print(f'New words is {new_words}.\n'
                      f'Buffer stack is {buffer_stack}')
            # once input is empty, add a space to the top of the buffer stack to preserve spacing
            else:
                push_stack(buffer_stack, ' ')
        # once words have all been iterated through, add words back in from the buffer
        elif stack_is_empty(words_stack):
            while buffer_stack:
                new_words.append(pop_stack(buffer_stack))
            # once buffer_stack is empty, print the new stack
            else:
                return new_words


# The stock span problem is a financial problem where we have a series of
# N daily price quotes for a stock and we need to calculate the span of the
# stock’s price for all N days. The span Si of the stock’s price on a
# given day i is defined as the maximum number of consecutive days
# just before the given day, for which the price of the stock on the
# current day is less than or equal to its price on the given day.

# define a function that calculates the n day for a given day range, given the input
# is the most recent day
def calc_n_span(price_range, n_day_price):
    n = 1
    while not stack_is_empty(price_range) and n_day_price >= pop_stack(price_range):
        n += 1
    else:
        return n


def stock_span_calculator(price):
    # this function assumes input is already in stack format.
    # note: I initially tried to solve this with recursion, but realised that the
    # price we want to compare is needed, so I couldn't proceed with that method.
    # recursion methods only work if we don't care about the result of each subprocess.

    # initialise variable to contain the final result of the span
    span = []

    # we want to iterate until the input stack is empty.
    while len(price) != 1:
        n_day = pop_stack(price)
        temp_price = copy.deepcopy(price)
        n_span = calc_n_span(temp_price, n_day)
        add_to_bottom_of_stack(span, n_span)
    else:
        add_to_bottom_of_stack(span, 1)
    return span

