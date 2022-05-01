t = int(input())
ans = []
for i in range(t):
    sum1 = 0
    n, p = input().split()
    n = int(n)
    p = int(p)
    last = 0
    temp = 0
    for j in range(n):

        sum = 0
        a = input().split()
        a = list(map(int, a))
        a = sorted(a)
        for k in range(p - 1):
            sum = (a[k + 1] - a[k]) + sum
        c1 = abs(last - a[p - 1])
        c2 = abs(last - a[0])
        cnt1 = 0
        for z in a:
            if z <= last:
                cnt1 += 1
        cnt2 = len(a) - cnt1
        if cnt1 == cnt2:
            if c2 <= c1:
                temp = c2 + sum
                sum1 = sum1 + temp
            else:
                temp = c1 + sum
                sum1 = sum1 + temp
        elif cnt2 > cnt1:
            temp = c2 + sum
            sum1 = sum1 + temp

        else:
            temp = c1 + sum
            sum1 = sum1 + temp
        last = a[p - 1]
        # sum1 = sum1 + temp
    ans += [sum1]
for i in range(len(ans)):
    print(f"case #{i + 1}:{ans[i]}")
