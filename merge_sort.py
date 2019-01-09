# With auxiliary array provided
def merge_sort(arr):
    if arr is None or len(arr) == 0:
        return arr
    
    buf = [0 for _ in arr]
    _merge_sort_helper(arr, 0, len(arr) - 1, buf)
    return arr
    
def _merge_sort_helper(arr, start, end, buf):
    if start == end:
        return
    mid = start + (end - start) // 2
    _merge_sort_helper(arr, start, mid, buf)
    _merge_sort_helper(arr, mid + 1, end, buf)
    _merge_two_sorted_array(arr, start, mid, mid + 1, end, buf)
    
def _merge_two_sorted_array(arr, lstart, lend, rstart, rend, buf):
    for k in range(lstart, rend + 1):
        buf[k] = arr[k]
    i, j, k = lstart, rstart, lstart
    while i <= lend and j <= rend:
        if buf[i] <= buf[j]:
            arr[k] = buf[i]
            k += 1
            i += 1
        else:
            arr[k] = buf[j]
            k += 1
            j += 1
    while i <= lend:
        arr[k] = buf[i]
        k += 1
        i += 1
        
def test(arr):
    assert merge_sort(arr) == sorted(arr)

if __name__ == '__main__':
    arrs = [[],
            [1, 2, 3],
            [3, 2, 1],
            [2, 5, 1, 3, 6, 7, 1, 0],
            [0, 1, 6, 2, 1, 4, 3, 0]]
    for arr in arrs:
        test(arr)