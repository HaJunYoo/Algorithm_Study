n = int(input())
a_min = 217000000
a_max = -217000000

s_x, s_y = 0, 0
e_x, e_y = n-1, n-1

a = []
for k in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] > a_max:
            e_x, e_y = k, j
            a_max = temp[j]

        if temp[j] < a_min:
            s_x, s_y = k, j
            a_min = temp[j]

    a.append(temp)


visited = [[False] * n for _ in range(n)]

dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)

cnt = 0


def valid_coord(x, y):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    else:
        return True


def dfs(x, y):
    global cnt

    if (x, y) == (e_x, e_y):
        cnt += 1
        return

    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy
        if valid_coord(new_x, new_y) and not visited[new_x][new_y]:
            if a[new_x][new_y] > a[x][y]:
                visited[new_x][new_y] = True
                dfs(new_x, new_y)
                visited[new_x][new_y] = False


print(a_min, a_max)

visited[s_x][s_y] = True
dfs(s_x, s_y)
print(cnt)