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
            main.pop_stack(self.x)


class TestStackIsNotEmpty:
    x = ['t', 'e', 's', 't']
    def test_non_empty_stack(self):
        assert main.stack_is_empty(self.x) is False

    def test_pop_non_empty_stack(self):
        assert main.pop_stack(self.x) == 't'