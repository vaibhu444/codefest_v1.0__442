n = int(input("Enter number"))


def mul(n):
    ans = 1
    for i in range(1, n + 1):
        ans = i * ans
    return ans


if (n % 3 == 0 and n % 5 == 0):
    print(f"{n} is divisible by both 3 and 5")
    ans=[]
    for i in range(1,n):
        ans = ans+[mul(i)]
    print(f"Multiplication = {ans}")
    # ans = mul(n)
    # print(f"Multiplication = {ans}")
elif (n % 3 == 0):
    ans=[]
    for i in range(1,n):
        ans = ans+[mul(i)]
    print(f"Multiplication = {ans}")
    # print(f"{n} is divisible by 3")
    # ans = mul(n)
    print(f"Multiplication = {ans}")
elif (n % 5 == 0):
    ans=[]
    for i in range(1,n):
        ans = ans+[mul(i)]
    print(f"Multiplication = {ans}")
    print(f"{n} is divisible by 5")
    # ans = mul(n)
    # print(f"Multiplication = {ans}")
else:
    print("Not divisible by either 3 or 5")
