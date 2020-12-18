# QUESTION:
# Define a recursive functionin Python named sub_er (i.e. substitute
# embedded-recursive). It should take three arguments; old-value,
# new-value, and a list which could be nested. The function should
# replace old-value with the new-value from the given list.

def sub_er(old, new, lst):
    subList = []
    for i in range(0, len(lst)):
        if type(lst[i]) == list:
            subList.append(sub_er(old, new, lst[i]))
        elif lst[i] == old:
            subList.append(new)
        else:
            subList.append(lst[i])
    return subList
