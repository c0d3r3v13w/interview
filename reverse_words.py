def rev_array_section(arr, start_index, end_index):
    if (start_index < 0) or (end_index>(len(arr)-1)) or start_index>end_index:
        raise Exception('Invalid index {},{}'.format(start_index,end_index))
    if start_index == end_index:
        return
    j = end_index
    for i in range(start_index, (start_index + (end_index-start_index)//2)+1):
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        j -=1

def rev_words(s_arr):
        if len(s_arr) < 2:
            return
        rev_array_section(s_arr, 0, len(s_arr)-1)
        start_index = 0
        for i in range(len(s_arr)):
            if s_arr[i]==' ':
                if i>0 and start_index!=i:
                    rev_array_section(s_arr,start_index,i-1)
                start_index = i+1

        if start_index < len(s_arr):
            rev_array_section(s_arr, start_index, len(s_arr)-1)

s = [c for c in '   dog   bites man   ']
rev_words(s)
print(''.join(s))
s = [c for c in 'array']
rev_words(s)
print(''.join(s))
s = [c for c in '']
rev_words(s)
print(''.join(s))
s = [c for c in 'aaaaaabbbbbb cd']
rev_words(s)
print(''.join(s))
s = [c for c in 'c ']
rev_words(s)
print(''.join(s))
s = [c for c in ' c']
rev_words(s)
print(''.join(s))
