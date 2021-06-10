
from math import *
def is_prime(n):
    s=int(sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
        return True
for i in range(int(input())):
    fi,la=map(int,input().split())
    f=l=0
    for j in range(fi,la+1):
        if f==0 and is_prime(fi):
            f=fi
        else:
            fi+=1
        if l==0 and is_prime(la):
            l=la
        else:
            la-=1
    if f!=0 and l!=0:
        print(l-f)
    else:
        print(-1)



