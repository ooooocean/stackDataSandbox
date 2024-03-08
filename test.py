import main

def test_create_stack_accepts_single_word():
    assert main.create_text_stack('text') == ['t', 'e', 'x', 't']#

class TestIsEmpty:
    def test_empty_stack(self):
        x = []
        assert main.stack_is_empty(x) is True

    def test_non_empty_stack(self):
        x = ['t', 'e', 's', 't']
        assert main.stack_is_empty(x) is False
