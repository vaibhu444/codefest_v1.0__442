l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
     "x", "y", "z"]
test_case = int(input())
ans2=[]
for i in range(test_case):
    minus = 0
    l1 = list(input())
    w = list(input())
    ans = []

    for j in l1:
        temp = []
        sum1 = 0
        for m in w:
            k = l.index(m)
            # print(k)
            # print(l1.index(j))
            temp = temp + [abs(k - l.index(j))]
            # minus = minus + abs(k - l1.index(j))
        # print(temp)
        sum1=min(temp)+sum1
        # pr
        ans += [sum1]
    ans2+=[sum(ans)]

for i in range(len(ans2)):
    print(f"case #{i + 1}:{ans2[i]}")
