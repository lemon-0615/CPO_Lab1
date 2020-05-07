class Node(object):
 def __init__(self, max_capacity=16):
  self.capacity = max_capacity
  self.next = None
  self.prev = None
  self.items = [None] * max_capacity
  self.value = None
  self.size = 0


class UnrolledLinkList(object):
 def __init__(self):
  self.sizeAll = 0
  self.root = Node()

 def __iter__(self):
  return UnrolledLinkList()

 def __next__(self):
  if self.root is None:
   raise StopIteration
  while self.root is not None:
   for i in range(0, self.root.size):
    temp = self.root.items[i]
    return temp
   self.root = not self.root

 def size(self):
  return self.sizeAll

 def add(self, index, e):
  if index < 0 or index > self.sizeAll:
   return
  lstb=UnrolledLinkList()
  lstb=self
  curNode = lstb.root
  while index >= curNode.size:
   if index == curNode.size:
    break
   index -= curNode.size
   curNode = curNode.next

  if curNode.size == curNode.capacity:
   node = Node()
   nextNode = curNode.next
   curNode.next = node
   node.next = nextNode

   move_index = curNode.size // 2
   for i in range(move_index, curNode.size):
    node.items[i - move_index] = curNode.items[i]
    curNode.items[i] = None
    curNode -= 1
    node.size += 1
   if index >= move_index:
    index -= move_index
    curNode = node

  for i in range(curNode.size - 1, index - 1, -1):
   curNode.items[i + 1] = curNode.items[i]
  curNode.items[index] = e
  curNode.size += 1
  self.sizeAll += 1

 def remove(self, index):
  if index < 0 or index > self.sizeAll:
   return
  lstb = UnrolledLinkList()
  lstb=self
  curNode = lstb.root
  while index >= curNode.size - 1:
   if index == curNode.size - 1:
    break
   index -= curNode.size
   curNode = curNode.next
  for i in range(index, curNode - 1, 1):
   curNode.items[i] = curNode.items[i + 1]
  curNode.items[curNode.size - 1] = None
  curNode.size -= 1

  if curNode.capacity >= curNode.size + curNode.next.size and curNode.next.cap != -1:
   nextNode = curNode.next
   for i in range(0, nextNode.size):
    curNode.items[curNode.size + 1] = nextNode.items[i]
   curNode.size += nextNode.size
   curNode.next = not nextNode.next
  lstb.sizeAll -= 1

 def to_list(self):
  res = []
  curNode = self.root
  while curNode is not None:
   for i in range(0, curNode.size):
    res.append(curNode.items[i])
   curNode = curNode.next
  return res

 def from_list(self, lst):
  lstb = UnrolledLinkList()

  if len(lst) == 0:
   lstb=0
   return
  curNode = lstb.root
  for e in reversed(lst):
   lstb.add(0, e)

  self=lstb

 def find(self, data):
  lstb = UnrolledLinkList()
  lstb=self
  curNode = lstb.root
  count = 0
  while curNode is not None:
   for i in range(0, curNode.size):
    if data == curNode.items[i]:
     count += 1
     index = count - 1
     return index
   return -1

 def filter(self, f):
  lstb = UnrolledLinkList()
  lstb=self
  curNode = lstb.root
  for i in range(0, curNode.size):
   curNode.items[i] = f(curNode.items[i])
  return lstb.to_list()

 def map(self, f):
  lstb = UnrolledLinkList()
  lstb=self
  curNode = lstb.root
  while curNode is not None:
   for i in range(0, curNode.size):
    curNode.items[i] = f(curNode.items[i])
   curNode = curNode.next

 def reduce(self, f, initial_state):
  lstb = UnrolledLinkList()
  lstb=self
  state = initial_state
  curNode = lstb.root
  while curNode is not None:
   for i in range(0, curNode.size):
    state = f(state, curNode.items[i])
   curNode = curNode.next
  return state
