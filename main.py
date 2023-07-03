def caesarCipherEncryptor(string, key):
    chList = list(string)
    shiftedList = shiftList(chList, key)
    shiftedString = "".join(shiftedList)
    return shiftedString

def shiftList(chList,key):
    newList = []
    for ch in chList:
        chVal = ord(ch)
        newVal = chVal + key

        if newVal > ord('z'):       # 122
            newVal = (newVal - ord('a'))%26 + ord('a')
        newCh = chr(newVal)
        newList.append(newCh)
    return newList
    pass
