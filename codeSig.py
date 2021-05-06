def csAlphanumericRestriction(input_str):
    if input_str.isa-lpha():
        return True
    
    if input_str.isdigit():
        return True
    
    else:
        return False

csAlphanumericRestriction(90870)


def csOppositeReverse(txt):
    txt = txt[::-1].swapcase()
    return txt

csOppositeReverse("chaD AnD SARah ARE Awesome ParTners")


def csSquareAllDigits(n):
    string = ""
    
    res = [int(x) for x in str(n)]
    
    for number in res:
        squared = (number ** 2)
        newString = str(squared)
        string += newString
    
    return int(string)

csSquareAllDigits(654654)

def csRemoveTheVowels(input_str):
    newstr = input_str
    vowels = ('a', 'e', 'i', 'o', 'u', 'I', 'O', 'U', 'A', 'E')
    for x in input_str:
        if x in vowels:
            newstr = newstr.replace(x,"")
    return newstr

