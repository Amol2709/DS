class Solution:
	def solve(self,graph):
		self.graph = graph
		self.visited=set()
		self.ans = 0
		self.connected_comp=[]
		self.temp=[]
		self.isCycle=False
		self.dfs(0,-1)
		return self.isCycle
	# def connComp(self):
	# 	for i in self.graph:
	# 		self.temp=[]
	# 		if i  not in self.visited:
	# 			self.dfs(i)
	# 			self.ans = self.ans+1
	# 			self.connected_comp.append(self.temp)
	# 	return self.ans,self.connected_comp
	def dfs(self,source,parent):
		if source not in self.visited:
			# self.temp.append(source)
			self.visited.add(source)
			for neighbour in self.graph[source]:
				if neighbour in self.visited and neighbour !=parent and neighbour!=source:
					self.isCycle = True
				self.dfs(neighbour,source)




graph={
	0:[4,2],
	1:[1,2],
	2:[2,3],
	3:[],
	4:[]
}
obj = Solution()
print(obj.solve(graph))
# print(obj.connComp())