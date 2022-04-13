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
        row,col = self.N+1,self.cap+1
        # self.dp = [[-1 for i in range(col)] for j in range(row)]
        self.dp={}
        return self.maxSum(0,self.cap)
    def maxSum(self,index,capacity):
        sum_=0
        #print(index,capacity)
        if (index,capacity) in self.dp:
            return self.dp[(index,capacity)]
        for i in range(index,self.N):
            if capacity-self.weight[i]>=0:
                sum_=max(sum_,self.val[i]+self.maxSum(i+1,capacity-self.weight[i]))
        #self.dp[index][capacity]=sum_
        self.dp[(index,capacity)]=sum_
        return sum_


val=[ 359, 963, 465, 706, 146, 282, 828, 962, 492 ]
weight = [ 96, 43, 28, 37, 92, 5, 3, 54, 93 ]
cap= 383
obj = Solution()
print(obj.solve(val,weight,cap))
