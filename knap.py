import sys
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        self.wt = wt
        self.val = val
        self.cap = W
        self.N = n
        self.ans=-sys.maxsize
        self.func(0,0,0)
        return self.ans
    def func(self,index,currWt,valsum):
        if index>=self.N:
            self.ans = max(self.ans,valsum)
            return
        for i in range(index,self.N):
            if currWt+self.wt[i]<=self.cap:
                self.func(i+1,currWt+self.wt[i],valsum+self.val[i])
        self.ans=max(self.ans,valsum)


weight=[6,5,6,6,3,7]
val = [5,6,4,6,5,2]
cap= 15
n=6
obj = Solution()
print(obj.knapSack(cap,weight,val,n))
