a=int(input())
for _ in range(a):
    b=int(input())
    c=set(map(int,input().split()))
    d=int(input())
    e=set(map(int,input().split()))
    print(c.issubset(e))