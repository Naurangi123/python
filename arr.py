arr=[12,34,3,3,5,67,89,45,65,9,12,34,56,7,45,34,90]

arr1=[]
arr2=[]
arr3=[]

for i in arr:
    if arr[i+1]%3==0:
        arr.append(arr1)
        print(arr1)
    elif arr[i+1]%5==0:
        arr.append(arr2)
        print(arr2)
    elif arr[i+1]%3==0 or arr[i+1]%5==0:
        arr.append(arr3)
        print(arr3)
    else:
        print(arr)
        