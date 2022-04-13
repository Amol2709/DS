def InsertionSort(L):
	for i in range(0,len(L)-1):
		if L[i]>L[i+1]:
			temp = L[i]
			L[i] = L[i+1]
			L[i+1] = temp

			ans = InsertionSort(L[:i+2])
			for i in range(0,len(ans)):
				L[i] = ans[i]
		else:
			if i == len(L)-2:
				return L 
			else:
				pass
	return L


#L=[1,0,2]
L=[0,-1,100,23,10]
ans=InsertionSort(L)
print(ans)