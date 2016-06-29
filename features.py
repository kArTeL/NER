# coding=utf-8

months = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","setiembre","octubre","noviembre","diciembre"]
srs = ["señora", "señor", "sr", "sra","sr.","sra."]

def isMonth(text):
    lowerCaseText = text.lower()
    return isInArray(lowerCaseText,months)


def isSrSra(text):
    lowerCaseText = text.lower()
    return isInArray(lowerCaseText,srs)



def isInArray(text, array):
    try:
        wordIndex = array.index(text)
    except ValueError:
        return False
    return True


# print(isMonth("Enero"))
# print(isMonth("yolo"))
# print(isMonth("8"))
# print(isMonth("2"))
# print(isMonth("DICIEMBRE"))

# print(isSrSra("sra"))
# print(isSrSra("SRA."))
# print(isSrSra("SRA.asd"))
