import math
def BinarySearch(L,low,high,number):
	mid = math.floor((low+high)/2)
	if mid<len(L) :
		if L[mid]==number:
			return mid
		elif L[mid]>number:
			ans=BinarySearch(L,low,mid-1,number)
			return ans	
		elif L[mid]<number:
			ans= BinarySearch(L,mid+1,high,number)
			return ans
	else:
		return -1


L=[1,2,5,9,11,12,16,32]
ans=BinarySearch(L,0,len(L),32)
print(ans)


