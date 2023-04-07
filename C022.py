n = int(input())
st = []
h_max = 0
l_min = 1000000
for i in range(n):
    s, e, h, l = map(int, input().split())
    st.append(s)
    if h > h_max:
        h_max = h
    if l < l_min:
        l_min = l
print(st[0], e, h_max, l_min)