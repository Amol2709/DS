class Solution(object):
    def nextGreaterElement(self, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n1=len(nums2)
        nums2= nums2+nums2
        nge=[-1]*len(nums2)
        stk=[]
        isempty = True
        n2 = len(nums2)
        for i in range(n2-1,-1,-1):
            if isempty == True:
                nge[i]=-1
                stk.append(nums2[i])
                isempty = False
            elif stk[-1]>nums2[i]:
                nge[i]=stk[-1]
                stk.append(nums2[i])
            else:
                while(True):
                    temp = stk.pop()
                    if temp>nums2[i]:
                        nge[i]=temp
                        stk.append(temp)
                        stk.append(nums2[i])
                        break
                    if len(stk)==0:
                        nge[i]=-1
                        stk.append(nums2[i])
                        break
        return nge[0:n1]



obj = Solution()
nums2=[3,10,4,2,1,2,6,1,7,2,9]
print(obj.nextGreaterElement(nums2))