#!/usr/bin/python3


class Node:
    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Return the data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the data of the linked list"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """return the next_node value"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the position value"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ # Function to initialize head"""
    def __init__(self):
        self.__head = None

    def __repr__(self):
        str1 = []
        if self.__head is None:
            pass
        else:
            temp = self.__head
            while temp:
                str1.append(str(temp.data))
                temp = temp.next_node
        str1.sort(key=int)
        return ('\n'.join(str1))

    def sorted_insert(self, value):
        index = 0
        if self.__head is None:
            new_node = Node(value)
            self.__head = new_node
            return
        new_node = Node(value)
        new_node.next_node = self.__head
        self.__head = new_node
