data={
    "name":['Bob','Ram',"Krishna","Rajesh","Naurangi","Sunak","Settewll",],
    "dept":['IT','HR','Manager','HR','Recuirter',"fhp","dg"],
    "salary":[45000,36000,45000,12000,34000,45554,67043]
}
#Fetch Particuler Emp data 

# emp_name=input("enter emp name:")
# index=data["name"].index(emp_name)
# print("name:",emp_name)
# print("dept:",data['dept'][index])
# print('salary:',data["salary"][index])


print("+="*30)

#Total salary of all employee
# sum=0
# for i in range(len(data["name"])):
#     sum+=data["salary"][i]
# print("Total salary.....",sum)


#Find out avg salary of HR Department

# avg_salary=0
# for i in range(len(data["dept"])):
#     if data["dept"][i]=="HR":
#         avg_salary+=data["salary"][i]
#         print("avg_salary..",data["salary"][i],data["name"][i])

#Find out employee with the highest salary


hi_salary=0
for i in range(len(data["name"])):
    if data["name"][i]==data["salary"][i]:
        hi_salary+=max(data["name"],["salary"])
        print("hi_salary...",data["salary"]["name"])

#Find out total salary of employees whose name starts with 'S'

# print("Employees Whose Name Starts With 'S'")
# for i in range(len(data["name"])):
#     if data["name"][i].startswith("S"):
#         print(data["name"][i])

#Print emp name with dept_name and his salary
# empName = input("Enter Emp Name : ")
# index = data["name"].index(empName)
# print(empName,":", data["dept"][index],":",data["salary"][index])
