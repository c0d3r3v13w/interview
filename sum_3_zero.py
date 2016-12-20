def sum_3_zero(arr):

    if len(arr) < 3:
        return None
    nums = set()
    needed = {}
    nums.add(arr[0])
    nums.add(arr[1])

    needed[0-(arr[0]+arr[1])] = (arr[0],arr[1])

    for i in range(2, len(arr)):
        if arr[i] in needed:
            return arr[i], needed[arr[i]][0], needed[arr[i]][1]
        else:
            for n in nums:
                needed[0-(n+arr[i])] = (n, arr[i])

    return None


print(sum_3_zero([1,2,-3]))
