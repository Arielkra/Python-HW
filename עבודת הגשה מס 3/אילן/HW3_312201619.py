'''
ilan tal
312201619
'''
print ("Q1")
'''
Q1
a
(1, 2, 3, 4, 5)
b
(7, 8, 9)
c
(4, 6, 8)
d
(8, 7, 6, 5, 4, 3, 2)
e
(1, 2, 8, 9)
f
(5, 6, 7, 8, 9, 1, 2, 3, 4)
have a array and print the requerments
'''
a=(1,2,3,4,5,6,7,8,9)
print("a")
'''
0 to 4 place
'''
array1=a[0:5]
print(array1)
print("b")
'''
3 last nubers
'''
array2=a[6:9]
print(array2)
print("c")
'''
6 last numbers in even place
'''
array3=a[3:8:2]
print(array3)
print("d")
'''
reverse not last and first
'''
array4=a[-2:-9:-1]
print(array4)
print("e")
'''
2first and 2 last
'''
array5=a[0:2]+a[7:9]
print(array5)
print("f")
'''
middle and right helf and laft helf
'''
array6=a[len(a)//2::]+a[0:len(a)//2]
print(array6)

print ("Q2")
'''
sum of 2 digit numbers

sum of 2 digits numbers are: 4
'''
sum=0
a=(23,-45,1,567,-12,8,164,38)
for i in a:
    if i<100 and i>9 or i<-9 and i>-100:
        sum=sum+i
print("sum of 2 digits numbers are:",sum)

print ("Q3")
'''
return 1 digits 2 digits and 3 digits
(1, 8, 3, 23, 45, 12, 567, 164)
'''
array=(23, 45,1,567,7234,12,8,164,3)
array1=()
array2=()
array3=()
for i in array:
    if i<10:
        array1=array1+(i,)
    elif i<100:
        array2=array2+(i,)
    elif i<1000:
        array3=array3+(i,)
array1=array1+array2+array3
print (array1)

print("Q4")
'''
print all 3 digit prime numbers and 2 same digits
(101, 113, 131, 151, 181, 191, 199, 211, 223, 227, 229, 233, 277, 311, 313, 331, 337, 353, 373, 383, 433, 443, 449, 499, 557, 577, 599, 661, 677, 727, 733, 757, 773, 787, 797, 811, 877, 881, 883, 887, 911, 919, 929, 977, 991, 997)
'''
array=()
for i in range(100,1000):
    flag=1
    for j in range (2,i):
        if i%j==0:
            flag=0
            break
    if flag==1 and (i%10==i//100 or i%10==i//10%10 or i//100==i//10%10) :
        array=array+(i,)
print (array)

print("Q5")
'''
max nuber with uneven digit
Q5
324
'''
array=(121,2468,324,140,76,642,9)
max1=0
for i in array:
    temp=i
    flag=0
    while temp>0:
        if temp%2==1:
            flag=1
            break
        temp=temp//10
    if flag==1 and max1<i:
        max1=i
print (max1)
