
def duplicate(s):
    if s == '':
        return s
    s = sorted(list(s))
    idx = 0
    i = 0
    for j in range(len(s)):
        if s[i] != s[j]:
            s[idx] = s[i]
            idx += 1
            i = j
    s[idx] = s[i]
    return ''.join(s[:idx+1])

def count(arr):
    i = 0
    res = []
    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            res.append(j-i)
            i = j
    res.append(len(s)-i)
    return res

s = input('enter a string:')
print(duplicate(s),'\n',count(s))
