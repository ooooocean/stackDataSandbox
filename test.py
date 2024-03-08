import main
import pytest


def test_create_stack_accepts_single_word():
    assert main.create_text_stack('text') == ['t', 'e', 'x', 't']  #


class TestStackIsEmpty:
    x = []

    def test_empty_stack(self):
        assert main.stack_is_empty(self.x) is True


    def test_pop_empty_stack(self):
        with pytest.raises(IndexError):
            main.pop_stack(self.x, 'z')


class TestStackIsNotEmpty:
    def test_non_empty_stack(self):
        x = ['t', 'e', 's', 't']
        assert main.stack_is_empty(x) is False
