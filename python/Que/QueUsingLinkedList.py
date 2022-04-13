class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class Que:
	def __init__(self):
		self.head = None
	def Enque(self,node):
		if self.head == None:
			self.head = node 
		else:
			self.temp = self.head
			self.head = node 
			self.head.next = self.temp
	def Deque(self):
		self.temp = self.head
		while True:
			if self.temp.next == None:
				break
			self.prev = self.temp
			self.temp = self.temp.next
		self.prev.next = None
		return self.temp.data

	def printQue(self):
		self.temp = self.head
		while True:
			print(self.temp.data)
			if self.temp.next == None:
				break
			self.temp = self.temp.next




obj_node = Node(1)
obj_que = Que()
obj_que.Enque(obj_node)

obj_node2= Node(2)
obj_que.Enque(obj_node2)

obj_que.printQue()
print('*'*100)
print(obj_que.Deque())
print('*'*100)
obj_que.printQue()