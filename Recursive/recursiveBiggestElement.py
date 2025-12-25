def find(lst:list):
    if len(lst) == 1 :
        return lst[0]
    return max(lst[0] , find(lst[1:]))