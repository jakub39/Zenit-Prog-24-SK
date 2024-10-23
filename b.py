n = int(input())
par = 0

if n % 2 == 0:
    par = n + 1

if n % 2 != 0:
    par = n - 1

print(par)