def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''    
    if (aList == []):
        return aList  
    elif (type(aList[0]) == list):
        return flatten(aList[0]) + flatten(aList[1:])
    else:
        return aList[:1] + flatten(aList[1:])