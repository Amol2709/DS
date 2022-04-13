class Node:
	def __init__(self,data):
		self.left = None
		self.data = data
		self.right = None



class BTree:
	def createNode(self,data):
		return Node(data)

	def insertNode(self,node,data):
		if node==None:
			return self.createNode(data)
		if node.data > data:
			node.left = self.insertNode(node.left,data)
		else:
			node.right = self.insertNode(node.right,data)
		return node


	def printTreeInorder(self,node):
		if node !=None:
			self.printTreeInorder(node.left)
			print(node.data)
			self.printTreeInorder(node.right)

	











obj = BTree()
root = obj.createNode(5)

obj.insertNode(root,2)
obj.insertNode(root,10)
obj.insertNode(root,7)
obj.insertNode(root,6)


obj.printTreeInorder(root)