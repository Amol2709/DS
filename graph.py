class Solution:
	def adjList(self,N,V,B):
		Adj = [[]for i in range(0,N+1)]
		# for i in range(V):
		# 	u = A[i][0]
		# 	v = A[i][1]
		# 	Adj[u].append(v)
		# 	Adj[v].append(u)
		D={}
		for i in range(0,V):
			if B[i][0] in D:
				D[B[i][0]].append(B[i][1])
			else:
				D[B[i][0]]=[B[i][1]]
			if B[i][1] in D:
				D[B[i][1]].append(B[i][0])
			else:
				D[B[i][1]] = [B[i][0]]
		print(list(D.keys()))
		return D






obj = Solution()
N=5
V=10
B = [[1, 2],[4, 1],[2, 4],[3, 4],[5, 2] ,[1, 3]]
#A=[[1,2],[2,4],[3,1],[4,5],[1,3],[4,2],[3,2],[4,1],[5,3],[3,5]]
print(obj.adjList(N,len(B),B))