import main
import pytest


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
    assert x == []


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


class TestStackIsEmpty:
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
    y = [1, 2, 3, 4]

    def test_push_stack_to_stack(self):
        main.push_stack(self.y, 5)
        assert self.y == [1, 2, 3, 4, 5]
        assert len(self.y) == 5

    def test_reverse_stack_int(self):
        assert main.reverse_stack(self.y) == [5, 4, 3, 2, 1]
