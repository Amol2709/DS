class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)
        count = 0
        ans = 0
        
        dp=[[0 for j in range(0,m+1)]for i in range(0,n+1)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                    ans=max(ans,dp[i][j])
                else:
                    # count=0
                    dp[i][j]=0
        print(dp)
        return ans

obj = Solution()
S1="ABCDGH"
S2 = "ACDGHR"
n = len(S1)
m = len(S2)
print(obj.longestCommonSubsequence(S1,S2))