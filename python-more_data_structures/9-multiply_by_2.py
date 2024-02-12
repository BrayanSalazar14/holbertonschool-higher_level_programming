def multiply_by_2(a_dictionary):
    newDic = dict(a_dictionary)
    for index in newDic:
        newDic[index] *= 2
    return newDic
