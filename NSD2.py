def gcd2(a, b):
    while b:
        a, b = b, a % b
    return a
#fjnvesnvsl;dkfvn;
a, b = map(int, input().split())
print(gcd2(a, b))