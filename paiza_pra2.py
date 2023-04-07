"""num = int(input())
total_price = 0
goods = []
for i in range(num):
    good = input().split()
    goods.append(good[0])
    price = int(good[1])
    total_price = total_price + price
for j in range(num):
    if goods[j] == 'pants' and total_price >= 2000:
        print(goods[j])
        total_price = total_price - 500
        break
#print(goods)
print(total_price)"""


n = int(input())

sum = 0
pants = False

for i in range(n):
    c, p = input().split()
    sum += int(p)
    if c == "pants":
        pants = True

if pants and sum >= 2000:
    sum -= 500

print(sum)
