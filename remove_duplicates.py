def rem_dup(arr_s):
    if len(arr_s)==0:
        return
    chars = set()
    i=0
    while i<len(arr_s):
        if arr_s[i] not in chars:
            chars.add(arr_s[i])
            i += 1
        else:
            arr_s.pop(i)


def rem_dup_iter(arr_s):
    if len(arr_s)==0:
        return

    i=0
    while i < len(arr_s):
        j= i-1
        while j>-1:
            if arr_s[j] == arr_s[i]:
                arr_s.pop(i)
                i -= 1
                break
            j -= 1
        i += 1


s = [c for c in 'aa bb cc dd']
rem_dup_iter(s)
print(s)
