# def BubbleSort(L):
# 	count =0
# 	for i in range(0,len(L)-1):
# 		if L[i]>L[i+1]:
# 			temp = L[i]
# 			L[i]=L[i+1]
# 			L[i+1] = temp
# 		else:
# 			count= count+1
# 			if count == len(L)-1:
# 				return L
# 		if i==len(L)-2:
# 			newL= L
# 			ans = BubbleSort(newL)
# 			return ans

# L=[20,15,5,10,-1,0,1]
# ans= BubbleSort(L)
# print(ans)
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        count_=0
        for i in range(0,n-1):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                count_ = count_+1
                if i == n-2:
                    arr=self.bubbleSort(arr,n)
            else:
                if i == n-2 and count_!=0:
                    arr=self.bubbleSort(arr,n)
        if count_==0:
            return arr
        
        return arr


L=[24,18,38,43,14,40,1,54]
obj = Solution()
ans = obj.bubbleSort(L,len(L))
print(ans)


