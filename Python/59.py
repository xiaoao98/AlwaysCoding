if __name__ == '__main__':
    s = 'asdjgqad'
    dic = {}
    for i, c in enumerate(s):
        if c not in dic:
            dic[c] = [1, i]
        else:
            dic[c][0] += 1
    tmp = []
    for key in dic:
        if dic[key][0] == 1:
            tmp.append(dic[key][1])
    if not tmp:
        print('-1')
    else:
        print(s[min(tmp)])