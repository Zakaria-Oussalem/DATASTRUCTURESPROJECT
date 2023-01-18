from LeetCode.LeetCode_medium import addTwoNumbers, Node, Anagram
import pytest


def test_Node_equal():
    l1 = Node()
    l1.insert_values([1, 2, 3])
    assert l1 == l1


@pytest.mark.parametrize(
    "input_1, input_2, expected",
    [([1, 0, 2], [2, 4, 6], [3, 4, 8])],
)
def test_add_binary(input_1, input_2, expected):
    l1 = Node()
    l2 = Node()
    l1.insert_values(input_1)
    l2.insert_values(input_2)
    exp = Node()
    exp.insert_values(expected)
    print(l1.print())
    print("")
    print(l2.print())
    assert addTwoNumbers(l1, l2) == exp


def test_annargram():
    b = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    temp = Anagram(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert len(b) == len(temp)
    for e in temp:
        assert sorted(e) in b

        
