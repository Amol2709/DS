class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Linked_List:
	def __init__(self):
		self.head = None

	def insert_node(self,node):
		if self.head == None:
			self.head = node
		else:
			self.temp = self.head
			while (True):
				if self.temp.next == None:
					self.temp.next = node
					break
				else:
					self.temp = self.temp.next



	def insert_node_first(self,node):
		if self.head == None:
			self.head = node
		else:
			self.temp = self.head
			self.head = node 
			self.head.next = self.temp


	def insert_node_inbetween(self,node,pos):
		if pos == 0:
			pass
		else:
			self.temp = self.head
			count = 0
			while (True):
				if count == pos-1:
					break
				else:
					count = count+1
					self.temp = self.temp.next
			# print('*')
			# print(self.temp.data)

			# self.temp2 = self.temp.next.next
			# self.temp.next = self.temp2
			self.temp2 = self.temp
			self.temp.next = node 
			self.temp.next.next = self.temp2.next
			print('amol')
			print(self.temp.data)





	def delete_node(self,pos):
		if pos == 0:
			#self.temp = self.head
			self.head = self.head.next
		else:
			self.temp = self.head
			count = 0
			while (True):
				if count == pos-1:
					break
				else:
					count = count+1
					self.temp = self.temp.next
			# print('*')
			# print(self.temp.data)

			self.temp2 = self.temp.next.next
			self.temp.next = self.temp2






		



	def print_linked_list(self):
		if self.head == None:
			print("Linked List is Empty")
		else:
			self.temp = self.head
			while (True):
				if self.temp == None:
					break
				else:
					print(self.temp.data)
					self.temp = self.temp.next









node_1 = Node(0)
obj_linked_list = Linked_List()
obj_linked_list.insert_node(node_1)

node_1 = Node(1)
obj_linked_list.insert_node(node_1)

node_1 = Node(2)
obj_linked_list.insert_node(node_1)

node_1 = Node(3)
obj_linked_list.insert_node(node_1)

node_1 = Node(-1)
obj_linked_list.insert_node_first(node_1)

node_1 = Node(-2)
obj_linked_list.insert_node_first(node_1)

obj_linked_list.print_linked_list()


print('*****')
obj_linked_list.delete_node(2)

print('******')
obj_linked_list.print_linked_list()


obj_linked_list.delete_node(0)

print('******')
obj_linked_list.print_linked_list()


node_1 = Node(0)
obj_linked_list.insert_node_inbetween(node_1,2)

# print('******')
# obj_linked_list.print_linked_list()



# 0  1  2  3  4 5
# -2 -1 0  1  2 3