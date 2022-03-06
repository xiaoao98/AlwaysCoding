def islegal(psd):
    if len(psd) <= 8:
        return False
    ty = set()
    for s in psd:
        if s.isdigit():
            ty.add(1)
        elif s.isalpha():
            if s.lower() == s:
                ty.add(2)
            else:
                ty.add(3)
        else:
            ty.add(4)
    #print(ty)
    if len(ty) < 3:
        return False
    rep = set()
    for i in range(2, len(psd)):
        if psd[i-2:i+1] in rep:
            return False
        rep.add(psd[i-2:i+1])
    return True


if __name__ == "__main__":
    if islegal('021Abc9000'):
        print('OK')