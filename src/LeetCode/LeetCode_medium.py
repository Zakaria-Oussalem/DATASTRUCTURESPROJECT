# Definition for singly-linked list.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def insert_end(self, val):
        if self.val is None:
            self.val = val
            return

        iterator = self

        while iterator.next:
            iterator = iterator.next

        iterator.next = Node(val)

    def insert_values(self, values):
        if values:
            for e in values:
                self.insert_end(e)

    def __eq__(self, second: object) -> bool:

        it1 = self
        it2 = second
        while it1 or it2:
            if not it1:
                return False
            if not it2:
                return False
            if it1.val == it2.val:
                it1 = it1.next
                it2 = it2.next
            else:
                return False
        return True

    def print(self):
        """String representation of the linked lists"""

        toPrint = ""
        iterator = self

        while iterator.next is not None:
            toPrint += str(iterator.val) + " -- "
            iterator = iterator.next
        toPrint += str(iterator.val) + " -- "
        return toPrint.strip()


# addTwoNumbers
def addTwoNumbers(l1: Node, l2: Node) -> Node:

    if l1.val is None:
        return l2
    if l2.val is None:
        return l1

    carry = l1.val + l2.val
    result = Node(val=carry % 10)
    iterator = result
    carry = carry // 10
    l1 = l1.next
    l2 = l2.next
    while l1 or l2 or carry:
        iterator.next = Node()
        iterator = iterator.next
        if l1:
            carry = l1.val + carry
            l1 = l1.next
        if l2:
            carry = l2.val + carry
            l2 = l2.next

        iterator.val = carry % 10
        carry = carry // 10

    return result


#####################
#####################


def Anagram(l: list[str]) -> list[list[str]]:
    # my first idea is that we will traverse the list and when we see something that matches we add it
    # to the dictionnary

    ann = dict()
    for e in l:
        temp = "".join(sorted(e))
        if temp in ann:
            ann[temp].append(e)
            continue
        ann[temp] = [e]

    return list(ann.values())


print(Anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
