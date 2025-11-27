class Node:
    """
        Lightweight, nonpublic class for storing a doubly linked node.
    """

    def __init__(self, element=None, prev=None, next=None):  # initialize node’s fields
        self._element = element  # user’s element
        self._prev = prev  # previous node reference
        self._next = next  # next node reference


class DoubleLinkedList:
    def __init__(self):
        """
            Create an empty DoubleLinkedList.
            You can also modify this function if needed
        """
        self._header = Node(None, None, None)
        self._trailer = Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """
            Return the number of elements in the DoubleLinkedList.
        """
        return self._size

    def is_empty(self):
        """
            Return True if the DoubleLinkedList is empty.
        """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def __str__(self):
        # Please write your code here
        res = []
        currNode = self._header._next
        while currNode != self._trailer:
            res.append(str(currNode._element) + '<-->')
            currNode = currNode._next
        res_str = ''.join(res)
        return 'Header<-->' + res_str + 'Trailer'

    def insertAtFirst(self, e):
        """
            Add element e to the start of the DoubleLinkedList.
        """

        # Please write your code here
        self._insert_between(e,self._header,self._header._next)

    def remove_all(self, e):
        """
            Removes all nodes with the node value e from
            the LinkedList. Throw the exception Exception
            ("Empty") if the LinkedList is empty.

            You have to maintain the LinkedList integrity
            when removing the nodes.
        """

        # Please write your code here
        if self._size == 0:
            raise Exception("Empty")
        else:
            currNode = self._header._next
            while currNode is not None:
                currNext = currNode._next
                if currNode._element == e:
                    self._delete_node(currNode)
                currNode = currNext
        

    def head_to_tail(self):
        """
            Swaps the LinkedLists first node with the lists
            last node.

            You have to maintain the LinkedList integrity
            when swapping the nodes.
        """

        # Please write your code here
        if self.is_empty() or self._size == 0:
            return
        currNode1 = self._header._next
        currNode2 = self._trailer._prev
        currNode3 = self._header._next._next
        currNode4 = self._trailer._prev._prev

        self._header._next = currNode2
        self._trailer._prev = currNode1
        
        currNode1._next = self._trailer
        currNode2._prev = self._header

        if self._size == 2:
            currNode1._prev = currNode2
            currNode2._next = currNode1
            return
        
        currNode1._prev = currNode4
        currNode2._next = currNode3
        currNode3._prev = currNode2
        currNode4._next = currNode1

    def printer(self, d):
        """
            returns a generator to yield all elements given in
            the direction d, either in forward or in reverse.
            Throw the exception Exception("Empty") if the
            LinkedList is empty.
        """

        # Please write your code here
        if d == 'forward':
            currNode = self._header._next
            while currNode != self._trailer:
                yield currNode._element
                currNode = currNode._next
            raise StopIteration()
        else:
            currNode = self._trailer._prev
            while currNode != self._header:
                yield currNode._element
                currNode = currNode._prev
            raise StopIteration()

    def reverse_sub(self, a, b):
        """
            reverses the range between a and b in the
            LinkedList. Your function has to work in-place.
            Throw the exception Exception("Empty") if the
            LinkedList is empty.
        """

        # Please write your code here
        currNode1 = self._header._next
        currNode2 = self._header._next
        for i in range(a):
            currNode1 = currNode1._next
        for i in range(b):
            currNode2 = currNode2._next
        
        before_head = currNode1._prev
        after_tail = currNode2._next
        curr = currNode1
        prev = after_tail
        
        for i in range(b - a + 1):
            next_node = curr._next
            curr._next = prev
            prev = curr
            curr._prev = next_node
            curr = next_node
        before_head._next = currNode2
        currNode1._next = after_tail
        after_tail._prev = currNode1
        currNode2._prev = before_head


    def compress(self):
        """
            Compresses the occurrence of elements in the
            unsorted LinkedList as tuples. Your function
            has to work in-place. Throw the exception
            Exception("Empty") if the LinkedList is empty.
        """

        # Please write your code here
        if self.is_empty():
            raise Exception("Empty")
        self.insertion_sort_descending()
        currNode1 = self._header._next
        currNode2 = self._header._next
        while currNode1 != self._trailer:
            count = 0
            while currNode1._element == currNode2._element and currNode2 != self._trailer:
                count += 1 
                currNode2 = currNode2._next
            self.insertAtFirst((currNode1._element, count))
            self.remove_all(currNode1._element)
            currNode1 = currNode2
    
    def insertion_sort_descending(self):
        if self._size == 0 or self._size == 1:
            return

        currNode = self._header._next._next
        while currNode != self._trailer:
            value_insert = currNode._element
            position_node = currNode._prev
            while position_node != self._header and position_node._element < value_insert:
                position_node._next._element = position_node._element
                position_node = position_node._prev

            position_node._next._element = value_insert
            currNode = currNode._next


def main():
    # Part A: Remove all

    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(22)
    ls1.insertAtFirst(10)
    ls1.insertAtFirst(22)
    ls1.insertAtFirst(35)

    print(ls1)  # Should print: Header<-->35<-->22<-->10<-->22<-->Trailer
    ls1.remove_all(22)
    print(ls1)  # Should print: Header<-->35<-->10<-->Trailer

    # ________________________________________________

    # Part B: Head to Tail

    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(5)
    ls1.insertAtFirst(10)
    ls1.insertAtFirst(22)
    ls1.insertAtFirst(35)

    print(ls1)  # Should print: Header<-->35<-->22<-->10<-->5<-->Trailer
    ls1.head_to_tail()
    print(ls1)  # Should print: Header<-->5<-->22<-->10<-->35<-->Trailer

    # ________________________________________________

    # Part C: Printer

    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(5)
    ls1.insertAtFirst(10)
    ls1.insertAtFirst(22)
    ls1.insertAtFirst(35)

    a = ls1.printer("forward")
    print(next(a))  # Should return: 35
    print(next(a))  # Should return: 22
    print(next(a))  # Should return: 10
    print(next(a))  # Should return: 5

    a = ls1.printer("reverse")
    print(next(a))  # Should return: 5
    print(next(a))  # Should return: 10
    print(next(a))  # Should return: 22
    print(next(a))  # Should return: 35

    # ________________________________________________

    # Part D: Reverse Sublist

    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(3)
    ls1.insertAtFirst(4)
    ls1.insertAtFirst(5)
    ls1.insertAtFirst(6)

    print(ls1)  # Should print: Header<-->6<-->5<-->4<-->3<-->2<-->1<-->Trailer
    ls1.reverse_sub(2, 5)
    print(ls1)  # Should print: Header<-->6<-->5<-->1<-->2<-->3<-->4<-->Trailer

    # ________________________________________________

    # Part E: Compress lists

    ls1 = DoubleLinkedList()
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(2)
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(1)
    ls1.insertAtFirst(5)
    ls1.insertAtFirst(2)

    print(ls1)  # Should print: Header<-->2<-->5<-->1<-->1<-->2<-->1<-->Trailer
    ls1.compress()
    print(ls1)  # Should print: Header<-->(1, 3)<-->(2, 2)<-->(5, 1)<-->Trailer


if __name__ == '__main__':
    main()
