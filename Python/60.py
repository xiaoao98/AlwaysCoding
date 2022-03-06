if __name__ == '__main__':
    n = 54
    m1 = n//2-1
    m2 = n//2+1
    def isp(num):
        if num==3: return True
        for i in range(3,num-2,2):
            if num%i == 0:
                return False
        return True
    while True:
        if isp(m1) and isp(m2):
            print(str(m1))
            print(str(m2))
            break
        else:
            m1 -= 2
            m2 += 2