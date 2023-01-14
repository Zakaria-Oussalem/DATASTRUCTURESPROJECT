from LeetCode.LeetCode_easy import addBinary
import pytest


@pytest.mark.parametrize(
    "input_1, input_2, expected",
    [
        ("0", "0", "0"),
        ("1", "1", "10"),
        ("1", "1010", "1011"),
        ("0", "1010", "1010"),
        ("10101", "11000", "101101"),
        ("11", "111", "1010"),
        ("101", "10", "111"),
    ],
)
def test_add_binary(input_1, input_2, expected):
    assert addBinary(input_1, input_2) == expected
