m1=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]
for i in m1:
   print(i)
# print(m1)
ans1=int(input("Enter row: "))
row1=m1[(ans1-1)][:]
# print(row1)

m2=[[1,5,9,13],
   [2,6,10,14],
   [3,7,11,15],
   [4,8,12,16]]
for i in m2:
   print(i)
# print(m2)
ans2=int(input("Enter row: "))
row2=m2[(ans2-1)][:]
# print(row2)
for i in row2:
   for j in row1:
      if i==j:
         print(i)

