l1=[1,2,3]
l2=[6,4,8]
sum=[]
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            sum=l1[i]+l2[j]
            print(sum)
        else:
            print("error")