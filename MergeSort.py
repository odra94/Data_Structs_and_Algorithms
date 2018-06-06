lst = [-1,90,9,4,2,67,2,4,-9]

def merge(left, right):
    result = []
    i,j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = int(len(lst) / 2)
    left = mergesort(lst[:mid]) # from beginning to middle
    right = mergesort(lst[mid:]) # from middle to end
    return merge(left, right)

print(mergesort(lst))