def checkIsList(col):
    return isinstance(col, list)

def process_collection(col, isNumber):
    newCol = []

    if not checkIsList(col):
        return newCol

    for elem in col:
        if isNumber:
            if (isinstance(elem, str) and elem.isnumeric() == isNumber) or isinstance(elem, int) == isNumber:
                newCol.append(int(elem))
        else:
            if isinstance(elem, str) and elem.isnumeric() == isNumber:
                newCol.append(elem)

    newCol.sort()
    return newCol

def process_numbers(col):
    return process_collection(col, True)

def process_names(col):
    return process_collection(col, False)