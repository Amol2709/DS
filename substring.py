#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        self.ans=0
        self.s1=S1
        self.s2=S2
        self.n=n
        self.m=m
        self.dp={}
        self.func(0,0)
        return self.ans
    def func(self,index1,index2):
        if index1>=self.n or index2>=self.m:
            return
        if (index1,index2) in self.dp:
            self.ans = self.ans+self.dp[(index,index2)]
            return
        if self.s1[index1]==self.s2[index2]:
            self.ans =self.ans+1
            self.dp[(index1,index2)]=self.ans
            self.func(index1+1,index2+1)
        else:
            self.ans=0
            self.dp[(index1,index2)]=self.ans
            self.func(index1,index2+1)
            self.ans=0
            self.dp[(index1,index2)]=self.ans
            self.func(index1+1,index2)

obj=Solution()
print(obj.longestCommonSubstr('ABCDGH','ACDGHR',6,6))