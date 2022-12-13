def pairs(a, k):
    answer = 0

    vals = {}

    for i in a:
        vals[i] = [i - k, i + k]

    for k in vals:
        for j in vals[k]:
            if j in vals:
                answer += 1

    return int(answer / 2)


# pseduo code:
# 1. Create a dictionary of the values in the array
# 2. For each value in the array, check if the value minus k or the value plus k is in the dictionary
# 3. If the value minus k or the value plus k is in the dictionary, then add 1 to the answer
# 4. Return the answer divided by 2

# overall equation for running time:
# T = O(n)


# testing
if __name__ == '__main__':
    # input format:
    # n k
    # a1 a2 ... an
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size = a[0]
    _k = a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b, _k))
