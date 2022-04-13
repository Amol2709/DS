def check(x,y):
    s=set()
    for j in range(y,COL):
        s.add((x,j))
    for j in range(y,-1,-1):
        s.add((x,j))
    for i in range(x,ROW):
        s.add((i,y))
    for i in range(x,-1,-1):
        s.add((i,y))
    i,j=x,y
    while(i<ROW and j<COL):
        s.add((i,j))
        i=i+1
        j=j+1
    i,j=x,y
    while(i>=0 and j>=0):
        s.add((i,j))
        i=i-1
        j=j-1
    i,j=x,y
    while(i<ROW and j>=0):
        s.add((i,j))
        i=i+1
        j=j-1
    i,j=x,y
    while(i>=0 and j<COL):
        s.add((i,j))
        i=i-1
        j=j+1
    return set(sorted(list(s)))

def func(previous_position,count,X):
    if count==COL:
        #print('amol')
        #print(previous_position)
        y=[]
        for i in range(0,len(previous_position)):
            y.append(previous_position[i])
        ans.append(y)
    #     ans=ans+1
    for row in range(X[0],ROW):
        for col in range(0,COL):
            flag=0
            for i in range(0,len(previous_position)):
                if (row,col) in H[previous_position[i]]:
                    flag=1

            if flag==0:
                previous_position.append((row,col))
                func(previous_position,count+1,(row+1,0))
                previous_position.pop()




            
ans=[]
H={}

ROW,COL=5,5
Ans=0
for i in range(0,ROW):
    for j in range(0,COL):
        H[(i,j)]=check(i,j)
func([],0,(0,0))
Ans={}
# print(ans)

Main_Ans=[]


for i in range(0,len(ans)):
    temp=[]
    for j in range(0,COL):
        Y=['.']*COL
        Y[ans[i][j][1]]='Q'
        a="".join(Y)
        #print(a)
        temp.append(a)
    Main_Ans.append(temp)
print(len(Main_Ans))
print(Main_Ans)


