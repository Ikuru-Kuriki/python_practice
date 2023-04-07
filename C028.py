n = int(input())
point = 0
for i in range(n):
    cor, ans = map(str, input().split())
    if len(cor) == len(ans):
        if cor == ans:
            point += 2
        else:
            wrong = 0
            for j in range(len(cor)):
                if cor[j] != ans[j]:
                    wrong += 1
            if wrong == 1:
                point += 1
print(point)
                
                

    
