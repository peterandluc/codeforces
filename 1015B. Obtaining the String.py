'''
Water problem, nothing to say. First idea would be dp, but finally I find it's just greedy.
'''
n = int(input())
c = [*input()]
s = [*input()]
re = list()
def swap(i):
    c[i], c[i+1] = c[i+1], c[i]
if sorted(c) != sorted(s):
    print(-1)
else:
    for i in range(n):
        if c[i] != s[i]:
            j = i
            tmp = list()
            while True:
                if j+1 >= n:
                    break
                if s[i] != c[j]:
                    tmp.append(j)
                    j += 1
                else:
                    break
            if len(tmp) == 0:
                flag = False
                break
            else:
                for k in range(len(tmp)-1, -1, -1):
                    swap(tmp[k])
                    re.append(tmp[k]+1)
    print(len(re))
    print(*re)

