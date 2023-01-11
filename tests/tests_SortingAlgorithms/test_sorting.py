from SortingAlgorithms.BasicSortingAlgorithms import *
import pytest


@pytest.mark.parametrize(
    "mylist, val, expected",
    [
        ([], 10, False),
        ([10], 10, True),
        ([10], 11, False),
        ([12, 13, 15, 18, 29], 15, True),
        ([12, 13, 15, 18], 15, True),
        ([12, 13, 15, 18], 18, True),
        ([12, 13, 15, 18], 12, True),
        ([12, 13, 15, 18], 19, False),
        ([12, 13, 15, 18], 11, False),
        ([12, 13, 15, 18], 14, False),
    ],
)
def test_binary_search(mylist, val, expected):
    assert BinaryS(mylist, val) is expected


@pytest.mark.parametrize(
    "mylist, val, expected",
    [
        ([], 10, False),
        ([10], 10, True),
        ([10], 11, False),
        ([12, 13, 15, 18, 29], 15, True),
        ([12, 13, 15, 18], 15, True),
        ([12, 13, 15, 18], 18, True),
        ([12, 13, 15, 18], 12, True),
        ([12, 13, 15, 18], 19, False),
        ([12, 13, 15, 18], 11, False),
        ([12, 13, 15, 18], 14, False),
    ],
)
def test_binary_search_recursive(mylist, val, expected):
    assert BinaryS(mylist, val) is expected


@pytest.mark.parametrize(
    "mylist, expected",
    [
        ([], []),
        ([10], [10]),
        ([12, 13, 15, 18, 29], [12, 13, 15, 18, 29]),
        ([12, 13], [12, 13]),
        ([12, 10], [10, 12]),
        ([18, 16, 14, 9, 1], [1, 9, 14, 16, 18]),
        ([1, 6, 2, 9, 7, 0], [0, 1, 2, 6, 7, 9]),
        ([12, 12, 11, 11], [11, 11, 12, 12]),
    ],
)
def test_bubble_sort(mylist, expected):
    assert bubbleSort(mylist) == expected


@pytest.mark.parametrize(
    "mylist, expected",
    [
        ([], []),
        ([10], [10]),
        ([12, 13, 15, 18, 29], [12, 13, 15, 18, 29]),
        ([12, 13], [12, 13]),
        ([12, 10], [10, 12]),
        ([18, 16, 14, 9, 1], [1, 9, 14, 16, 18]),
        ([1, 6, 2, 9, 7, 0], [0, 1, 2, 6, 7, 9]),
        ([12, 12, 11, 11], [11, 11, 12, 12]),
    ],
)
def test_quickSortH(mylist, expected):
    assert quickSortH(mylist) == expected


@pytest.mark.parametrize(
    "mylist, expected",
    [
        ([], []),
        ([10], [10]),
        ([12, 13, 15, 18, 29], [12, 13, 15, 18, 29]),
        ([12, 13], [12, 13]),
        ([12, 10], [10, 12]),
        ([18, 16, 14, 9, 1], [1, 9, 14, 16, 18]),
        ([1, 6, 2, 9, 7, 0], [0, 1, 2, 6, 7, 9]),
        ([12, 12, 11, 11], [11, 11, 12, 12]),
    ],
)
def test_quickSortL(mylist, expected):
    assert quickSortL(mylist) == expected


@pytest.mark.parametrize(
    "mylist, expected",
    [
        ([], []),
        ([10], [10]),
        ([12, 13, 15, 18, 29], [12, 13, 15, 18, 29]),
        ([12, 13], [12, 13]),
        ([12, 10], [10, 12]),
        ([18, 16, 14, 9, 1], [1, 9, 14, 16, 18]),
        ([1, 6, 2, 9, 7, 0], [0, 1, 2, 6, 7, 9]),
        ([12, 12, 11, 11], [11, 11, 12, 12]),
    ],
)
def test_insertionSort(mylist, expected):
    assert insertionSort(mylist) == expected


@pytest.mark.parametrize(
    "mylist, expected",
    [
        ([], []),
        ([10], [10]),
        ([12, 13, 15, 18, 29], [12, 13, 15, 18, 29]),
        ([12, 13], [12, 13]),
        ([12, 10], [10, 12]),
        ([18, 16, 14, 9, 1], [1, 9, 14, 16, 18]),
        ([1, 6, 2, 9, 7, 0], [0, 1, 2, 6, 7, 9]),
        ([12, 12, 11, 11], [11, 11, 12, 12]),
    ],
)
def test_mergeSort(mylist, expected):
    assert mergeSort(mylist) == expected


@pytest.mark.parametrize(
    "mylist, expected",
    [
        ([], []),
        ([10], [10]),
        ([12, 13, 15, 18, 29], [12, 13, 15, 18, 29]),
        ([12, 13], [12, 13]),
        ([12, 10], [10, 12]),
        ([18, 16, 14, 9, 1], [1, 9, 14, 16, 18]),
        ([1, 6, 2, 9, 7, 0], [0, 1, 2, 6, 7, 9]),
        ([12, 12, 11, 11], [11, 11, 12, 12]),
    ],
)
def test_selectionSort(mylist, expected):
    assert selectionSort(mylist) == expected
