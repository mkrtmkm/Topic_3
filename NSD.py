def gcd1(a, b):
    while b:
        a, b = b, a % b
    return a
a, b = map(int, input().split())
print(gcd1(a, b))