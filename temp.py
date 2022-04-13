class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self,A):
        self.A = list(set(A))
    def solve(self):
        #self.A = list(set(A))
        self.A.sort()
        print(self.A)
        odd=[]
        even=[]
        start=0
        end= len(self.A)-1
        while (True):
            if len(odd) !=0 and len(even)!=0:
                break
            else:
                if self.A[start]%2!=0 and len(odd)==0:
                    odd.append(self.A[start])
                elif self.A[end]%2==0 and len(even)==0:
                    even.append(self.A[end])
                elif self.A[end]%2!=0 and  len(even)==0:
                    end = end-1
                elif self.A[start]%2==0 and len(odd)==0:
                    start = start +1
        print(even,odd)
        return even[0]-odd[0]


A=[0,2,9]
obj = Solution(A)
print(obj.solve())