from BasicDataStructures.BasicDataStructures import LinkedList
import pytest


def test_insert_begin():
    ll = LinkedList()
    ll.insert_begin("banana")
    ll.insert_begin("blueberry")
    ll.insert_begin("orange")
    assert ll.print() == "orange -- blueberry -- banana --"


def test_insert_end():
    ll = LinkedList()
    ll.insert_end("banana")
    ll.insert_end("blueberry")
    ll.insert_end("orange")
    assert ll.print() == "banana -- blueberry -- orange --"


@pytest.mark.parametrize(
    "test_input, expected",
    [([], ""), (["banana", "blueberry", "orange"], "banana -- blueberry -- orange --")],
)
def test_insert_values(test_input, expected):
    ll = LinkedList()
    ll.insert_values(test_input)
    assert ll.print() == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [([], 0), (["banana", "blueberry", "orange"], 3)],
)
def test_get_lenght(test_input, expected):
    ll = LinkedList()
    ll.insert_values(test_input)
    assert ll.get_lenght() == expected


@pytest.mark.parametrize(
    "test_input_1, test_input_2,  expected",
    [
        ([], "banana", ""),
        (["banana", "blueberry", "orange"], "banana", "blueberry -- orange --"),
        (["banana", "blueberry", "orange"], "blueberry", "banana -- orange --"),
        (["banana"], "banana", ""),
    ],
)
def test_remove_by_value(test_input_1, test_input_2, expected):
    ll = LinkedList()
    ll.insert_values(test_input_1)
    ll.remove_by_value(test_input_2)
    assert ll.print() == expected


@pytest.mark.parametrize(
    "test_input_1, test_input_2,  expected",
    [
        ([], 1, ""),
        (["banana", "blueberry", "orange"], 0, "blueberry -- orange --"),
        (["banana", "blueberry", "orange"], 1, "banana -- orange --"),
        (["banana", "blueberry", "orange"], 2, "banana -- blueberry --"),
        (["banana"], 0, ""),
        (["banana", "orange"], 2, "banana -- orange --"),
    ],
)
def test_remove_at(test_input_1, test_input_2, expected):
    ll = LinkedList()
    ll.insert_values(test_input_1)
    ll.remove_at(test_input_2)
    assert ll.print() == expected


@pytest.mark.parametrize(
    "test_input_1, test_input_2, test_input_3, expected",
    [
        ([], 1, "banana", ""),
        ([], 0, "banana", "banana --"),
        (
            ["banana", "blueberry", "orange"],
            0,
            "apple",
            "apple -- banana -- blueberry -- orange --",
        ),
        (
            ["banana", "blueberry", "orange"],
            1,
            "apple",
            "banana -- apple -- blueberry -- orange --",
        ),
        (
            ["banana", "blueberry", "orange"],
            3,
            "apple",
            "banana -- blueberry -- orange -- apple --",
        ),
    ],
)
def test_insert_at(test_input_1, test_input_2, test_input_3, expected):
    ll = LinkedList()
    ll.insert_values(test_input_1)
    ll.insert_at(test_input_2, test_input_3)
    assert ll.print() == expected
