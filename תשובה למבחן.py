x = [1,2,3,4,5,6,7]
x.insert( 2, 10 )
x.remove( 2 )
print( x[ :4] )

data = (123,242,8,56763,3773,934,171)
c = 0
for n in data:
    nm, t = 0, n
    while t > 0:
        nm = nm*10 + t%10
        t = t //10
    if n == nm:
        c = c + 1
print(c)


data = [8,23,6754,171,123456,7,15,15713]
nd = [ ]
for n in data:
    c,t=0,n
    while t>0:
        c=c+1
        t=t//10
    if c%2==0:
        nd.insert(0,n)
    else:
        nd.append(n)
print(nd)

nt = ( )
for n in range(10,30):
    t, f = 2,True
    while t < n:
        if n % t == 0:
            f = False
        t = t + 1
    if f == True:
        nt = nt + (n, )
print( nt )

