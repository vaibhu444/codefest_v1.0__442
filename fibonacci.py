# num=int(input("enter the number"))
user_num = int(input("Enter the desire num:"))
inde = 0
cnt = 0
v = 5
lis = [0, 1]
inde1 = 0
for i in range(0, user_num + 5):
    sum1 = lis[i] + lis[i + 1]
    lis += [sum1]
# print(lis)
for j in range(0, user_num + 5):
    cnt = cnt + 1
    if user_num == lis[j]:
        inde = j
        # print("avail")
        break
    # else:
    # print("no")
# print(inde)
if cnt == user_num + 5:
    print("no")
    for j in range(0, user_num + 5):
        if lis[j] > user_num:
            inde1 = j
            break
    print(lis[inde1:inde1 + 5])
else:
    print("yes")
    print(lis[inde:inde + 5])
