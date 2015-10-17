result = []

def f(n, s, m):
    if n == 0:
        result.append(s)
        return

    if m > int(n):
        return

    if n % (m*2) == 0:
        f(n, "0"+s, m*2)
        f(n-m*2, "2"+s, m*2)
    else:
        f(n-m, "1"+s, m*2)
number = input()

f(int(number), "", 1)
print(result)