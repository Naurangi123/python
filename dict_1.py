data = {
    "names" : ['John','Shawn','Max','Sam','Tom','Nick','Steve'],
    "dept" : ['IT','manager','IT','p_engineer','Admin','marketing','c.owener'],
    "salary" : [23000,60000,34000,35400,67067,25070,56040]
}

# emp_name = input("Enter employee name : ")
# index = data["names"].index(emp_name)
# print("Name :",emp_name)
# print("Dept :",data["dept"][index])
# print("Salary :",data["salary"][index])

# sum = 0
# for i in range(len(data["names"])):
#     sum += data["salary"][i]

# print("Total Salary...",sum)

#Find out total salary of IT Department

T_salary=0
for i in range(len(data["dept"])):
    if data["dept"][i]=="IT":
        T_salary==data.fromkeys("dept","salary")
        print(T_salary)
