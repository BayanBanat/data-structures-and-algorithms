
def binary_search(arr, target):
    left=0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def sequential_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

   
print(binary_search([4, 8, 15, 16, 23, 42], 15))

print(sequential_search([-131, -82, 0, 27, 42, 68, 179], 42	))
