'''
ilan tal
3212201619
change the list only with :
pop, remove,insert,reverse, sort, index,extend,append
Q1
[1, 2, 3, -5, 4, 2, 6, 2, 7]
1 [2, 3, 4, 2, 6, 2, 7]
[1, 3, 4, 2, 6, 2, 7]
[7, 2, 6, 2, 4, 3, 2, 1, -1, -2, -3]
[1, 2, 2, 2, 3, 4, 6, 7, -1]
'''
print("Q1")
x=[1,2,3,4,2,6,2,7]
x.insert(3,-5)
print(x)
x=[1,2,3,4,2,6,2,7]
num=x.pop(0)
print(num,x)
x=[1,2,3,4,2,6,2,7]
x.pop(1)
print(x)
x=[1,2,3,4,2,6,2,7]
x.reverse()
x.extend([-1,-2,-3])
print(x)
x=[1,2,3,4,2,6,2,7]
x.sort()
x.append(-1)
print(x)
'''
change the list only with[a:b:c]
Q2
[1, 2, 3, 4, 5]
[2, 4, 6, 8]
[8, 6, 4, 2, 1]
[8, 7, 6, 5]
[8, 4, 5, 1]
'''
print("Q2")
x=[1,2,3,4,5,6,7,8]
print(x[0:5:1])
print(x[1:9:2])
print(x[7:0:-2]+x[0:1:1])
print(x[7:3:-1])
print(x[7:2:-4]+x[-4:-9:-4])
'''
cheack the sum of n numbers in start and finish are equal
Q3
enter number:3
True
enter number:5
True
enter number:4
False
'''
print("Q3")
data=[23,-45,1,567,-12,8,164,-193]
sum1=0
sum2=0
n=int(input("enter number:"))
for i in range (0,n,1):
    sum1+=data[i]
    sum2+=data[-i-1]
if sum1==sum2:
    print("True")
else:
    print("False")
'''
Q4
put num on the list after positive number and beforea negitive number
enter number:4
[23, 4, 4, -45, 1, 4, 567, 4, 4, -12, 8, 4, 164, 4, 4, -193]
enter number:18
[23, 18, 18, -45, 1, 18, 567, 18, 18, -12, 8, 18, 164, 18, 18, -193]
'''
print("Q4")
data=[23,-45,1,567,-12,8,164,-193]
n=int(input("enter number:"))
for i in range (0,len(data)*2,2):
    if data[i]>-1:
        data.insert(i+1,n)
    else:
        data.insert(i,n)
print(data)
'''
sort by digit number
Q5
[1, 6, 3, 19, 12, 54, 65, 854, 345, 8000]
data=[854,8000,19, 1, 6, 3, 12, 345, 54, 65]
data1=data
data1.sort() 
print(data1)
'''
print("Q5")
data=[854,8000,19, 1, 6, 3, 12, 345, 54, 65]
data1=[]
count=0
j=1
while (count<len(data)):
    for i in range (0,len(data)):
        if data[i]<10**j and data[i]>=10**(j-1):
            data1.append(data[i])
            count=count+1
    j=j+1
print(data1)
