# MA214 Assessed Coursework Q1
# Candidate Number: 37443

class Node:
    def __init__(self,val,le,ri,pa):
        self.value = val
        self.left=le
        self.right=ri
        self.parent=pa

    # prints the whole tree below the current node
    def print(self):
        self.printrec(0)

    # recursively prints the values in the tree, indenting by depth
    def printrec(self,depth):
        print("    "*depth,end="") # right amount of indentation
        print(self.value)
        if self.left==None:
            print("    "*(depth+1),"None")
        else:
            self.left.printrec(depth+1)
        if self.right==None:
            print("    "*(depth+1),"None")
        else:
            self.right.printrec(depth+1)

class Item:
    def __init__(self,aroot,p,n):
        self.heap=aroot
        self.previous=p
        self.next=n

class MinHeaplist:
    def __init__(self):
        self.min = None

    # Helper function for insert
    # x is a Node object
    def insert_node(self,x):
        # Create single-element min-heap Item for new Node
        new = Item(x, None, None)
        # Get current head pointer
        head = self.min
        # Check if heaplist is empty
        if head == None:
            new.next = new
            new.previous = new
            self.min = new # Assign head pointer
        else:
            # Get current next item pointed by head
            n = head.next
            # Redraw links - insert new item after head
            head.next, new.previous, new.next, n.previous = new, head, n, new
            # Check if new value is less than current head pointer
            if x.value < head.heap.value:
                self.min = new # Move head pointer
   
    # Helper function for linkheaps and union
    # a, b are Node objects
    # Recursively call MinHeapify to satisfy MinHeap property
    def MinHeapify(self,a,b):
        if a.value <= b.value:
            if a.left == None:
                a.left, b.parent = b, a
            elif a.right == None:
                a.right, b.parent = b, a
            elif a.left.value <= b.value:
                self.MinHeapify(a.left, b)
            else:
                self.MinHeapify(a.right, b)
        else:
            if b.left == None:
                b.left, a.parent = a, b
            elif b.right == None:
                b.right, a.parent = a, b
            elif b.left.value <= a.value:
                self.MinHeapify(a, b.left)
            else:
                self.MinHeapify(a, b.right)

    # x is an integer or Node object
    def insert(self,x):
        if isinstance(x, Node):
            # Call helper function
            self.insert_node(x)
        elif isinstance(x, int):
            # Create Node object for value
            newval = Node(x, None, None, None)
            # Call helper function
            self.insert_node(newval)
        else:
            raise TypeError

    # h1, h2 are Item objects
    def linkheaps(self,h1,h2):
        a = h1.heap
        b = h2.heap
        # Call helper function
        self.MinHeapify(a, b)
        if a.value <= b.value:
            # value of h1 <= value of h2
            # Redraw links - delete h2 from root list
            p, q = h2.previous, h2.next
            p.next, q.previous = q, p
            h2.previous, h2.next = None, None
            return h1 # return pointer to h1
        else:
            # value of h1 > value of h2
            # Redraw links - delete h1 from root list
            p, q = h1.previous, h1.next
            p.next, q.previous = q, p
            h1.previous, h1.next = None, None
            return h2 # return pointer to h2

    def extractMin(self):
        # Current head pointer will be a Minimum 
        # (there may exist children with the same value, or other head pointers with the same value)
        min = self.min
        prev, next = min.previous, min.next
        prev.next = next
        next.previous = prev
        self.min = next
        leftchild = min.heap.left
        rightchild = min.heap.right
        # If there is a left child, move it to the root list
        if leftchild != None:
            self.insert_node(leftchild)
        # If there is a right child, move it to the root list
        if rightchild != None:
            self.insert_node(rightchild)
        temp = next
        # Clean-up min-heaps in the rootlist
        while temp.next != temp:
            # Call linkedheap function
            temp = self.linkheaps(temp, temp.next)
        # New head will be the only node remaining after clean-up
        self.min = temp
        return min.heap.value

    # H is a MinHeapList object
    def union(self,H):
        C_h = self.min
        C_p = self.min.previous
        H_h = H.min
        H_p = H.min.previous
        # Connection both root lists together
        C_p.next, H_h.previous, H_p.next, C_h.previous = H_h, C_p, C_h, H_p
        # Update head pointer
        if H_h.value < C_h.value:
            self.min = H_h

    # node is a Node object, k is an integer
    def decreaseKey(self,node,k):
        p = node.parent
        node.value = k
        # Check if the node is a root node
        if p != None:
            # Verify MinHeap property is not violated, if so break off that part and move to root list
            if k < p.value:
                # Delete child connection
                if p.left == node:
                    p.left = None
                else:
                    p.right = None
            # Delete parent connection   
            node.parent = None
            # Call helper function
            self.insert_node(node)
        else:
            # If after decreasekey this value is less than the current minimum, move the head pointer
            head = self.min
            temp = head.next
            # Find the pointer to the node
            if k < head.heap.value:
                while temp.heap.value != k:
                    temp = temp.next      
                # Update head pointer         
                self.min = temp
    
    def print(self):
        h=self.min
        if h != None:
            print("-----")
            h.heap.print()
            h = h.next
            while h != self.min:
                print("-----")
                h.heap.print()
                h = h.next
            print("-----")

    # # My implementation of print
    # # Print the min-heaplist
    # def print(self):
    #     if self.min == None:
    #         print("Empty min-heaplist")
    #     else:
    #         head = self.min
    #         temp = head.next
    #         print("Min", "Key:",head.heap.value, "Next:", head.next.heap.value, "Previous:", head.previous.heap.value)
    #         self.print_heap(head.heap)
    #         while temp is not head:
    #             print("Key:",temp.heap.value, "Next:", temp.next.heap.value, "Previous:", temp.previous.heap.value)
    #             self.print_heap(temp.heap)
    #             temp = temp.next

    # # Helper function for print
    # def print_heap(self, node, indent=0):
    #     if node.left != None:
    #         print("\t" * (indent+1), "Left child:", node.left.value)
    #         self.print_heap(node.left, indent+1)
    #     else:
    #         print("\t" * (indent+1), "Left child: None")
    #     if node.right != None:
    #         print("\t" * (indent+1), "Right child:", node.right.value)
    #         self.print_heap(node.right, indent+1)
    #     else:
    #         print("\t" * (indent+1), "Right child: None")

