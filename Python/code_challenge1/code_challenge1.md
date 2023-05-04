# array-reverse

## Whiteboard Process:

![Whiteboard](https://user-images.githubusercontent.com/125543324/235689079-bd6140a4-441c-4f15-aaf4-3834c4a7dda5.png)

## Approach & Efficiency:

The approach of the reverseArray function is to iterate over the indices of the input array in reverse order, and append the corresponding elements to a new array in the reverse order. This approach involves using a while loop to iterate over the indices in reverse order, and an additional array to store the reversed elements.


## Solution:

```
def reverseArray(arr):
    reverseArr = []
    i = len(arr) - 1
    while i >= 0:
        reverseArr.append(arr[i])
        i -= 1
    return reverseArr
```    

for teting in Compiler :

```
print(reverseArray([1, 2, 3, 4, 5, 6]))
```
 
