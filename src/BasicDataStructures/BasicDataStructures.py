# type: ignore
# Stack Data structure
class Stack:
    """_summary_
    Class of Stacks Data structure
    """

    def __init__(self):
        self.stack = list()

    def push(self, val):
        """_summary_
                Function that adds a new value to the stack
        Args:
            val (object): data to add to the stack
        """
        self.stack.append(val)

    def pop(self):
        """_summary_
                Function that enables removing the last element of the stack and returns it
        Returns:
            object: None if the stack is empty, and the last object in teh stack otherwise
        """
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        """_summary_
                Function that enables us to get the last element of the stack
        Returns:
            object: None if the stack is empty, and the last object in teh stack otherwise.
        """
        if self.stack:
            return self.stack[-1]
        return None

    def is_empty(self):
        """_summary_
                Checking wether the stack is empty or not
        Returns:
            bool: True if the stack is empty and False otherwise
        """
        return len(self.stack) == 0

    def __str__(self):
        """_summary_
            Prints the stack.
        Returns:
            string: String representation of the stack.
        """
        return self.stack.__str__()


# Linked Lists:


class Node:
    """Class that defines nodes in linked list"""

    def __init__(self, data=None, next=None) -> None:
        """Initialisation

        Args:
            data (object, optional): The content of the node. Defaults to None.
            next (object, optional): link to the next node. Defaults to None.
        """
        self.data = data
        self.next = next


class LinkedList:
    """Class defining LinkedLists"""

    def __init__(self) -> None:
        """Initialisation"""
        self.head = None

    def insert_begin(self, data: object) -> None:
        """Adding a Node to the begining of the linked list

        Args:
            data (Node): New node to add at the begining
        """
        node = Node(data, self.head)
        self.head = node  # type: ignore [assignment]

    def insert_end(self, data: object) -> None:
        """Insertion of data at the end of a LinkedList

        Args:
            data (object): Object to be inserted
        """
        if self.head is None:
            node = Node(data)
            self.head = node  # type: ignore [assignment]
            return

        iterator = self.head  # type: ignore [unreachable]

        while iterator.next is not None:
            iterator = iterator.next

        iterator.next = Node(data)

    def print(self):
        """String representation of the linked lists"""
        if self.head is None:
            return ""

        toPrint = ""
        iterator = self.head

        while iterator.next is not None:
            toPrint += str(iterator.data) + " -- "
            iterator = iterator.next
        toPrint += str(iterator.data) + " -- "
        return toPrint.strip()

    def insert_values(self, values: list):  # type: ignore [type-arg]
        """To insert many values at the same time

        Args:
            values (list): List of values to be inserted
        """
        if values:
            for e in values:
                self.insert_end(e)
        return

    def get_lenght(self) -> int:
        """Get the lenght of a linked list

        Returns:
            int: lenght of the linked list
        """
        if self.head is None:
            return 0

        iterator = self.head
        counter = 1
        while iterator.next is not None:
            iterator = iterator.next
            counter += 1
        return counter

    def remove_at(self, index: int):
        """Method to remove a node from the linked list

        Args:
            index (int): Index and location of the node to remove
        """
        if self.head is None:
            return

        # basic case
        if index == 0:
            self.head = self.head.next
            return

        # variables to go through and track nodes
        iterator = self.head

        # Going through the linked list
        for i in range(index - 1):
            # In case the index > length of the linked list
            if iterator.next.next is None:
                return

            # continuing to run through the LL
            iterator = iterator.next

        # "Removing" Node in the middle by linking the one before to the one after
        iterator.next = iterator.next.next

    def insert_at(self, index: int, data: object):
        """Method to insert a node in some location in the linked list

        Args:
            index (int): Index and location of insertion
        """
        # basic case
        if index == 0:
            self.insert_begin(data)
            return
        if self.head is None:
            return

        # variables to go through and track nodes
        iterator = self.head

        # Going through the linked list
        for i in range(index - 1):
            # In case the index > length of the linked list
            if iterator.next is None:
                raise Exception("The index is far bigger than the lenght of the LL")

            # continuing to run through the LL
            iterator = iterator.next

        # "inserting" Node in the middle by linking the one before to the one after
        node = Node(data)
        node.next = iterator.next
        iterator.next = node

    def insert_after_value(self, dt_after: object, dt_insert: object):
        """Method that inserts a value after the first occurance of a certian value

        Args:
            dt_after (object): Value we are looking for to insert after it
            dt_insert (object): The value to insert
        """
        # variables to go through and track nodes
        iterator = self.head

        # Going through the linked list
        while iterator:
            # When we find value, we do the changes
            if iterator.data == dt_after:
                node = Node(dt_insert, iterator.next)
                iterator.next = node
                return
            iterator = iterator.next

    def remove_by_value(self, dt_remove: object):
        """Method that removes the first occurance of a certian value

        Args:
            dt_remove (object): Value to remove
        """
        if self.head == None:
            return
        # basic case
        if self.head.data == dt_remove:
            self.head = self.head.next
            return

        # variables to go through and track nodes
        iterator = self.head

        # Going through the linked list
        while iterator.next:
            # When we find value, we do the changes
            if iterator.next.data == dt_remove:
                iterator.next = iterator.next.next
                return
            iterator = iterator.next


