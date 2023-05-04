"""Square Pattern
*****
*****
*****
*****
*****
"""
'''

for i in range(5):
    for j in range(5):
        print("*",end="")
    print()
    


print("=="*10)

"""
*
**
***
****
*****
******
"""

for i in range(6):
    for j in range(i+1):
        print("*",end=" ")
    print()

print("=="*10)
'''
"""
*****
****
***
**
*
"""
'''
for i in range(6):
    for j in range(6,i,-1):
        print(" *",end="")
    print()

print("=="*10)
"""
*
**
***
****
*****
******
*****
****
***
**
*
"""
for i in range(6):
    for j in range(i+1):
        print("",end="*")
    print()
k=0
for i in range(6):
    for j in range(6,i,-1):
        k+=1
        print("*",end="")
    print()

print("=="*10)
"""
    *
   **
  ***
 ****
*****
k=0
for i in range(0,5):
    for j in range(1,5-i):
        print(" ",end="")
        k+=1
    print("*")
    
                    *
                   * *
                 * * * *
               * * * * * *
             * * * * * * * *
           * * * * * * * * * *
         * * * * * * * * * * * *
       * * * * * * * * * * * * * *
     * * * * * * * * * * * * * * * *
   * * * * * * * * * * * * * * * * * *
   """

for i in range(10):
    for j in range(10-i):
        print(" ",end=" ")
    print(" *" * (2 * i))
    '''

'''
       *******
      *      
     *      
    *      
   *      
  *      
 *******
'''
'''
rows=int(input("enter the number"))
for i in range(rows):
    for j in range(rows-i):
        print(" ",end="")
    for j in range(rows):
        if i==0 or i==rows-1 or j==0 or j==rows+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    ********
     *     
      *    
       *   
        *  
         * 
          *
    ********
    '''
"""
rows=8
for i in range(rows):
    for j in range(rows-1):
        print(" ",end="")
    for j in range(rows):
        if i==0 or i==rows-1:
            print("*",end="")
        elif i==j-1 or i>=rows:
            print("*",end="")
        else:
            print(" ",end="")
        print("",end="")
    print()
"""
rows=7
for i in range(rows):
    for j in range(rows):
        print("*",end="")
    print()