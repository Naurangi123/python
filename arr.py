arr=[1,3,2,5,45,78,34,56,89,49,18]

arr1=[]
arr2=[]
arr3=[]

for i in range(len(arr)):
    if arr[i]%3==0:
        arr1.append(arr[i])
        
        print('This is arr1',arr1)
    if arr[i]%5==0:
        arr2.append(arr[i])
        
        print('This is arr2',arr2)
    if arr[i]%3==0 and arr[i]%5==0:
        arr3.append(arr[i])
        
        print('This is arr3',arr3)
    else:
        print("")
        