'''
The idea is to use optimized DP solution to solve.
At the beginning, I try normal DP, which is just uses recursion from (0, 0) to the end.
Unfortunately, it's out of time.
Then I try to separate this matrix into two parts, half left and half right.
The reason why it works based on this math rule, A xor B xor C = D <==> A xor B xor D = C.
So, I can use a special dictionary d to store the middle points where two half parts meet.
This reduces the time at least a half.
(Attention: I have out of time states many times, from 10pm to 2am, until I find backward function
has wrong return place. It leads to run the program with double useless data)
'''
# standard python input
n, m, k = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
re = 0
half = (m + n - 2) // 2
d = [dict() for _ in range(22)]


def forward(i, j, value):
    if i >= n or j >= m:
        return
    value ^= l[i][j]
    if i + j == half:
        if value in d[i]:
            d[i][value] += 1
        else:
            d[i][value] = 1
        return
    forward(i+1, j, value)
    forward(i, j+1, value)


def backward(i, j, value):
    if i < 0 or j < 0:
        return
    if i + j == half:
        tmp = k ^ value
        if tmp in d[i]:
            global re
            re += d[i][tmp]
        return
    value ^= l[i][j]
    backward(i-1, j, value)
    backward(i, j-1, value)


forward(0, 0, 0)
backward(n-1, m-1, 0)
print(re)
