
#Armstrong number
"""
n=int(input("Enter the number"))


sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if n==sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")

"""
#Count Digit


n=int(input("Enter the number"))
total=0
while(n>0):
    num=n%10
    total=total+num
    n=n//10
    print(total)

#Palindrome number
"""
n=int(input("Enter the number"))
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10
if(n==r):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
    """
