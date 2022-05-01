h, m, a = input().split(":")
h = int(h)
if a.upper() == "AM":
    h = h % 12
    print(f"{h}:{m}")
elif a.upper() == "PM":
    t = h % 12
    h = 12 + t
    print(f"{h}:{m}")
else:
    print("invalid")
