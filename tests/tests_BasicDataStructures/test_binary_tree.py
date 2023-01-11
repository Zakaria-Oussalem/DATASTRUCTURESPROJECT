from BasicDataStructures.BasicDataStructures import BinarySearchTree
import pytest


@pytest.fixture
def build_search_tree():
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    root = BinarySearchTree(elements[0])
    for e in elements[1:]:
        root.add_child(e)
    return root


def test_good_tree(build_search_tree):
    assert build_search_tree.left.left.data == 1
    assert build_search_tree.left.right.data == 9
    assert build_search_tree.right.data == 20


def test_pre_order_traversal(build_search_tree):
    assert build_search_tree.pre_order_traversal() == [17, 4, 1, 9, 20, 18, 23, 34]


def test_post_order_traversal(build_search_tree):
    assert build_search_tree.post_order_traversal() == [1, 9, 4, 18, 34, 23, 20, 17]


def test_in_order_traversal(build_search_tree):
    assert build_search_tree.in_order_traversal() == [1, 4, 9, 17, 18, 20, 23, 34]


@pytest.mark.parametrize(
    "test_input, tree, expected",
    [
        (17, "build_search_tree", True),
        (1, "build_search_tree", True),
        (34, "build_search_tree", True),
        (20, "build_search_tree", True),
        (10, "build_search_tree", False),
    ],
)
def test_search(test_input, tree, expected, request):
    tree = request.getfixturevalue(tree)
    assert tree.search(test_input) is expected


def test_min_max_sum(build_search_tree):
    assert build_search_tree.find_max() == 34
    assert build_search_tree.find_min() == 1
    assert build_search_tree.calculate_sum() == 126


@pytest.mark.parametrize(
    "test_input, tree, expected",
    [
        (17, "build_search_tree", [18, 4, 1, 9, 20, 23, 34]),
        (1, "build_search_tree", [17, 4, 9, 20, 18, 23, 34]),
        (34, "build_search_tree", [17, 4, 1, 9, 20, 18, 23]),
        (20, "build_search_tree", [17, 4, 1, 9, 23, 18, 34]),
        (10, "build_search_tree", [17, 4, 1, 9, 20, 18, 23, 34]),
    ],
)
def test_delete_big(test_input, tree, expected, request):
    tree = request.getfixturevalue(tree)
    tree = tree.delete(test_input)
    assert tree.pre_order_traversal() == expected


def test_delete_small():
    root = BinarySearchTree(17)
    root = root.delete(17)
    assert root == None
