s1 = [i for i in input().strip()]
s2 = [i for i in input().strip()]
sd = s1.copy()
f = ['F','L','A','M','E','S']
for i in s1:
    if i in s2:
        sd.remove(i)
        s2.remove(i)
n = len(sd) + len(s2)
m = n
while len(f) > 1:
    if m > len(f) :
        m -= len(f)
    else:
        f.pop(m-1)
        f = f[m-1:] + f[:m-1]
        m = n
print(f[0])