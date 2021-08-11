
print("Q1")
x=[1,2,3,4,2,6,2,7]
x.insert(3,-5)
print(x)

x=[1,2,3,4,2,6,2,7]
num=x.pop(0)
print(num,x)

x=[1,2,3,4,2,6,2,7]
x.remove (2,)
print(x)

x=[1,2,3,4,2,6,2,7]
x.reverse()
x.extend([-1,-2,-3])
print(x)

x=[1,2,3,4,2,6,2,7]
x.sort()
x.extend([-1])
print(x)
'''
[1, 2, 3, -5, 4, 2, 6, 2, 7]
1 [2, 3, 4, 2, 6, 2, 7]
[1, 3, 4, 2, 6, 2, 7]
[7, 2, 6, 2, 4, 3, 2, 1, -1, -2, -3]
[1, 2, 2, 2, 3, 4, 6, 7, -1]
'''



print("Q2")
x=[1,2,3,4,5,6,7,8]
print(x[0:5:1])
print(x[1:8:2])
print(x[7:0:-2]+x[0:1:1])
print(x[7:3:-1])
print(x[7:2:-4]+x[4:-9:-4])
'''
[1, 2, 3, 4, 5]
[2, 4, 6, 8]
[8, 6, 4, 2, 1]
[8, 7, 6, 5]
[8, 4, 5, 1]
'''



print("Q3")
data=[23,-45,1,567,-12,8,164,-193]
sum1=0
sum2=0
n=int(input("enter number:"))
for i in range (0,n,1):
    sum1=sum1+data[i]
    sum2=sum2+data[-i-1]
if sum1==sum2:
    print("True")
else:
    print("False")

'''
enter number:3
True
enter number:5
True
enter number:4
False
'''



print("Q4")
data=[23,-12,33,-44,1,5,-77]
n=int(input("enter number:"))
for i in range (0,len(data)*2,2):
    if data[i]>-1:
        data.insert(i+1,n)
    else:
            data.insert(i,n)
print(data)

'''
put num on the list after positive number and beforea negitive number
enter number:4
[23, 4, 4, -12, 33, 4, 4, -44, 1, 4, 5, 4, 4, -77]
'''


print("Q5")
data=[854,8000,19, 1, 6, 3, 12, 345, 54, 65]
data2=[]
count=0
f=1
while (count<len(data)):
    for i in range(0,len(data)):
        if data[i]<10**f and data[i]>=10**(f-1):
           data2.append(data[i])
           count=count+1
    f=f+1
print(data2)

'''
data=[854,8000,19, 1, 6, 3, 12, 345, 54, 65]
[1, 6, 3, 19, 12, 54, 65, 854, 345, 8000]
'''

            


    
    











      
