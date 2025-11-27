class Node:
    def __init__(self, element=None, next=None):
        self._element = element
        self._next = next


class SingleLinkedList:
    def __init__(self):
        """Create an empty LinkedList."""
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the LinkedList."""
        return self._size

    def is_empty(self):
        """Return True if the LinkedList is empty."""
        return self._size == 0

    def insertAtFirst(self, e):
        """Add element e to the start of the LinkedList."""
        newNode = Node(e, self._head)
        self._head = newNode
        self._size += 1

    def deleteFirst(self):
        """Remove and return the first element from the LinkedList.
        Raise Empty exception if the Linked list is empty.
        Return: the value of the first node
        """
        if self.is_empty():
            raise Exception('LinkedList is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def deleteLast(self):
        """Remove and return the last element from the LinkedList.
        Raise Empty exception if the Linked list is empty.
        Return: the value of the last node
        """
        if self.is_empty():
            raise Exception('LinkedList is empty')
        prv = None
        cur = self._head
        while cur._next is not None:
            cur = cur._next
            prv = prv._next if prv is not None else self._head
        if prv is None:
            self._head = None
        else:
            prv._next = None
        self._size -= 1
        return cur._element

    def unOrderedSearch(self, target):
        currNode = self._head
        while currNode is not None and currNode._element != target:
            currNode = currNode._next
        return currNode is not None

    def __str__(self):
        result = "Head-->"
        currNode = self._head
        while currNode is not None:
            result += str(currNode._element) + "-->"
            currNode = currNode._next
        return result + "None"

    def remove(self, k):
        """
            This function deletes the node indexed by the parameter k.
            
            Throw the exception Exception("Short") if the LinkedList is too short for the operation.     
        """

        # Please write your code here
        if self._size <= k:
            raise Exception('Empty')
        if k == 0:
            self._head = self._head._next
        else:
            currNode = self._head
            for i in range(k-1):
                currNode = currNode._next
            currNode1 = currNode._next
            currNode._next = currNode1._next
            currNode1._next = None
            self._size -= 1
            
        

    def frontswap(self):
        """
            This function swaps the linked lists first and second node
        
            Throw the exception Exception("Short") if the LinkedList is too short for the operation.
        """

        # Please write your code here
        if self._size <= 1:
            raise Exception("Short")
        else:
            currNode = self._head
            currNode1 = self._head._next
            currNode._next = currNode1._next
            currNode1._next = currNode
            self._head = currNode1



    def tailswap(self):
        """
            This function swaps the linked lists last and second last node
        
            Throw the exception Exception("Short") if the LinkedList is too short for the operation.
        """

        # Please write your code here
        if self._size <= 1:
            raise Exception("Short")
        elif self._size == 2:
            tail = self._head._next
            tail._next = self._head
            self._head = tail
        else:
            currNode = self._head
            for i in range(self._size-3):
                currNode = currNode._next
            currNode1 = currNode._next
            currNode2 = currNode1._next
            currNode._next = currNode2
            currNode2._next = currNode1
            currNode1._next = None

        

    def add_sparse(self, other):
        """
            This functions performs an addition of two sparse vectors.
            The result is a sparse vector added on self.
        """

        # Please write your code here
        res = SingleLinkedList()
        currNode1 = self._head
        currNode2 = other._head
        
        while currNode1 != None and currNode2 != None:
            if currNode1._element[0] == currNode2._element[0]:
                res.insertAtFirst((currNode1._element[0],currNode1._element[1] + currNode2._element[1]))
                currNode1 = currNode1._next
                currNode2 = currNode2._next
    
            elif currNode1._element[0] < currNode2._element[0]:
                res.insertAtFirst(currNode1._element)
                currNode1 = currNode1._next    
            elif currNode1._element[0] > currNode2._element[0]:
                res.insert_ordered(currNode2._element)
                currNode2 = currNode2._next
                
        while currNode1 != None and currNode2 is None:
            res.insertAtFirst(currNode1._element)
            currNode1 = currNode1._next
        
        while currNode1 is None and currNode2 != None:
            res.insertAtFirst(currNode2._element)
            currNode2 = currNode2._next
              
        self._head = res._head
        self.reverse()
        
    def reverse(self):
        prevNode = None
        currNode = self._head
        while currNode != None:
            next_temp = currNode._next
            currNode._next = prevNode
            prevNode = currNode
            currNode = next_temp
        self._head = prevNode
    
    def insertAtLast(self, e):
        newNode = Node(e)
        if self._head == None:
            self._head = newNode
        else:
            currNode = self._head
            while currNode._next != None:
                currNode = currNode._next
            currNode._next = newNode
        self._size += 1





class SparseMatrix:
    def __init__(self, mat=None):
        """
            a constructor for accepting matrices in the form of nested lists.
            The constructor creates a sparse matrix from the provided input.
            There will be two-dimensional matrices at most. The form of provided
            matrices is MxN.
        """

        # Please write your code here
        self._rows = len(mat)
        self._columns = len(mat[0])
        self._original = SingleLinkedList()
        for i in reversed(range(self._rows)):
            sublist = SingleLinkedList()
            for j in reversed(range(self._columns)):
                if mat[i][j] != 0:
                    sublist.insertAtFirst((j, mat[i][j]))
            if sublist._size > 0:
                self._original.insertAtFirst((i, sublist))
        

    def __str__(self):
        """
            print function, output a string
        """

        # Please write your code here
        result = "Head"
        currNode = self._original._head
        while currNode != None:
            result += '-->' + '(' + str(currNode._element[0]) + ', ' + 'Head'
            sublist = currNode._element[1]
            currNode1 = sublist._head
            for i in range(sublist._size):
                result += "-->(" + str(currNode1._element[0]) + ", " + str(currNode1._element[1]) + ")"
                currNode1 = currNode1._next
            result += "-->" + "None" + ")"
            currNode = currNode._next
        return result + "-->" + "None"


    def __mul__(self, other):
        """
            a magic function to form the product of two sparse matrices
        """

        # Please write your code here
        currNode1 = self._original._head
        currNode2 = other._original._head
        result = SparseMatrix([[]])
        while currNode1 is not None:
            sublist = SingleLinkedList()
            while currNode2 is not None:
                row = currNode1._element[0]
                column = currNode2._element[0]
                count = 0
                currNode1_sublist = currNode1._element[1]._head
                currNode2_sublist = currNode2._element[1]._head
                while currNode1_sublist is not None and currNode2_sublist is not None:
                    if currNode1_sublist._element[0] == currNode2_sublist._element[0]:
                        count += currNode1_sublist._element[1] * currNode2_sublist._element[1]
                        currNode1_sublist = currNode1_sublist._next
                        currNode2_sublist = currNode2_sublist._next
                    elif currNode1_sublist._element[0] < currNode2_sublist._element[0]:
                        currNode1_sublist = currNode1_sublist._next
                    elif currNode1_sublist._element[0] > currNode2_sublist._element[0]:
                        currNode2_sublist = currNode2_sublist._next

                if count != 0:
                    sublist.insertAtLast((column, count))
                currNode2 = currNode2._next

            if sublist._size > 0:
                result._original.insertAtLast((row, sublist))
            currNode1 = currNode1._next
            currNode2 = other._original._head

        return result

    def __add__(self, other):
        """
            a magic function to form the addition of two sparse matrices
        """

        # Please write your code here

        currNode1 = self._orinigal._head
        currNode2 = other._original._head
        result = SparseMatrix([[]])
        while currNode1 is not None and currNode2 is not None:
            if currNode1._element[0] == currNode2._element[0]:
                sublist = currNode1._element[1].add_sparse(currNode2._element[1])
                if sublist._size > 0:
                    result._original.insertAtLast((currNode1._element[0], sublist))

                currNode1 = currNode1._next
                currNode2 = currNode2._next

            elif currNode1._element[0] < currNode2._element[0]:
                result._original.insertAtLast(currNode1._element)
                currNode1 = currNode1._next

            elif currNode1._element[0] > currNode2._element[0]:
                result._original.insertAtLast(currNode2._element)
                currNode2 = currNode2._next

        while currNode1 is not None:
            result._original.insertAtLast(currNode1._element)
            currNode1 = currNode1._next

        while currNode2 is not None:
            result._original.insertAtLast(currNode2._element)
            currNode2 = currNode2._next

        return result

def main():
    # Part A: remove()
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(5)
    ls1.insertAtFirst(10)
    ls1.insertAtFirst(22)
    ls1.insertAtFirst(35)

    print(ls1)  # Should print: Head-->35-->22-->10-->5-->None
    ls1.remove(2)
    print(ls1)  # Should print: Head-->35-->22-->5-->None
    ls1.remove(2)
    print(ls1)  # Should print: Head-->35-->22-->None
    ls1.remove(0)
    print(ls1)  # Should print: Head-->22-->None

    # ________________________________________________

    # Part B: frontswap()
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(5)
    ls1.insertAtFirst(10)
    ls1.insertAtFirst(22)
    ls1.insertAtFirst(35)

    print(ls1)  # Should print: Head-->35-->22-->10-->5-->None
    ls1.frontswap()
    print(ls1)  # Should print: Head-->22-->35-->10-->5-->None

    # ________________________________________________

    # Part C: tailswap()
    ls1 = SingleLinkedList()
    ls1.insertAtFirst(5)
    ls1.insertAtFirst(10)
    ls1.insertAtFirst(22)
    ls1.insertAtFirst(35)

    print(ls1)  # Should print: Head-->35-->22-->10-->5-->None
    ls1.tailswap()
    print(ls1)  # Should print: Head-->35-->22-->5-->10-->None

    # ________________________________________________

    # Part D: Sparse Vector

    ls1 = SingleLinkedList()
    ls1.insertAtFirst((5, 0))
    ls1.insertAtFirst((4, 0))
    ls1.insertAtFirst((3, 5))
    ls1.insertAtFirst((2, 3))
    ls1.insertAtFirst((1, 2))
    ls1.insertAtFirst((0, 1))

    ls2 = SingleLinkedList()
    ls2.insertAtFirst((5, 4))
    ls2.insertAtFirst((4, 1))
    ls2.insertAtFirst((3, 2))
    ls2.insertAtFirst((2, 1))
    ls2.insertAtFirst((1, 0))
    ls2.insertAtFirst((0, 0))

    ls1.add_sparse(ls2)

    print(ls1)  # Should print: Head-->(0, 1)-->(1, 2)-->(2, 4)-->(3, 7)-->(4, 1)-->(5, 4)-->None

    # ________________________________________________

    # Part E: Sparse Matrix

    mat1 = [[1, 1, 1], [1, 2, 3]]
    mat2 = [[0, 0, 0], [1, 1, 1]]
    mat3 = [[0, 1], [1, 0], [0, 0]]
    sp1 = SparseMatrix(mat1)
    sp2 = SparseMatrix(mat2)
    sp3 = SparseMatrix(mat3)

    sp4 = sp1 + sp2
    print(sp4)  # Should print a list: Head-->(0, Head-->(0, 1)-->(1, 1)-->(2, 1)-->None)-->(1, Head-->(0, 2)-->(1, 3)-->(2, 4)-->None)--None

    sp5 = sp2 * sp3
    print(sp5)  # Should print a list: Head-->(1, Head-->(0, 1)-->(1, 1)-->None)-->None


if __name__ == '__main__':
    main()
