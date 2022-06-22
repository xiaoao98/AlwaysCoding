def getPermutations(array):
    if array is None or len(array) == 0:
        return []
    result = helper(array)
    return result


def helper(array):
    if len(array) <= 1:
        return [[array[0]]]
    result = []
    for i in range(len(array)):
        firstele = array[i]
        for comb in helper(array[:i] + array[i+1:]):
            result.append([firstele] + comb)
    return result


if __name__ == '__main__':
    array = [1, 2, 3]
    print(getPermutations(array))