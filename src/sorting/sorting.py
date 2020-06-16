# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # position in arrA
    a = 0
    
    # position in arrB
    b = 0

    for k in range(0, elements):
        # if position in arrA is out of the bounds of arrA, set 
        # current position in merged_arr to arrB[b] and then we increment position in arrB
        if a >= len(arrA):
            merged_arr[k] = arrB[b]
            b += 1
        # if posiition in arrB is out of bounds of arrB, set
        # the current position in merged_arr to arrA[a] and increment pos in arrA
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1  
        # if current value of arrA is less than that of arrB, set
        # current position in merged_arr to a  to arrA[a] and increment position in arrA
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1  
        # if current value of arrA is greater thatn that of arrB, set 
        # the current position in merged_arr to arrB[b] and increment position in arrB            
        elif arrA[a] > arrB[b]:
            merged_arr[k] = arrB[b]   
            b += 1
                
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # if array has more than 1 item, split it in half
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr) //2 ])
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

