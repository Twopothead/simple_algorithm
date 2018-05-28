def addToSkyline(dimension):
    result = []
    result.append((dimension[0], 0))
    result.append((dimension[0], dimension[2]))
    result.append((dimension[1], dimension[2]))
    result.append((dimension[1], 0))
    return result


def mergeSkylines(one, two):
    result = []
    i = 0
    j = 0
    h1 = 0
    h2 = 0

    while i < len(one) and j < len(two):
        if one[i][0] < two[j][0]:
            h1 = one[i][1]
            result.append((one[i][0], max(h1,h2)))
            i += 1
        else:
            h2 = two[j][1]
            result.append((two[j][0], max(h1,h2)))
            j += 1
    while i < len(one):
        result.append(one[i])
        i += 1
    while j < len(two):
        result.append(two[j])
        j += 1

    return result


def skyline(input):
    if len(input) < 2:
        return addToSkyline(input[0])

    one = skyline(input[:len(input) // 2])
    two = skyline(input[len(input) // 2:])
    return mergeSkylines(one, two)



input0 = [(1,11,5), (2,6,7), (3,13,9), (12,7,16), (14,3,25),
         (19,18,22), (23,13,29), (24,4,28) ]


print(skyline(input0))
