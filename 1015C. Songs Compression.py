'''
Greedy again.
'''
n, m = map(int, input().split())
s = list()
cnt = 0
cnt_tmp = 0
for _ in range(n):
    a, b = map(int, input().split())
    cnt += a
    cnt_tmp += a-b
    s.append(a-b)
tmp = sorted(s, reverse=True)
if cnt > m:
    if cnt - cnt_tmp > m:
        print(-1)
    else:
        for i in range(n):
            if cnt - tmp[i] <= m:
                print(i+1)
                break
            else:
                cnt -= tmp[i]
else:
    print(0)
