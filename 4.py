a = [int(x) for x in open('17_2400.txt')]
ans = []
m = min(x for x in a if 100 <= abs(x) <= 999 and abs(x) // 100 == 5)
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) % m == 0:
        ans.append(a[i] + a[i + 1])
print(len(ans), max(ans))


