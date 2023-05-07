# for table in range(1,11):
#     for table_value in range(1,11):
#         ans=table*table_value
#         print(ans,end=" ")
#     print()
# else:
#     print("Loop is Over")
    
    
#LIST COMPREHENSIVE

cube_list=[]

for i in range(0,10):
    cube_list.append(i**3)
print(cube_list)

# method 2
print('method 2')

print([i**3 for i in range(0,10)])

print('method 3')
cube_list3=[]
for i in range(0,10):
    if i%2==0:
        cube_list3.append(i**3)
        print(cube_list3)
    elif i%3==0:
        cube_list3.append(i**3)
        print(cube_list3)
    else:
        print(" ")
print(cube_list3)