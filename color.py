t=int(input())
l=[]

for i in range(t):
    n=int(input())
    a=input()
    l+=[a]

for i in l:
    flag=0

    stroke=0
    for j in range(len(i)):
        if i[j]=="Y":
            if(flag==1):
                continue
            else:
                stroke+=1
            flag=1
            continue
        if i[j]=="B":
            if (flag == 2):
                continue
            else:
                stroke += 1
            flag = 2
            continue
        if i[j]=="R":
            if (flag == 3):
                continue
            else:
                stroke += 1
            flag = 3
            continue
        if i[j]=="O":
            if (flag == 3 or flag == 1):
                continue
            else:
                stroke += 1

            continue


print(stroke)


