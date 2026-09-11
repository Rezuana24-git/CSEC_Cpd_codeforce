n= int(input())
result=0
for i in range (n):
    bit = input()
    if "+" in bit:
        result += 1
    if "-" in bit :
        result -= 1
print (result)
