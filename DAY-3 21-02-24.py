#1
N=int(input())
arr=list(map(int,input().split()))
for i in range(N):
    if arr.count(arr[i])>1:
        print(arr[i])
        break
#2
N=int(input())
arr=list(map(int,input().split()))[:N]
for i in range(N):
    if arr[i] in arr[i+1:]:
        print(arr[i])
        break

N=int(input())
arr=list(map(int,input().split()))[:N]
arr.sort()
for i in range(N):
    if arr[i]==arr[i+1]:
        print(arr[i])
        break
#3
    a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    a=0
elif b>c:
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

#3-2
N=int(input())
arr=list(map(int,input().split()))[:N]
for i in range(N):
    if arr[i] in arr[i+1:]:
        print(arr[i])
        break

N=int(input())
arr=list(map(int,input().split()))[:N]
arr.sort()
for i in range(N):
    if arr[i]==arr[i+1]:
        print(arr[i])
        break
 

N=int(input())
arr=list(map(int,input().split()))[:N]
for i in range a:
    
#approach1
N=int(input())
a=list(map(int,input().split()))[:N]
for i in range(N):
    if a.count(a[i])==1:
        print(a[i])


#approach2
N=int(input())
a=list(map(int,input().split()))[:N]
for i in a:
    if a.count(i)==1:
        print(i,end=' ')
 
#approach1
t=int(input())
for i in range(t):
    N=int(input())
    t1=0
    t2=0
    for j in range(1,N+1):
        if N%j==0:
            if j%2==0:
                t1=t1+1
            else:
                t2=t2+1
    if t1==t2:
        print(1)
    else:
        print(0)

##
t=int(input())
for i in range(t):
    N=int(input())
    fact=[]
    for j in range(1,N+1):
        if N%j==0:
            fact.append(j)
    ef=[]
    of=[]
    for j in fact:
            if j%2==0:
                ef.append(j)
            else:
                of.append(j)
    if len(ef)==len(of):
        print(1)
    else:
        print(0)


#approach1

t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cost=[]
    for j in range(n):
        if(a[j]>=x):
            cost.append(b[j])
    print(sum(cost))


#approach2

t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cost=[]
    for j in a:
        if j>=x:
            z=a.index(j)
            cost.append(b[z])
    print(sum(cost))


#approach3
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    for j in range(n):
        if(a[j]>=x):
            c=c+b[j]
    print(c)


#prime
#approach1

n=int(input())
c=[]
for i in range(1,n+1):
    if n%i==0:
        c.append(i)
if len(c)>2:
    print("not prime ")
else:
    print("prime")



#approach2
n=int(input())
for i in range(2,n+1):
    if n%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break

 
#approach1

n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
d=0
for i in range(n):
    if a[i]>2*b[i]:
        print("alice happy")
        c=c+1
    else:
        print("alice unhappy")
    if b[i]>2*a[i]:
        print("bob happy")
        d=d+1
    else:
        print("bob unhappy")
if c>d:
    print(str(d)+"days happy")
else:
    print(str(c)+"days happy")


#approach2
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    happy=0
    for i in range(n):
        if a[i]<=2*b[i] and b[i]<=2*a[i]:
            happy+=1
    print(happy)


#
              

    
            
        
        
        

             
    

        
        
