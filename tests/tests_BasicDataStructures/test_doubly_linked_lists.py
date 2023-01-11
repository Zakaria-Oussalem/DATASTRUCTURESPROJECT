from BasicDataStructures.BasicDataStructures import dLinkedList
import pytest


def test_insert_begin():
    ll = dLinkedList()
    ll.insert_begin("banana")
    ll.insert_begin("blueberry")
    ll.insert_begin("orange")
    assert ll.print_forward() == "orange --> blueberry --> banana -->"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([], ""),
        (["banana", "blueberry", "orange"], "banana --> blueberry --> orange -->"),
    ],
)
def test_print_forward(test_input, expected):
    ll = dLinkedList()
    ll.insert_values(test_input)
    assert ll.print_forward() == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ([], ""),
        (["banana", "blueberry", "orange"], "orange --> blueberry --> banana -->"),
    ],
)
def test_print_backward(test_input, expected):
    ll = dLinkedList()
    ll.insert_values(test_input)
    assert ll.print_backwards() == expected
