# Number is Palindrome

n=int (input("Enter the number"))
org=n
h=0
while(n>0):
    r=n%10
    h=h*10+r
    n=n//10
if(org==h):
    print("Number is palindrome")
else:
    print("Nmube is not palindrome")


#Number is  Prime


n=int(input("Enter the number"))

T=False
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            T=True
if T:
    print("Number is not Prime")
else:
    print("Number is Prime")



    
