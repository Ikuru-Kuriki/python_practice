
num = input().split()
car_num = int(num[0])
jam_dis = int(num[1])

jam = 0

for i in range(car_num-1):
    dis = int(input())
    if dis <= jam_dis:
        jam = jam + dis
           
print(jam)
