# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    if end is None:
        end = len(arr) - 1
    if start > end:
        return end
    
    mid = (start + end) // 2
    if target == arr[mid]:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, start, mid - 1)
    return binary_search(arr, target, mid + 1, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return target
        elif target < mid:
            end = mid - 1
        else:
            start = mid + 1
        
    return False