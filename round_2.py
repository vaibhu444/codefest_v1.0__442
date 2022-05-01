num=input("enter string")
l=len(num)
# print(l)
demp=""
for i in range(l-1,0,-1):
    demp=demp+num[i]
demp=demp+num[0]
if num==demp:
    print("pallidrome")
else:
    print("not pallidrome")
