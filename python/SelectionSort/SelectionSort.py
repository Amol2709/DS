def SelectionSort(L):
	
	for i in range(0,len(L)-1):
		#temp=L[i:]
		#print(temp)
		min_=L[i]
		index_=i
		for j in range(0,len(L[i:])):
			if min_<=L[i:][j]:
				min_ = min_
			else:
				min_ = L[i:][j]
				index_=L.index(min_)
		var_ = L[i]
		L[i] = L[index_]
		L[index_]=var_
		print(L)
	return L 


L=[1,6,0,-32,-3,100]
ans=SelectionSort(L)
print(ans)
