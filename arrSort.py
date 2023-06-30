arr=[10,5,3,2,7,9,6,8,4,1]

arr1=[]
x=0
index=0
for i in range(len(arr)):
    t=arr[i]
    for j in range(len(arr)):
        if t>arr[j]:
            t=arr[j]
            x=j
        
    
            
