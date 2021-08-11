'''Ariel Kravizki
39678024
work 1 py'''

print("Q1")

x=int (input("Enter 5 Numbers:"))
a1=x//10000
a2=x//1000%10
a3=x//100%10
a4=x//10%10
a5=x%10
sum1=int(0)
if x>9999 and x<100000:
    if a1%2==0:
        print(a1)
    else:
        sum1+=a1
    if a2%2==0:
        print(a2)
    else:
        sum1+=a2
    if a3%2==0:
        print(a3)
    else:
        sum1+=a3
    if a4%2==0:
        print(a4)
    else:
        sum1+=a4
    if a5%2==0:
        print(a5)
    else:
        sum1+=a5
        

print (sum1)
    

'''
Enter 5 Numbers:12345
מציג בהצלחה רק את המספרים הזוגיים 
בסוף סכום של מספרים אי זוגיים
'''

print("Q2")
a=float (input("Enter float number 1:"))
b=float (input("Enter float number 2:"))
c=float (input("Enter float number 3:"))
d=float (input("Enter float number 4:"))
max1=float(a)
if (max1<b):
    max1=b
if (max1<c):
    max1=c
if (max1<d):
    max1=d

print(max1)
''' הכנס 4 מספרים ממשיים כך שתוכנית תדפיס מספר הכי גבוה
enter number 1: 80
enter number 2:40
enter number 3:-4
enter number 4:4

max: 80
'''

print("Q3")
x=int (input("enter New password number:"))
if x>999 and x<10000:
    a1=x//1000
    a2=x//100%10
    a3=x//10%10
    a4=x%10
    sum1=a1+a2+a3+a4
    if sum1>9:
        if a4!=a3 and a4!=a2 and a4!=a1 and a3!=a2 and a3!=a1 and a2!=a1:
            if a4%2==1 or a3%2==1 or a2%2==1 or a1%2==1:
                if a4%2==0 or a3%2==0 or a2%2==0 or a1%2==0:
                    print("Ok Password")
            else:
                    print("all numbers are uneven not pass")
        else:
                print("all numbers are even! not pass")
    else:
            print("same digits in the pass! not pass")

else:
        print("sum its not Double digit! not pass")
        
'''get 4 digin number and chack the requerments
enter password number:2245
all numbers are even! not pass
enter password number:2245
Ok Password
'''

print("Q4")
x=int (input ("Enter numbers:"))
if x>-1 and x<101:
    if x>95:
        print(x,"100")       
    elif x<95 and x>86:
        print(x,x+4,"4")
    elif x<85 and x>55:
        print(x,x+6,"6")
    elif x<=55:
        print("Non Factor")
else:
    print("no number")

'''
Enter numbers:78
Score : 78
Factor: 6
Final score : 84
'''

print("Q5")
kg=float (input ("Enter your weight:"))
h=float (input ("Enter yor height:"))
bmi=kg//(h)**2
if kg//(h)**2<17:
    print("תת משקל")
if kg//(h)**2<25 and kg//(h)**2>17:
    print ("משקל בריא")
if kg//(h)**2<30 and kg//(h)**2>25:
    print ("עודף משקל")
if kg//(h)**2<35 and kg//(h)**2>30:
    print ("השמנה")
if kg//(h)**2<44 and kg//(h)**2>35:
    print ("השמנת יתר")
if kg//(h)**2>44:
    print ("השמנת יתר חמורה")
'''
Enter your weight:80
Enter yor height:1.65
עודף משקל
Enter your weight:83
Enter yor height:1.83
משקל בריא
'''

















        

            
