import sys

class Solution:
	def frog(self,n,h):
		self.h=h
		self.N=n
		self.dp=[-1]*N
		self.cost = sys.maxsize
		return self.func(self.N)

	def func(self,n):
		if n==0:
			return 0
		if self.dp[n]!=-1:
			return self.dp[n]
		self.cost=min(self.cost,abs(self.h[n]-self.h[n-1])+self.func(n-1))
		if n>1:
			self.cost = min(self.cost,abs(self.h[n]-self.h[n-2])+self.func(n-2))
		self.dp[n]=self.cost
		return self.cost

obj=Solution()
N=4
H=[10,30,40,20]
print(obj.frog(N-1,H))

