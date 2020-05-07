#Laboratory 1
#List of group members:
Name:Huang Yanlin   student number:192050222
Name:Lin ningning   student number:192050192

#Laboratory work number:
variant1

#variant description:
Unrolled linked list is a kind of transformation or improvement of linked list. Each node of it is stored by an array. The capacity of node array is fixed. 1. Insert operation: insert the element after finding the position according to the subscript. If the current inserted node array is full, a new node is created, and half of the elements of the current node are moved to the array of the new node, and the element is inserted finally. 2. Delete: delete the element according to the subscript. A node after deleting an element may need its neighbors to merge. Unrolled linked list has the advantages of random access of array and efficient insertion and deletion of linked list.

#synopsis:
mutable version used used list to create a unrolled linked list

In immutable version,we create a new unrolled linked list before modifying each unrolled linked list, and do not change the original linked list

#contribution summary for each group member:
mutable&mutable_test:Lin ningning

immutable&immutable_test:Huang Yanlin


#explanation of taken design decisions and analysis

 We implement the operation of unrolled linked list, so we use list, which is mutable in Python.1. Insert operation: insert the element after finding the position according to the subscript. If the current inserted node array is full, a new node is created, and half of the elements of the current node are moved to the array of the new node, and the element is inserted finally. 2. Delete: delete the element according to the subscript. A node after deleting an element may need its neighbors to merge. Unrolled linked list has the advantages of random access of array and efficient insertion and deletion of linked list.

 In immutable vesion, in order not to change the address of the original unrolled linked list, a new unrolled linked list is reassigned before the operation function of the original unrolled linked list, and then the operation is carried out.

#conclusion and questions:
This is the first time I use loose linked lists. Because the elements in the unrolled linked list are arrays, the unrolled linked list has the advantages of random array access and efficient insertion and deletion of the linked list. At the same time, because each node will carry multiple elements, the node space overhead of unrolled linked list is less. In the two different vesions, because list  is mutable in Python, so we can directly use it to implement unrolled linked list. In the implementation of immutable version, the original unrolled linked list needs to be preserved to avoid modification, so in the specific implementation, a new unrolled linked list is created to store the original unrolled linked list, and then the new linked list is modified. But we are not sure whether such an implementation meets the requirements.
