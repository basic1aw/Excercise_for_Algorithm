a,b = input().split()
n = min(len(a),len(b))
m = 0
a = a[::-1]
b = b[::-1]
if len(a) >= len(b):
    res = list(a)
else:
    res = list(b)

for i in range(n):
    tmp = (int(a[i]) + int(b[i]) + m)
    m = tmp//2
    res[i] = str(m)
    t = i+1
while m == 1 and t<len(res):
    tmp = (int(res[t]) + m)
    m = tmp//2
    res[t] = str(m)
    t += 1
if m == 1:
    res.append('1')
print(res[::-1])
