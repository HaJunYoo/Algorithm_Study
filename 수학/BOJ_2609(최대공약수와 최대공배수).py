def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
g = gcd(a, b)
print(g)

l = g*(a//g)*(b//g)

print(l)