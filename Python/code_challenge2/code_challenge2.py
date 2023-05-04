def insertShiftArray(arr,x):
    '''
    This function inserts an element into an array 
    and shifts the other elements to make place for it.
    :param arr: list
    :param x: int
    :return: list
    '''
    midArr=len(arr) // 2
    if len(arr) % 2 == 0:
      arr.insert(midArr, x)
    else:
       int(midArr)
       arr.insert(midArr+1, x)
    return arr
  
