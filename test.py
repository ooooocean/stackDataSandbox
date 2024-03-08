import main
import pytest


def test_create_stack_accepts_single_word():
    assert main.create_stack('text') == ['t', 'e', 'x', 't']


def test_create_stack_accepts_integer():
    assert main.create_stack(12345) == ['1', '2', '3', '4', '5']

def test_peek_stack():
    assert main.peek_stack(['a','b','c']) == 'c'


def test_reverse_individual_1_words():
    assert ''.join(main.reverse_individual_words_in_stack('Test')) == 'tseT'

def test_reverse_individual_2_words():
    assert ''.join(main.reverse_individual_words_in_stack('Hello World')) == 'olleH dlroW'


def test_reverse_individual_3_words():
    assert ''.join(main.reverse_individual_words_in_stack('We love potatoes')) == 'eW evol seotatop'


class TestStackIsEmpty:
    x = []

    def test_empty_stack(self):
        assert main.stack_is_empty(self.x) is True

    def test_pop_empty_stack(self):
        with pytest.raises(IndexError):
            main.pop_stack(self.x)

    def test_push_empty_stack(self):
        item = 'z'
        main.push_stack(self.x, item)
        assert len(self.x) == 1
        assert self.x[0] == 'z'

    def test_peek_empty_stack(self):
        with pytest.raises(IndexError):
            main.peek_stack(self.x)


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

    def test_reverse_stack(self):
        assert main.reverse_stack('abcdefg') == 'gfedcba'
