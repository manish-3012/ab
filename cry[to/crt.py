def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def extended_gcd(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (d, x, y) = extended_gcd(b, a % b)
        return (d, y, x - (a // b) * y)

def chinese_remainder_theorem(a, m):
    M = 1
    for i in range(len(m)):
        M *= m[i]
    
    x = 0
    for i in range(len(m)):
        Mi = M // m[i]
        _, ai, _ = extended_gcd(m[i], Mi)
        x += a[i] * Mi * ai
    
    return x % M

a = [2, 3, 2]
m = [3, 5, 7]

print(chinese_remainder_theorem(a, m))