# Doubly Linked Lists


class dNode:
    """Node for double linked lists"""

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class dLinkedList:
    """Class defining double LinkedLists"""

    def __init__(self) -> None:
        """Initialisation"""
        self.head = None

    def insert_begin(self, data: object) -> None:
        """Adding a Node to the begining of the linked list

        Args:
            data (Node): New node to add at the begining
        """
        if self.head:
            node = dNode(data, self.head, None)
            self.head.prev = node
            self.head = node
        else:
            node = dNode(data, self.head)
            self.head = node

    def insert_end(self, data: object) -> None:
        """Insertion of data at the end of a LinkedList

        Args:
            data (object): Object to be inserted
        """

        if self.head is None:
            node = dNode(data)
            self.head = node
            return None

        iterator = self.head

        while iterator.next:
            iterator = iterator.next

        iterator.next = dNode(data)
        iterator.next.prev = iterator

    def insert_values(self, values: list):
        """To insert many values at the same time

        Args:
            values (list): List of values to be inserted
        """
        if values:
            for e in values:
                self.insert_end(e)
        return

    def print_forward(self):
        """String representation of the linked lists"""
        if self.head is None:
            return ""

        toPrint = ""
        iterator = self.head

        while iterator.next:
            toPrint += str(iterator.data) + " --> "
            iterator = iterator.next
        toPrint += str(iterator.data) + " --> "
        return toPrint.strip()

    def print_backwards(self):
        """String representation of the linked lists"""
        if self.head is None:
            return ""

        toPrint = ""
        iterator = self.head

        # First we travel to the end of the linked list
        while iterator.next:
            iterator = iterator.next

        while iterator:
            toPrint += str(iterator.data) + " --> "
            iterator = iterator.prev
        return toPrint.strip()


# Hash Tables :


class HashTable:
    """Class Implementing HashTables"""

    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key: str) -> int:
        """The Hash function

        Args:
            key (str): It takes the input to hash
        Returns:
            int: computed hash number
        """
        h = 0
        for char in key:
            h += ord(char)
        # we assume the size of the list is 100
        return h % 100

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))

    # Using Linear Probing:
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        index = h
        if self.arr[index]:
            while self.arr[index] and index < self.MAX:
                if self.arr[index][0] == key:
                    self.arr[index][1] = val
                    return
                index += 1
            index = 0
            while self.arr[index] and index < h:
                if self.arr[index][0] == key:
                    self.arr[index][1] = val
                    return
                index += 1
            raise Exception("Hash map is full")
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                return element[1]

    # using linear probing:
    def __getitem__(self, key):
        h = self.get_hash(key)
        index = h
        if self.arr[index]:
            while self.arr[index] and index < self.MAX:
                if self.arr[h][0] == key:
                    return self.arr[h][1]
                index += 1
            index = 0
            while self.arr[index] and index < h:
                if self.arr[h][0] == key:
                    return self.arr[h][1]
                index += 1


# Trees :


