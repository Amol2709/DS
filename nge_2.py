class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N=len(A)
        nse = [N]*N 
        pse = [-1]*N 
        # stk = [N-1]
        # for i in range(N-2,-1,-1):
        #     if len(stk)!=0:
        #         if A[i]>A[stk[-1]]:
        #             nse[i]=stk[-1]
        #             stk.append(i)
        #         else:
        #             while(True):
        #                 if len(stk)==0:
        #                     stk.append(i)
        #                     break
        #                 if A[i]>A[stk[-1]]:
        #                     nse[i] = stk[-1]
        #                     stk.append(i)
        #                     break
        #                 else:
        #                     stk.pop()
        #     else:
        #         stk.append(i)
        # return nse
        stk=[0]
        for i in range(1,N):
            if len(stk)!=0:
                if A[i]>A[stk[-1]]:
                    pse[i]=stk[-1]
                    stk.append(i)
                else:
                    while(True):
                        if len(stk)==0:
                            stk.append(i)
                            break
                        if A[i]>A[stk[-1]]:
                            pse[i] = stk[-1]
                            stk.append(i)
                            break
                        else:
                            stk.pop()
            else:
                stk.append(i)
        return pse
obj = Solution()
print(obj.solve([4,7,3,8]))