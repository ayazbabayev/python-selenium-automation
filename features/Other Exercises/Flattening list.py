def flatten(alist):
    flat_list = []
    for element in alist:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
print('Original List :', nested_list)
print('Modified flat list:', flatten(nested_list))