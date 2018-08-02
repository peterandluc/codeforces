'''
It's really stupid for me that I understand totally wrong with what it required.
And after this contest, I fall down to grey name...
'''
n, m = map(int, input().split())
s = list()
for i in range(n):
    s.append(list(map(lambda x: 0 if x == "." else 1, *input().split())))

re = list()
check_re = [[0]*m for _ in range(n)]


def check(x, y, length):
    if x + length >= n or y + length >= m or x - length < 0 or y - length < 0:
        if length > 1:
            re.append(['{} {} {}'.format(x + 1, y + 1, length-1)])
        return
    tmp = s[x+length][y] + s[x-length][y] + s[x][y+length] + s[x][y-length]
    if tmp == 4:
        prin(x, y, length)
        check(x, y, length+1)
    else:
        if length > 1:
            re.append(['{} {} {}'.format(x + 1, y + 1, length-1)])


def prin(x, y, i):
    check_re[x][y] = 1
    check_re[x + i][y] = 1
    check_re[x - i][y] = 1
    check_re[x][y + i] = 1
    check_re[x][y - i] = 1


for i in range(n):
    for j in range(m):
        if s[i][j] == 1:
            check(i, j, 1)

if s == check_re:
    print(len(re))
    for i in re:
        print(i[0])
else:
    print(-1)




