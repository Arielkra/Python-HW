''' ariel kravizki
ID : 039678024
'''

print("Q1")
count=0
for i in range (1,10,1):
    for j in range (1,10,1):
       if i%2==0 and j%2==1:
           if j+i==11:
              count=count+1
print("count =",count)
'''
Input: (3+8,5+6,7+4,9+2)
Output : 4
'''


print ("Q2")
max1=0
for i in range(1,10,1):
    x=int(input('enter number: '))
    temp=x
    f=0
    g=0
    while temp>0:
        if temp%2==0:
            f=1
        else:
            g=1
        temp=temp//10
    if f==1 and g==1 and x>max1:
        max1=x
print ("max =",max1)             
'''
enter number: 189
enter number: 97513
enter number: 9459
enter number: 3135
enter number: 121
enter number: 989
enter number: 15
enter number: 23
enter number: 19991
max = 9459
'''


print ("Q3")
count1=0
x=1
x=int(input('enter number: '))
while x!=0:
    temp=x
    y=0
    while temp>0:
        y=y*10+temp%10
        temp=temp//10
    if y==x:
        count1=count1+1
    x=int(input('enter number: '))

print ("count =",count1)

'''
enter number: 989
enter number: 1234321
enter number: 8
enter number: 1234
enter number: 12
enter number: 0
count = 3
'''


print("Q4")
z=2
x=1
y=1
sum1=4
n=int(input('enter number: '))
if n>2:
    for i in range(3,n,1):
        x=y
        y=z
        z=z+x
        sum1=sum1+z
    print ("sum =" ,sum1)
else:
    print("Bad")

'''
enter number: 8
sum = 54
'''


print ("Q5")
n=int(input("enter odd integer number [1-19]:"))
if n%2==1 and n>0 and n<20:
 for i in range (0,(n//2)+1,1):
        for j in range(n-i-1):
            print(' ',end='')    
        for j in range(i+1):
            print(j+1,end='')
        for j in range(i-1,-1,-1):
            print(j+1,end='')
        print()
 for i in range ((n//2),0,-1):
        for j in range(n,i,-1):
            print(' ',end='')
        for j in range(1,i+1,1):
            print(j,end='')
        for j in range(j-1,0,-1):
            print(j,end='')
        print()
else:
    print("Error number")

    '''
enter odd integer number [1-19]:7
      1
     121
    12321
   1234321
    12321
     121
      1
      '''
'''
enter odd integer number [1-19]:15
              1
             121
            12321
           1234321
          123454321
         12345654321
        1234567654321
       123456787654321
        1234567654321
         12345654321
          123454321
           1234321
            12321
             121
              1
'''
    


