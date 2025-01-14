# This program returns union of two lists while making sure that resulted list does not contain repeated elements

def union(a, b) :
    return len(set(a) | set(b))


list1 = [1,2,3,4,5]
list2 = [1,2,3]
print("Length = ", union(list1, list2))