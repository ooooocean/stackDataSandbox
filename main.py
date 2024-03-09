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


# define a function that will be used to recurse and reverse an entire stack
# this function will add an entry to the bottom of a stack
def add_to_bottom_of_stack(stack, item):
    # if the stack is not empty, then we want to pop the entries and add to a temporary
    # stack until the original stack is empty
    if not stack_is_empty(stack):
        # save the first item on the stack and remove it
        temp = pop_stack(stack)
        # call the function again so that we iterate until the stack is empty
        add_to_bottom_of_stack(stack, item)
        push_stack(stack, temp)
    # if the stack is empty, add the element
    else:
        push_stack(stack, item)


def reverse_stack_with_recursion(stack):
    """This needs to take the input as a stack already for the recursion to work."""
    if stack_is_empty(stack):
        return reversed
    else:

        temp_stack = stack
        if stack_is_empty(temp_stack):
            temp_stack
        reverse_stack_with_recursion(stack)


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


def stock_span_calculator(price):
    # this function assumes input is already in stack format.
    # note: I initially tried to solve this with recursion, but realised that the
    # price we want to compare is needed, so I couldn't proceed with that method.
    # recursion methods only work if we don't care about the result of each subprocess.





    # initialise variable to contain the final result of the span
    span = []

    # we want to iterate until the input stack is empty.
    while price:
        # initialise our nth element span variable
        n_span = 1

        # now, pop the price stack and assign it to a variable for comparison.
        n_price = pop_stack(price)

        # we also save the current value of the input stack so that we can call it back
        # once comparisons are finished
        n_stack = price

        # if our nth day price is larger than the previous day's price,
        # we increment our nth span by 1 and pop the stack
        if not stack_is_empty(n_stack) and n_price >= peek_stack(n_stack):
            # however, if the
            n_span += 1
            pop_stack(n_stack)
        # if our nth day price is larger than the previous day's price,
        # then write this span to our span stack and start again with the
        # saved input stack
        else:
            push_stack(span, n_span)
    # once we reach the end of our list, the span stack needs to be reversed
    else:
        return reverse_stack_with_recursion(span,'')

# price =[100, 80, 60, 70, 60, 75, 85]
# print(stock_span_calculator(price))