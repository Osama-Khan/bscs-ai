# Define two functions (one iterative and other recursive)
# in Python named sub-it and sub-rec. Each of the functions
# will take three arguments; old-value, new-value, and a
# list. They should replace old-value with the new-value
# from the given list.

def sub_it(old, new, arr):
    out = list()
    for e in arr:
        if (e == old):
            out.append(new)
        else:
            out.append(e)
    return out


def sub_rec(old, new, arr):
    out = []
    if len(arr) != 1:
        if arr[0] == old:
            out.append(new)
        else:
            out.append(arr[0])
        out.extend(sub_rec(old, new, arr[1:]))
        return out
    else:
        if arr[0] == old:
            return [new]
        return arr


print(sub_it(10, 5, [10, 8, 10, 12]))
print(sub_rec(10, 5, [10, 8, 10, 12]))
