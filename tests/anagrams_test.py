import main
import pytest


@pytest.mark.parametrize("index, word", [
    (0, 'A'),
    (3725, 'Axis'),
])
def test_read_word_list(index, word):
    word_list = main.read_word_list()
    assert word_list[index] == word


# Write your tests here!
