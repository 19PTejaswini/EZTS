#problem Statement 1
def profit(n):
    return n*50 - (n*50*70)//100
def main(i):
    if i==0:
        return 
    else:
        print(profit(int(input())))
        main(i-1)
main(int(input()))


#problem Statement 2

def time(x,y):
    print(y//2+(x-y))
for _ in range(int(input())):
    a ,b = map(int,input().split())
    time(a,b)


#problem Statement 3
def no(a,c):
    if a==0:
        return c
    t = a%10
    if t==4:
        c+=1
    return no(a//10,c)
for _ in range(int(input())):
    a = int(input())
    print(no(a,0))


#problem Statement 4

a = int(input())
f = 1
while a != 1:
    f *= a
    a-=1
print(f)

#problem Statement 5
a = int(input())
c = 0
d = a
while d!=0:
    d//=10
    c+=1
a = a*10 + 3
a = a + 3*(10**(c+1))
print(a)
