n= int(input())
D= "Division"
for i in range(n):
    num= int(input())
    if num <= 1399:
        print(D + " 4")
    elif 1400 <= num <= 1599:
        print(D + " 3")
    elif  1600 <= num <= 1899:
        print(D + " 2")
    else:
        print(D + " 1")
