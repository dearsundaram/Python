num = 25
f1 = 0
f2 = 1

for num in range(1,num,1):
    num = f1 + f2
    f1 = f2
    f2 = num
    print(num)
print("num is : ", num)
