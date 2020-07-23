import time, math
A, B = 0, 0
print("\x1b[2J", end='')
while True:
    z = [0] * 1760
    b = [' '] * 1760
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(40 + 30 * D * (l * h * m - t * n))
            y = int(12 + 15 * D * (l * h * n + t * m))
            o = int(x + 80 * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 22 > y and y > 0 and x > 0 and 80 > x and D > z[o]:
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
    print('\x1b[H', end='')
    for k in range(1761):
        print((b[k] if k % 80 else '\n'), end='')
        A += 0.00004
        B += 0.00002
    time.sleep(0.03)
