n, r  = map(int, input().split())

for i in range(n):
    h, w, d = map(int, input().split())
    if h>=r*2 and w>=r*2 and d>=r*2:
        print(i+1)
