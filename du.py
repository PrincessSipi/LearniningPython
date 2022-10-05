def intersection(list1, list2):
    #result = [value for value in list1 if value in list2]
    #return result

  #  largerArray
    #smallerArray
    hashtable = {}
    result= []

    if len(array1) >len(array2):
        largerArray =list1
        smallerArray = list2
    else:
        largerArray = list2
        smallerArray = list1

    hashtable = dict.fromkeys(largerArray, True)

    for value in smallerArray:
        if (value in hashtable):
            result.append(value)
    return result
        
array1 = [1, 2, 3, 4, 5, 6]
array2 = [1, 3, 5, 4,9, 8]
m = intersection(array1, array2)
print(m)
