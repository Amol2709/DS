class Solution:
    def ninjaTraining(self,n, points):
        self.n = n 
        self.points = points
        self.ans  = -1
        self.func(0,-1,0)
        return self.ans

    def func(self,day,prev,curr_sum):
        for i in range(day,self.n):
            for j in range(0,3):
                if j!=prev:
                    self.func(i+1,j,curr_sum+self.points[i][j])
                if j ==2:
                    self.ans = max(self.ans,curr_sum+self.points[i][j])

        self.ans = max(self.ans,curr_sum)

obj = Solution()
n = 3

A=[[10,40,70],[20,50,80],[30,60,90]]
print(obj.ninjaTraining(n,A))
    