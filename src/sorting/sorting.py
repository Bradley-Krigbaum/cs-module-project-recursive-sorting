# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # Your code here

    i, j = 0, 0
    result = []

    while (i < len(arrA)) and (j < len(arrB)):
        if arrA[i] < arrB[j]:
            result.append(arrA[i])
            i += 1
        else:
            result.append(arrB[j])
            j += 1
    if i == len(arrA):
        result.extend(arrB[j:])
    else:
        result.extend(arrA[i:])
        
    return result

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2
    arrA, arrB = merge_sort(arr[:middle]), merge_sort(arr[middle:])

    return merge(arrA, arrB)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here