class TreeNode:
    def __init__(self, data, function=None) -> None:
        self.data = data
        self.function = function
        self.children = []
        self.parent = None

    def add_child(self, child):
        """Function that adds a child to a node in a tree

        Args:
            child (TreeNode): The tree node we whish to add as a child
        """
        child.parent = self
        self.children.append(child)

    def get_level(self) -> int:
        """This function gets the level of a node in a tree.
            A level is how many nodes down we need to travel to get
            to the current node from the head.
        Returns:
            int: level
        """
        level = 0
        iterator = self.parent
        while iterator:
            level += 1
            iterator = iterator.parent

        return level

    def print_tree(self, type="name", level=-1):

        if type == "both":
            to_print = (
                " " * self.get_level() * 3
                + "|--"
                + self.data
                + " ("
                + self.function
                + ")"
                if self.parent
                else self.data + " (" + self.function + ")"
            )
            print(to_print)
            if level > self.get_level() or level < 0:
                if self.children:
                    for child in self.children:
                        child.print_tree(type, level)

        elif type == "name":
            to_print = (
                " " * self.get_level() * 3 + "|--" + self.data
                if self.parent
                else self.data
            )
            print(to_print)

            if level > self.get_level() or level < 0:
                if self.children:
                    for child in self.children:
                        child.print_tree(type, level)

        elif type == "designation":
            to_print = (
                " " * self.get_level() * 3 + "|--" + self.function
                if self.parent
                else self.function
            )
            print(to_print)

            if self.children:
                for child in self.children:
                    child.print_tree(type)

        else:
            raise Exception("Invalid type")


# Binary search trees:


class BinarySearchTree:
    """Class implementing a binary search tree
    Unlike a normal tree, the right side is always bigger then the node
    and the left side is always smaller (recursivly accross all the tree
    """

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        elif data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(data)
                return
            self.left.add_child(data)

        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
                return
            self.right.add_child(data)

    def pre_order_traversal(self):

        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def in_order_traversal(self):

        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):

        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)

        return elements

    def search(self, val: int) -> bool:
        """function to see if a value exists in tree or not

        Args:
            val (int): the value to search for in the tree

        Returns:
            bool: True if the value exists and False otherwise
        """
        if self.data == val:
            return True
        elif self.data > val and self.left is not None:
            return self.left.search(val)

        elif self.data < val and self.right is not None:
            return self.right.search(val)

        else:
            return False

    def find_min(self):
        iterator = self
        while iterator.left:
            iterator = iterator.left
        return iterator.data

    def find_max(self):
        iterator = self
        while iterator.right:
            iterator = iterator.right
        return iterator.data

    def calculate_sum(self) -> int:
        """calculate sum of all numbers in a tree

        Args:
            sum (int, optional): current sum (recursion). Defaults to 0.

        Returns:
            float: total sum
        """
        total_sum = 0
        if self.left is not None:
            total_sum += self.left.calculate_sum()
        if self.right is not None:
            total_sum += self.right.calculate_sum()
        total_sum += self.data

        return total_sum

    def delete(self, val):
        # basic case:
        if self.right is None and self.left is None:
            if self.data == val:
                return None
            else:
                return self
        elif self.right is None:
            if self.data == val:
                return self.left
            else:
                self.left = self.left.delete(val)
                return self
        elif self.left is None:
            if self.data == val:
                return self.right
            else:
                self.right = self.right.delete(val)
                return self
        else:
            if self.data == val:
                mini = self.right.find_min()
                self.data = mini
                self.right = self.right.delete(mini)
            elif self.data > val:
                self.left = self.left.delete(val)
            else:
                self.right = self.right.delete(val)
            return self


# Graphs


class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = dict[str, int]
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_paths(self, start: str, end: str, path=[]) -> list[list[str]]:
        """function to get all the paths between two nodes

        Args:
            start (str): starting node
            end (srt): ending node
            path (list, optional): current path being built between the two nodes. Defaults to [].

        Returns:
            list: list of paths between two nodes
        """
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths = []
        for element in self.graph_dict[start]:
            if element not in path:
                paths += self.get_paths(element, end, path)
        return paths

    def get_shortest_path(self, start: str, end: str) -> list[str]:
        """getting shortest path in a graph

        Args:
            start (str): starting node of the path
            end (str): the ending node of the path

        Returns:
            list: the shortest path between nodes
        """
        paths = self.get_paths(start, end)
        mini = paths[0]
        for p in paths:
            if len(p) < len(mini):
                mini = p
        return mini
