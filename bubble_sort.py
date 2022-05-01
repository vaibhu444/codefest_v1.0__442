n = int(input("enter the digits:"))
a = input("enter the number").split()
list_num = list(map(int, a))

# print(list_num[1]+list_num[0])
for i in range(0, n - 1):
    # temp=0
    for j in range(i, n):
        if list_num[i] > list_num[j]:
            temp = list_num[i]
            list_num[i] = list_num[j]
            list_num[j] = temp
print(list_num)
