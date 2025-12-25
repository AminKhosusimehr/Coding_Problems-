def revert(str) : 
    if len(str) == 1 :
        return str[0]
    return revert(str[1:]) + str[0]

print(revert('amin'))