def numbersInPi(pi, numbers):
    nset = set()
    for number in numbers:
        nset.add(number)
    mem = {}
    return helper(pi, 0, nset, mem) - 1 if helper(pi, 0, nset, mem) != -1 else -1


def helper(target, index, nset, mem):
    if len(target) == index:
        mem[index] = 0
        return 0
    if index in mem:
        return mem[index]
    minSpaces = float('inf')
    for i in range(index+1, len(target) + 1):
        if target[index:i] in nset:
            later = helper(target, i, nset, mem)
            if later == -1:
                continue
            else:
                minSpaces = min(1 + later, minSpaces)
    mem[index] = minSpaces if minSpaces != float('inf') else -1
    return mem[index]
if __name__ == '__main__':
    print(numbersInPi("3141592653589793238462643383279",
                      ["3", "141", "592", "65", "55", "35", "8", "9793", "23846264", "383279"]))
