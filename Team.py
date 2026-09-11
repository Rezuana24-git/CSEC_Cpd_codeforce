n=int(input())
final=0
for i in range(n):
    m= list(map(int,input().split()))
    result= m.count(1)
    if result >= 2:
        final+=1
print(final)

