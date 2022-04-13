import sys
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.coins = sorted(coins,reverse=True)
        self.N= len(coins)
        #self.ans=sys.maxsize
        self.dp=[-1]*(amount+1)
        self.dp[0]=0
        ans=self.func(amount)
        if ans == sys.maxsize:
            return -1
        else:
            #print(self.dp)
            return ans
    def func(self,target):
        if target == 0:
            return 0
        if self.dp[target]!=-1:
            return self.dp[target]
        ans = sys.maxsize
        for coin in self.coins:
            if target-coin>=0:
                ans = min(self.func(target-coin)+1,ans)
        self.dp[target]=ans
        return ans


obj = Solution()
A=[3,7,405,436]
amount=8839
print(obj.coinChange(A,amount))