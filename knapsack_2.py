import sys
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        import sys
        self.val= A 
        self.weight = B
        self.N=len(A)
        self.cap = C 
        self.ans = -sys.maxsize
        self.val2=list(range(0,sum(self.val)+1))
        len_=len(self.val2)
        row,col = len_,sum(self.val)+1
        self.dp = [[-1 for i in range(col)] for j in range(row)]
        for value in range(len_-1,-1,-1):
        	if self.maxSum(self.val2[value],0)<=self.cap:
        		return value
    def maxSum(self,capacity,index):
    	if capacity==0:
    		return 0
    	if index>=self.N:
    		return sys.maxsize
    	if self.dp[index][capacity]!=-1:
    		return self.dp[index][capacity]
    	sum_=sys.maxsize
    	if self.val[index]<=capacity:
    		sum_=min(sum_,self.weight[index] +self.maxSum(capacity-self.val[index],index+1))
    	sum_=min(sum_,self.maxSum(capacity,index+1))
    	self.dp[index][capacity]=sum_
    	return sum_



        


# val=[ 359, 963, 465, 706, 146, 282, 828, 962, 492 ]
# weight = [ 96, 43, 28, 37, 92, 5, 3, 54, 93 ]
# cap= 383
val = [ 6, 1, 3, 9, 7, 1, 3, 5, 9, 7, 6, 1, 10, 1, 1, 7, 2 ]
weight=[44, 49, 30, 24, 35, 5, 7, 41, 17, 27, 32, 9, 45, 40, 27, 24, 38 ]
cap= 297
# print(sum(val))
# val=[6, 10, 12]
# weight = [10, 20, 30]
# cap= 50
obj = Solution()
print(obj.solve(val,weight,cap))
