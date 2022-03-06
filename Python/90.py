if __name__ == '__main__':
    input = '10.123.134.5'
    str1 = input.split('.')
    if len(str1) != 4:
        print('NO')
    flag = 1
    for s in str1:
        if s == '':
            flag = 0
            break
        if not s.isdigit():
            flag = 0
            break
        # if not flag:
        #     break
    if flag:
        print('YES')
    else:
        print('NO')