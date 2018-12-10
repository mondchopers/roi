import itemkey as itk

## Testing that all buildings in dictionary are in the correct format ##

itemList = list(itk.itemDict.keys())
for i, building in itk.buildingDict.items():
    check = True
    # Input Check
    for item in building[2]:
        if len(item) == 0:
            continue
        if item[0] not in itemList:
            check = False
            print(item)
    # Output Check
    for item in building[1]:
        if len(item) == 0:
            continue
        if item[0] not in itemList:
            check = False
            print(item)

    if not check:
        print("Building", building[0], i, "invalid")
        break
    else:
        print("Building", building[0], i, "valid")

