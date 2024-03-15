"""
Playing around with stack data structure, using it to reverse letters.
"""

import copy

class Stack:
    def __init__(self, values=None):
        self.top = -1
        self.stack = values if values else []

    def is_empty(self):
        return True if len(self.stack) == 0 else False
def create_stack(stack):
    """ Creates stack from a string """
    stack = list(str(stack))
    return stack


def peek_stack(stack):
    """ Looks at element from the top of a stack """
    return stack[len(stack) - 1]


def stack_is_empty(stack):
    """ Checks if a stack is empty"""
    return not bool(stack)


def pop_stack(stack):
    """ Removes element from a stack """
    if stack_is_empty(stack):
        print('Stack is empty.')
    return stack.pop()


def push_stack(stack, item):
    """ Adds item to a stack """
    stack.append(item)


def reverse_stack(stack):
    """ Reverses order of items in a stack"""
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
    """ Adds item to the bottom of a stack"""
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
    """ Reverses individual worlds in a string whilst maintaining word order """
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
            push_stack(buffer_stack, ' ')
        # once words have all been iterated through, add words back in from the buffer
        elif stack_is_empty(words_stack):
            while buffer_stack:
                new_words.append(pop_stack(buffer_stack))
            # once buffer_stack is empty, print the new stack
            return new_words


# The stock span problem is a financial problem where we have a series of
# N daily price quotes for a stock and we need to calculate the span of the
# stock’s price for all N days. The span Si of the stock’s price on a
# given day i is defined as the maximum number of consecutive days
# just before the given day, for which the price of the stock on the
# current day is less than or equal to its price on the given day.

# define a function that calculates the n day for a given day range, given the input
# is the most recent day
def calc_n_span(price_range, n_day_index):
    """ Calculates the span of a given day in a given price range """
    n = 1
    while not stack_is_empty(price_range) and n_day_index >= pop_stack(price_range):
        n += 1
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
    add_to_bottom_of_stack(span, 1)
    return span


def find_nearest_smallest_left_element(stack):
    # if the input stack has length 1, then don't continue with the rest of the code
    if len(stack) == 1:
        return 0
    # otherwise, continue with taking the top element of the stack
    comparator = pop_stack(stack)
    # we iterate a loop that is true as long as the next element is greater than
    # the initial value
    while comparator <= peek_stack(stack):
        # if we reach the end of the stack and the stack is still larger, then we
        # return 0 and break the loop
        if len(stack) == 1:
            return 0
        pop_stack(stack)
    # once a smaller number is found, record the smallest element
    return peek_stack(stack)


def find_nearest_smallest_left_element_array(stack):
    # define array to be returned
    result = []

    # push results from defined function into array
    while stack:
        # duplicate stack for feeding into next function
        temp_stack = copy.deepcopy(stack)
        smallest = find_nearest_smallest_left_element(temp_stack)
        pop_stack(stack)
        push_stack(result, smallest)
    # since values are calculated from the top of the stack to the bottom,
    # we need to reverse the stack to obtain the correct values
    return reverse_stack(result)


def find_nearest_smallest_right_element_array(stack):
    # reverse input stack
    temp = reverse_stack(stack)

    # call the left most array function
    array = find_nearest_smallest_left_element_array(temp)

    # reverse the result
    return reverse_stack(array)


def find_maximum_difference_between_nearest_left_and_right_elements(stack):
    # create copy of array for input
    stack_copy = copy.deepcopy(stack)

    # create an array for nearest left elements
    nearest_left_array = find_nearest_smallest_left_element_array(stack)
    # create an array for nearest right elements
    nearest_right_array = find_nearest_smallest_right_element_array(stack_copy)

    # initialise variables to be used in loop
    max_diff = 0

    while nearest_left_array:
        # find differences by popping the stacks
        diff = abs(pop_stack(nearest_left_array) - pop_stack(nearest_right_array))
        # save the largest value
        if diff > max_diff:
            max_diff = diff
    return max_diff

# the celebrity is determined if every value in a slice is equal to 1, other than one.

def find_celebrity(matrix):
    matrix_length = len(matrix)
    # define the slice that we want to compare against.
    comparator = [0]
    for i in range(matrix_length - 1):
        comparator.append(1)

    while matrix[0]:
        # initialise slice for comparison
        matrix_slice = []

        # pop each stack and add to a slice
        for i in range(matrix_length):
            push_stack(matrix_slice, pop_stack(matrix[i]))

        print(matrix_slice)
        # after obtaining the list, sort the list and see if it is equivalent to 1, 1, 1, 0
        if sorted(matrix_slice) == comparator:
            # if a match is made, we want to make sure that the person does not know anybody
            person = matrix[i-1]
            celebrity_check = all(ele == 0 for ele in person)
            # if the person knows no-one, then they are the celebrity
            if not celebrity_check:
                pass
            else:
                print(f'Person {i} is the celebrity')
                return i
        # otherwise, loop continues with the smaller people stacks
    # if no match is found, then throw error
    print('Nobody is a celebrity.')
    return None
