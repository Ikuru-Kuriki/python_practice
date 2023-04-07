input_line, height = map(int, input().split(' '))
sum_length = height
s = []
for i in range(input_line-1):
    t = int(input())
    s.append(t)
    length = height - s[i]
    sum_length += length
    
print(height*sum_length)
    
