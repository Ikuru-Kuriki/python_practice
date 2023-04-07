l = []
hit = [1, 2, 3, 4]
for i in range(5):
    score = int(input())
    l.append(score)

if set(hit) <= set(l):
    print("Yes")
else:
    print("No")

"""
v = [False] * 5

for i in range(5):
    m = int(input())
    v[m] = True

res = True
for i in range(1, 5):
    if v[i] == False:
        res = False
        break

if res:
    print("Yes")
else:
    print("No")"""