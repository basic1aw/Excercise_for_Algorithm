def reverse(num):
    try:
        num_list = list(str(num))[::-1]
        mark = ''
        if '-' in num_list:
            mark = '-'
            num_list.remove('-')
        res = mark + ''.join(num_list)
        return int(res)
    except:
        break

a = -100
print(reverse(a))
