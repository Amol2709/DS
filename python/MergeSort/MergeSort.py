######### Given two sorted array as input program to print element in sorted order
############ [Merge Sort basic]

class MergeSort:
	def __init__(self,LIST):
		self.LIST= LIST 

	def MS(self):
		var = 2 
		while (True):
			var2 = int(var/2)
			for i in range(0,len(self.LIST),var):
				if i+(var2*2)>= len(self.LIST):
					#print('$')
					#print(self.LIST[i:i+var2],self.LIST[i+var2:len(self.LIST)])
					ANS_=self.FUNC(self.LIST[i:i+var2],self.LIST[i+var2:len(self.LIST)])
					if i+var>=len(self.LIST):
						count=0
						for j in range(i,len(self.LIST)):
							self.LIST[j] = ANS_[count]
							count = count+1
						
					else:
						count = 0
						for j in range(i,var):
							self.LIST[j] = ANS_[count]
							count= count+1

				else:
					ANS_=self.FUNC(self.LIST[i:i+var2],self.LIST[i+var2:i+(var2*2)])
					count = 0
					if i+var>=len(self.LIST):
						for j in range(i,len(self.LIST)):
							self.LIST[j] = ANS_[count]
							count = count+1
						
					else:
						count = 0
						for j in range(i,var):
							self.LIST[j] = ANS_[count]
							count = count+1
			if var>=len(self.LIST):
				return self.LIST
				break
			print('#'*100)
			print(self.LIST)
			var = var*2





	def FUNC(self,temp1,temp2):
		ANS=[]
		if len(temp1)>=len(temp2):
			L1 = temp1
			L2 = temp2
		else:
			L1= temp2
			L2 = temp1
		count_1=0
		count_2=0


		while(True):
			if count_2== len(L2) and count_1 == len(L1):
				break
			elif count_1==len(L1):
				for j in range(count_2,len(L2)):
					ANS.append(L2[j])
					print(L2[j])
				count_2 = len(L2)
			elif count_2 == len(L2):
			 	for j in range(count_1,len(L1)):
			 		ANS.append(L1[j])
			 		print(L1[j])
			 	count_1 = len(L1)

			else:
				if L1[count_1]>L2[count_2]:
					ANS.append(L2[count_2])
					print(L2[count_2])
					count_2 = count_2 +1
				elif L1[count_1]<L2[count_2]:
					ANS.append(L1[count_1])
					print(L1[count_1])
					count_1 = count_1+1
				elif L1[count_1]==L2[count_2]:
					ANS.append(L1[count_1])
					ANS.append(L1[count_1])
					print(L1[count_1])
					print(L1[count_1])
					count_1 = count_1+1
					count_2 = count_2+1
		return ANS



L1 = [6,25,0,2,-1,6,6]


obj = MergeSort(L1)
ans_ = obj.MS()
print('*'*100)
print('ANS:{}'.format(ans_))


