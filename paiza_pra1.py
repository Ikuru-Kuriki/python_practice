Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = int(input())
total_price = 0
goods = []
for i in range(num):
    good = input().split()
    goods.append(good[0])
    price = int(good[1])
    total_price = total_price + price
for j in range(num):
    if goods[j][0] == 'pants' and total_price >= 2000:
        total_price -= 500
        break
#print(goods)
print(total_price)
SyntaxError: multiple statements found while compiling a single statement
>>> 
num = int(input())
total_price = 0
goods = []
for i in range(num):
    good = input().split()
    goods.append(good[0])
    price = int(good[1])
    total_price = total_price + price
for j in range(num):
    if goods[j][0] == 'pants' and total_price >= 2000:
        total_price -= 500
        break
#print(goods)
print(total_price)
SyntaxError: multiple statements found while compiling a single statement
>>> 