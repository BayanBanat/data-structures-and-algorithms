def insert(sorted, value):
    i = 0
    while i < len(sorted) and value > sorted[i]:
        i += 1
    sorted.insert(i, value)


def insertion_sort(input):
    sorted = [input[0]]
    for i in range(1, len(input)):
        insert(sorted, input[i])
    return sorted