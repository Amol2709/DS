# class Solution:
# 	def solve(self,N,prices):
# 		self.N=N 
# 		self.prices = prices
# 		return self.maxPrice(0,0,self.N)
# 	def maxPrice(self,index,cost,rod_length):
# 		if index>=self.N:
# 			return cost
# 		if rod_length<=0:
# 			return cost
# 		ans =0
# 		if rod_length-(index+1)>=0:
# 			ans = self.maxPrice(index,cost+self.prices[index],rod_length-(index+1))
# 		ans =max(ans,self.maxPrice(index+1,cost,rod_length))
# 		return ans
class Solution:
	def solve(self,N,prices):
		self.N=N 
		self.prices = prices
		self.dp=[-1]*(self.N+1)
		return self.maxPrice(0,self.N)
	def maxPrice(self,index,rod_length):
		if index>=self.N:
			return 0
		if rod_length<=0:
			return 0
		if self.dp[rod_length]!=-1:
			return self.dp[rod_length]

		ans =0
		if rod_length-(index+1)>=0:
			ans = self.prices[index]+self.maxPrice(index,rod_length-(index+1))
			ans=max(ans,self.maxPrice(index+1,rod_length))
		self.dp[rod_length]=ans
		return ans
N=8
prices = [3,5,8,9,10,17,17,20]
obj = Solution()

print(obj.solve(N,prices))