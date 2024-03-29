import pytest
import main

def test_class_stack():
    x = main.Stack(size=3)
    assert x.stack == [None, None, None]
    assert x.top == -1

    y = main.Stack(values=[1,2,3], size = 5)
    assert y.stack == [1,2,3, None, None]
    assert y.top == 2

    z = main.Stack(values=[1,2,3], size = 3)
    assert z.stack == [1,2,3]
    assert z.top == 2


def test_class_is_empty():
    x = main.Stack(size=3)
    assert x.is_empty() is True

    y = main.Stack(values=[1,2,3], size=3)
    assert y.is_empty() is False

def test_class_is_full():
    x = main.Stack(size=3)
    assert x.is_full() is False

    y = main.Stack(values=[1, 2, 3], size=3)
    assert y.is_full() is True

    z = main.Stack(values=[1,2,3], size = 5)
    assert z.is_full() is False

def test_class_pop_push():
    x = main.Stack(size=3)
    x.push(2)
    assert x.stack == [2, None, None]
    assert x.top == 0

    x.push(3)
    assert x.stack == [2,3,None]
    assert x.top == 1

    x.push(4)
    assert x.stack == [2,3,4]
    assert x.top == 2

    assert x.push(5) is None

    y = main.Stack(values=[1, 2, 3], size=3)
    assert y.push(4) is None

    z = main.Stack(values=[1,2,3], size = 5)
    z.push(4)
    z.push(5)
    assert z.push(6) is None

def test_class_pop():
    x = main.Stack(size=3)
    assert x.pop() is None
    assert x.top == -1

    y = main.Stack(values=[1, 2, 3], size=3)
    assert y.pop() == 3
    assert y.top == 1

    assert y.pop() == 2
    assert y.top == 0

    assert y.pop() == 1
    assert y.top == -1

def test_class_peek():
    x = main.Stack(size=3)
    assert x.peek() is None

    y = main.Stack(values=[1, 2, 3], size=3)
    assert y.peek() == 3

    y.pop()
    assert y.peek() == 2


def test_create_stack_accepts_single_word():
    assert main.create_stack('text') == ['t', 'e', 'x', 't']


def test_create_stack_accepts_integer():
    assert main.create_stack(12345) == ['1', '2', '3', '4', '5']


def test_peek_stack():
    assert main.peek_stack(['a', 'b', 'c']) == 'c'


def test_recursion_reverse_integer():
    x = [1, 2, 3, 4]
    main.reverse_stack_with_recursion(x)
    assert x == [4, 3, 2, 1]


def test_recursion_reverse_string():
    x = ['a', 'b', 'c', 'd']
    main.reverse_stack_with_recursion(x)
    assert x == ['d', 'c', 'b', 'a']


def test_recursion_reverse_empty():
    x = []
    main.reverse_stack_with_recursion(x)
    assert not x


def test_reverse_individual_1_words():
    assert ''.join(main.reverse_individual_words_in_stack('Test')) == 'tseT'


def test_reverse_individual_2_words():
    assert ''.join(main.reverse_individual_words_in_stack('Hello World')) == 'olleH dlroW'


def test_reverse_individual_3_words():
    assert ''.join(main.reverse_individual_words_in_stack('We love potatoes')) == 'eW evol seotatop'


def test_add_int_to_bottom_of_stack():
    x = [1, 2, 3, 4]
    main.add_to_bottom_of_stack(x, 0)
    assert x == [0, 1, 2, 3, 4]


def test_stock_span():
    price = [10, 4, 5, 90, 120, 80]
    assert main.stock_span_calculator(price) == [1, 1, 2, 4, 5, 1]


def test_stock_span_single_item():
    price = [10]
    assert main.stock_span_calculator(price) == [1]


def test_nearest_smallest_element():
    assert main.find_nearest_smallest_left_element([1, 2, 8]) == 2
    assert main.find_nearest_smallest_left_element([1, 8, 8]) == 1
    assert main.find_nearest_smallest_left_element([1, 9, 8]) == 1
    assert main.find_nearest_smallest_left_element([10]) == 0
    assert main.find_nearest_smallest_left_element([10, 9, 8]) == 0


def test_nearest_smallest_left_element_array():
    assert main.find_nearest_smallest_left_element_array([1, 2, 8]) == [0, 1, 2]
    assert main.find_nearest_smallest_left_element_array([1]) == [0]
    assert main.find_nearest_smallest_left_element_array(
        [2, 4, 8, 7, 7, 9, 3]) == [0, 2, 4, 4, 4, 7, 2]


def test_nearest_smallest_right_element_array():
    assert main.find_nearest_smallest_right_element_array([0, 1, 8]) == [0, 0, 0]
    assert main.find_nearest_smallest_right_element_array([5, 2, 7]) == [2, 0, 0]
    assert main.find_nearest_smallest_right_element_array([1]) == [0]
    assert main.find_nearest_smallest_right_element_array([5, 4, 3]) == [4, 3, 0]
    assert main.find_nearest_smallest_right_element_array(
        [2, 4, 8, 7, 7, 9, 3]) == [0, 3, 7, 3, 3, 3, 0]


def test_find_max_difference():
    assert main.find_maximum_difference_between_nearest_left_and_right_elements([2, 1, 8]) == 1
    assert main.find_maximum_difference_between_nearest_left_and_right_elements(
        [2, 4, 8, 7, 7, 9, 3]) == 4
    assert main.find_maximum_difference_between_nearest_left_and_right_elements(
        [5, 1, 9, 2, 5, 1, 7]) == 1

def test_celebrity_problem_with_celebrity():
    x = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]
    assert main.find_celebrity(x) == 3


def test_celebrity_problem_without_celebrity():
    y = [[0, 0, 1, 0],
         [0, 0, 1, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0]]
    assert main.find_celebrity(y) is None


class TestStackIsEmpty:
    """ Set of tests for testing empty stack"""
    x = []

    def test_empty_stack(self):
        assert main.stack_is_empty(self.x) is True

    def test_pop_empty_stack(self):
        with pytest.raises(IndexError):
            main.pop_stack(self.x)

    def test_peek_empty_stack(self):
        with pytest.raises(IndexError):
            main.peek_stack(self.x)

    def test_push_empty_stack(self):
        item = 'z'
        main.push_stack(self.x, item)
        assert len(self.x) == 1
        assert self.x[0] == 'z'


class TestStackIsText:
    """ Set of tests for testing a stack which has only text elements"""
    x = ['t', 'e', 's', 't']
    item = 'z'

    def test_text_stack_is_empty(self):
        assert main.stack_is_empty(self.x) is False

    def test_push_text_stack(self):
        main.push_stack(self.x, self.item)
        assert len(self.x) == 5
        assert self.x[4] == 'z'

    def test_pop_text_stack(self):
        assert main.pop_stack(self.x) == 'z'
        assert len(self.x) == 4

    def test_reverse_stack_text(self):
        assert main.reverse_stack(self.x) == ['t', 's', 'e', 't']


class TestStackIsInt:
    """ Set of tests for testing a stack which has only integer elements """
    y = [1, 2, 3, 4]

    def test_push_stack_to_stack(self):
        main.push_stack(self.y, 5)
        assert self.y == [1, 2, 3, 4, 5]
        assert len(self.y) == 5

    def test_reverse_stack_int(self):
        assert main.reverse_stack(self.y) == [5, 4, 3, 2, 1]
