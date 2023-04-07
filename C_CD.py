num = int(input())
total_time = 0
for i in range(num):
    time = input().split()
    min = int(time[0])
    sec = int(time[1])
    sum_sec = min*60 + sec
    total_time += sum_sec

if total_time <= 74*60:
    print('Yes')
else:
    print('No')


"""
n = int(input())

seconds = 0
for _ in range(n):
    m, s = map(int, input().split())
    seconds += 60 * m + s

if seconds <= 74 * 60:
    print("Yes")
else:
    print("No")"""
