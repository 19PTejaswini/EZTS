#problm1
#approach1

s=input()
for i in range(len(s)):
    if i%2!=0:
        print(s[i],end='')
for i in range(len(s)):
    if i%2==0:
        print(s[i],end='')



#approach2

s=input()
es=''
os=''
for i in range(len(s)):
    if i%2==0:
        es=es+s[i]
    else:
        os=os+s[i]
print(os+es)

#pb2
#approach1

S=input()
ch=input()
c=0
for i in range(len(S)):
    if i%2==0:
        if ch in S[i]:
            c=c+1
print(c)
 

S=input()
ch=input()
c=0
for i in range(len(S)):
    if ch in S[i]:
        c=c+1
print(c)

#pb3
#approach1

s=input()
k='aeiouAEIOU'
c=0
for i in range(len(s)):
    if s[i] in k:
        c=c+1
if c==len(s):
    print("Yes")
else:
    print("No")



#approach2
s=input()
k='aeiouAEIOU'
c=0
for i in range(len(s)):
    if s[i] not in k:
        c=c+1
if c==0:
    print("Yes")
else:
    print("No")

#approach3
s=input()
k='aeiouAEIOU'
for i in s:
    if i not in k:
        print("No")
        break
else:
    print("Yes")


#pb4
#approach1
s=input()
k='0123456789'
for i in s:
    if i not in k:
        print("No")
        break
else:
    print("Yes")


#approach2
s=input()
k='0123456789'
c=0
for i in range(len(s)):
    if s[i] in k:
        c=c+1
if c==len(s):
    print("Yes")
else:
    print("No")

#approach3
s=input()
if s.isdigit()==True:
    print("Yes")
else:
    print("No")
#pb5
#approach1
s=input()
k='aeiouAEIOU'
t='qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
c=0
d=0
for i in s:
    if i in k:
        c=c+1
    if i in t:
        d=d+1
print(c,' ',d)
       

#approach2
s=input()
k='aeiou'
t='qwrtypsdfghjklzxcvbnm'
s=s.lower()
c=0
d=0
for i in s:
    if i in k:
        c=c+1
    elif i in t:
        d=d+1
print(c,' ',d) 
 
#aproach3
s=input()
k='aeiouAEIOU'
cc=0
vc=0
for i in s:
    if i.isalpha():
        if i in k:
            cc=cc+1
        else:
            vc=vc+1
print(vc,cc)



#pb7
###
s=input()
c=1
for i in range(len(s)):
    if s[i]==s[i+1]:
        c=c+1
        print(s[i+1],c,'')
    else:
        i=i+1
 
 #pb8
t=int(input())
for i in range(t):
    s=list(input().split())
    l='aeiouAEIOU'
    vc=0
    cc=0
    wc=len(s)
    for j in s:
        for k in j:
            if k.isalpha():
                if k in l:
                    vc=vc+1
                else:
                    cc=cc+1
    print(wc,vc,cc)

#
t=int(input())
for i in range(t):
    s=list(input().split())
    l='aeiouAEIOU'
    vc=0
    cc=0
    for j in s:
        if j.isalpha():
            if j in l:
                    vc=vc+1
                else:
                    cc=cc+1
    wc=len(s.split())
            
    

#pb9
t=int(input())
for i in range(t):
    A,B=input().split()
    r=''
    for j in B:
            if j 5not in A:
                    r=r+j
    print(r)


t=int(input())
for i in range(t):
    a,b=input().split()
    b=int(b)
    r=''
    for i in a:
        k=ord(i)+b
        if k>122:
            k=96+(k-122)
            r=r+chr(k)
        else:
            r=r+chr(k)
    print(r)

#factorial                  
class classa:
    def factorial(self,n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print(fact)
ob=classa()
ob.factorial(5)
            
 
#fgh
class classA:
    def __init__(self,n):
        self.n=n
        print(n)
    def factorial(self):
        r=1
        for i in range(1,self.n+1):
            r=r*i
        print(r)
ob=classA(5)
ob.factorial()
    
        











    
