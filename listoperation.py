#+++++++++++++++++++++=========LIST OPERATION==================+++++++++++++++++++++++++++++
'''
li=[4,1,2,11,3,15,6,7,14,9]
#Method
for i in range(len(li)):
    print(li[i])

# print("  *"*10)

#Method 2
for i in li:
    print(i)

#This sort(built -in function) method Sort the List
li.sort()
print(li)

#User-define functin to sort the the list

for i in range(len(li)):
     for j in range(i+1,len(li)):
        if li[i]>= li[j]:
             li[i],li[j]=li[j],li[i]
             print(li)
#This reverse method reverse the whole List
li.reverse()
print(li)

#This append method the add th eelement at the last index
li.append(43)
print(li)

#This remove method removed the a particuler number
li.remove(4)
print(li)

#Concate the two list
Km=[4,5,7,8,2,3,4,5,67,90]
Na=[12,23,45,67,89,90,76,54,32,21]
cnc=Km+Na
print(cnc)

cnc.sort()
print(cnc)

#Reptition the element present in the list

Re=[12,23,34,56,78,90]
T=Re*5
print(T)
'''

total=0
count=0
while(True):
    inp=input("Enter the number:")
    if inp=='done': break
    value=float(inp)
    total=total+value
    count=count+1
    avarage=total/count
print('avarage',avarage)


#+++++++++++++++++++==========TUPLE OPERATION========================+++++++++++++++++++++++++++++++
#SOrt the list

# li1=(2,5,7,3,4,8,67,45,23,12,34,45,67,89,90,98,76,65,43)
# s=li1.index(12)
# print(s)

#Count the number that's repeated in the list
# li1=(2,5,7,3,4,8,67,45,23,12,34,45,67,89,90,98,76,65,43)
# t=li1.count(45)
# print(t)


#