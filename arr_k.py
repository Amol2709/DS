class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
		stk=[]
		count = 0
		Ans=[]
		for i in range(0,N):
			stk.append(arr[i])
			count=count+1
			if count ==K:
				while(len(stk)!=0):
					Ans.append(stk.pop())
				count=0
		while(len(stk)!=0):
			Ans.append(stk.pop())
		return Ans
obj = Solution()
print(obj.reverseInGroups([1,2,3,4,5],5,3))