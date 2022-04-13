class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self):
		self.head = None
	def Push(self,node):
		if self.head == None:
			self.head = node 
		else:
			self.temp = self.head
			while self.temp.next is not None:
				self.temp = self.temp.next
			self.temp.next = node

	def Pop(self):
		if self.head == None:
			print('stack is empty')
		else:
			self.temp = self.head
			while self.temp.next is not None:
				self.prev = self.temp
				self.temp = self.temp.next
			self.prev.next = None
			return self.temp.data

	def printStack(self):
		self.temp = self.head
		while True:
			print(self.temp.data)
			if self.temp.next == None:
				break
			self.temp = self.temp.next








obj_node = Node(1)
obj_stack = Stack()
obj_stack.Push(obj_node)



obj_node2 = Node(2)
obj_stack.Push(obj_node2)

obj_stack.printStack()
print('*'*100)
print(obj_stack.Pop())
print('*'*100)
obj_stack.printStack()


