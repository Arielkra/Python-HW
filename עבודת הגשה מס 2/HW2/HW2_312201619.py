'''
ilan tal
312201619
'''
print ("Q1")
'''
get 2 digits one even one not add count if sum of digit is 11
count: 4
'''
count=0
for i in range (1,10,1):
    for j in range (1,10,1):
        if i%2==0 and j%2==1:
            if i+j==11:
                count=count+1
print ("count:",count)
'''
get 10 number and print the max number with even and uneven digits
enter number number:189
enter number number:97513
enter number number:68428
enter number number:9459
enter number number:3135
enter number number:967
enter number number:121
enter number number:15
enter number number:989
enter number number:2897
max number is: 9459
'''
print ("Q2")
max2=0
for i in range (1,11,1):
    x=int(input("enter number:"))
    temp=x
    even=0
    uneven=0
    while temp>0:
        if temp%2==0:
            even=1
        else:
            uneven=1
        temp=temp//10
    if even==1 and uneven==1 and x>max2:
        max2=x
print ("max number is:",max2)
'''
get numbers and print the count of simatri numbers
enter number:8
enter number:3135
enter number:967
enter number:1234321
enter number:15
enter number:989
enter number:271897
enter number:0
counter: 3
'''
print("Q3")
i=1
counter=0
while i!=0:
    i=int(input("enter number:"))
    temp=i
    updown=0
    while temp!=0:
        updown=updown*10+temp%10
        temp=temp//10
    if updown==i and i!=0:
        counter=counter+1
print ("counter:",counter)  

'''
phibonachi return sum of n numbers
enter number bigger then 2:3
sum: 4
enter number bigger then 2:8
sum: 54
enter number bigger then 2:4
sum: 7
'''
print("Q4")
num1=2
num2=1
num3=1
sum4=4
n=int(input("enter number bigger then 2:"))
if n>2:
    for i in range(3,n,1):
        num3=num2
        num2=num1
        num1=num1+num3
        sum4=sum4+num1
    print("sum:",sum4)
else:
    print("not bigger then 2")

print("Q5")
'''
get uneven number lower then 20 and print dimond
enter odd integer number [1-19]:5
     
    1
   121
  12321
   121
    1
enter odd integer number [1-19]:9
         
        1
       121
      12321
     1234321
    123454321
     1234321
      12321
       121
        1
enter odd integer number [1-19]:19
                   
                  1
                 121
                12321
               1234321
              123454321
             12345654321
            1234567654321
           123456787654321
          12345678987654321
         12345678910987654321
          12345678987654321
           123456787654321
            1234567654321
             12345654321
              123454321
               1234321
                12321
                 121
                  1
'''
n=int(input("enter odd integer number [1-19]:"))
if n%2==1 and n>0 and n<20:
    for i in range (0,(n//2)+1,1):
        for j in range (n,i,-1):
            print(" ", end="")
        for j in range (1,i+1,1):
            print(j, end="")
        for j in range (j-1,0,-1):
            print(j, end="")
        print ()
    for i in range ((n//2)+1,0,-1):
        for j in range (n,i,-1):
            print(" ", end="")
        for j in range (1,i+1,1):
            print(j, end="")
        for j in range (j-1,0,-1):
            print(j, end="")
        print ()
else:
    print("Worng number")