# Test - Small Example
if __name__ == '__main__':

    H = MinHeaplist()

    print("Inserting 5")
    H.insert(5)
    print("Inserting 3")
    H.insert(3)
    print("Inserting 7")
    H.insert(7)
    print("Inserting 6")
    H.insert(6)
    H.print()

    print("Extracting ",H.extractMin())

    print("The current min-heaplist:")
    H.print()

    print("Inserting 4")
    H.insert(4)

    print("The current min-heaplist:")
    H.print()

    n=H.min.next.heap.left
    print("Decreasing key",n.value,"to 2")
    H.decreaseKey(n,2)
    H.print()


# Test - Bigger Example
# if __name__ == '__main__':
#     A = MinHeaplist()
#     n14 = Node(14, None, None, None)
#     n16 = Node(16, None, None, n14)
#     n14.left = n16
#     n19 = Node(19, None, None, n16)
#     n16.left = n19
#     n21 = Node(21, None, None, n19)
#     n19.left = n21
#     n15 = Node(15, None, None, n14)
#     n14.right = n15
#     n17 = Node(17, None, None, n15)
#     n15.left = n17
#     n25 = Node(25, None, None, n15)
#     n15.right = n25

#     n3 = Node(3, None, None, None)
#     n4 = Node(4, None, None, n3)
#     n3.left = n4
#     n10 = Node(10, None, None, n4)
#     n4.left = n10
#     n6 = Node(6, None, None, n4)
#     n4.right = n6
#     n7 = Node(7, None, None, n6)
#     n6.left = n7
#     n12 = Node(12, None, None, n3)
#     n3.right = n12

#     n5 = Node(5, None, None, None)
#     n8 = Node(8, None, None, n5)
#     n5.left = n8
#     n13 = Node(13, None, None, n8)
#     n8.right = n13
#     n9 = Node(9, None, None, n5)
#     n5.right = n9
#     n11 = Node(11, None, None, n9)
#     n9.right = n11

#     A.insert(n3)
#     A.insert(n14)
#     A.insert(15)
#     A.insert(n5)
#     A.print()

#     A.linkheaps(A.min, A.min.next.next)
#     A.print()

#     A.extractMin()
#     A.print()

#     A.decreaseKey(n5, 2)
#     A.print()

#     B = MinHeaplist()
#     B.insert(1)
#     A.union(B)
#     A.print()
