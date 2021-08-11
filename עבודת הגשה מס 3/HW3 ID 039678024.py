'''ariel Kravizki
ID 039678024
'''


print("Q1")
print()
a=(1,2,3,4,5,6,7,8,9)
array1=a[:5]
print(array1)
print()
array2=a[6:9]
print(array2)
print()
array3=a[3::2]
print(array3)
print()
array4=a[-2:-9:-1]
print(array4)
print()
array5=a[0:2]+a[7:9]
print(array5)
print()
array5=a[4:9]+a[:5]
print(array5)
print()
'''
(1, 2, 3, 4, 5)

(7, 8, 9)

(4, 6, 8)

(8, 7, 6, 5, 4, 3, 2)

(1, 2, 8, 9)

(5, 6, 7, 8, 9, 1, 2, 3, 4, 5)
'''


print("Q2")
x=(23,-100,84,3,43,32,500,121,55)
sum=0
for i in x:
    if i>9 and i<100 or i<-9 and i>-100:
        sum=sum+i
print("Only the sum of the odd numbers = ",sum)

'''
Only the sum of the odd numbers =  237
'''

print("Q3")
x=(24,400,44,1,3,53,200,78,9)
array1=()
array2=()
array3=()
for i in x:
    if i<10:
        array1=array1+(i,)
    elif i>9 and i<100:
            array2=array2+(i,)
    elif i>99 and i<1000:
        array3=array3+(i,)
array1=array1+array2+array3
print(array1)

'''
(1, 3, 9, 24, 44, 53, 78, 400, 200)
'''

print("Q4")
x=()
for i in range(100,1000):
    flag=1
    for j in range(2,i):
        if i%j==0:
            flag=0
    if flag==1:
        if i//100==i%10 or i%10==i%100//10 or i//100==i%100//10:
            x+=(i,)
    
print(x)
'''
(101, 113, 131, 151, 181, 191, 199, 211, 223, 227, 229, 233, 277, 311, 313, 331, 337, 353, 373, 383, 433, 443, 449, 499, 557, 577, 599, 661, 677, 727, 733, 757, 773, 787, 797, 811, 877, 881, 883, 887, 911, 919, 929, 977, 991, 997)
'''

print("Q5")
x=(21,2468,324,140,76,642,9)
max1=0
for i in x:
    flag=0
    temp=i
    while temp!=0:
        if temp%2==1:
            flag=1
        temp=temp//10
    if flag==1 and max1<i:
        max1=i
print(max1)

'''
324
'''

    




















