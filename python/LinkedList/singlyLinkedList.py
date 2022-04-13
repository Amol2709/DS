class Node:
	def __init__(self,data):
		self.data = data
		self.next = None




class LinkedList:
	def __init__(self):
		self.head = None
	def insertNode(self,node):
		'''
			Append Node to existing Linked List
		'''
		if self.head == None:
			self.head=node 
		else:
			self.temp = self.head
			while(True):
				if self.temp.next==None:
					break
				else:
					self.temp = self.temp.next
			self.temp.next = node

	def insertNodeFirst(self,node):
		'''
			Insert Node at beginning
		'''
		if self.head !=None:
			self.temp = self.head
			self.head = node 
			self.head.next = self.temp
		else:
			self.head = node


	def insertNodeBetween(self,node,pos):
		self.pos = pos
		self.temp = self.head
		count = 0
		while (True):
			if count == self.pos-1:
				self.temp2 = self.temp.next
				self.temp.next = node
				self.temp.next.next =self.temp2
				break

			self.temp = self.temp.next
			count = count +1

	def deleteNode(self,pos):
		if pos==0:
			self.temp = self.head
			del self.head
			self.head = self.temp.next
		else:
			count = 0
			self.temp = self.head
			while(True):
				if count == pos-1:
					self.temp2 = self.temp.next.next
					node = self.temp.next
					del node
					self.temp.next = self.temp2
					break
					
				count = count+1
				self.temp = self.temp.next
	def deleteLastNode(self):
		self.temp = self.head
		while self.temp.next is not None:
			self.prev = self.temp
			self.temp = self.temp.next

		self.prev.next = None






		

	def printLinkedList(self):
		self.temp = self.head
		while (True):
			if self.head == None:
				print("Linked List is Empty")
			else:
				print(self.temp.data)
				if self.temp.next == None:
					break
				else:
					self.temp = self.temp.next










obj_node= Node("A")
obj_linkedlist = LinkedList()
obj_linkedlist.insertNode(obj_node)

obj_node2 = Node("B")
obj_linkedlist.insertNode(obj_node2)

obj_node3 = Node("C")
obj_linkedlist.insertNode(obj_node3)


obj_node4= Node("D")
obj_linkedlist.insertNode(obj_node4)

obj_node5 = Node("a")
obj_linkedlist.insertNodeFirst(obj_node5)


obj_node6 = Node("b1")
obj_linkedlist.insertNodeBetween(obj_node6,1)




obj_linkedlist.printLinkedList()

obj_linkedlist.deleteNode(0)
print('*'*100)

obj_linkedlist.printLinkedList()
print('*'*100)
obj_linkedlist.deleteLastNode()
obj_linkedlist.printLinkedList()


