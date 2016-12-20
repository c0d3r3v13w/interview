def zeros_right(arr):
    if len(arr)<2:
        return arr
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i] == 0:
            while j>=0 and arr[j] == 0:
                j -= 1
            if j>i and arr[j]!=0:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
        i += 1

    return arr

print(zeros_right([0,0,0,0,0]))
print(zeros_right([0,1,0,0,2,3,4]))
print(zeros_right([0,1]))
print(zeros_right([1,0]))
print(zeros_right([0]))
