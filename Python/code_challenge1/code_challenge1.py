
def reverseArray(arr):
    reverseArr = []
    i = len(arr) - 1
    while i >= 0:
        reverseArr.append(arr[i])
        i -= 1
    return reverseArr

print(reverseArray([1, 2, 3, 4, 5, 6]))
