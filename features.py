#from dateutil.parser import parse


months = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","setiembre","octubre","noviembre","diciembre"]

def isMonth(text):
    lowerCaseText = text.lower()
    try:
        wordIndex = months.index(lowerCaseText)
    except ValueError:
        return False
    return True


print(isMonth("Enero"))
print(isMonth("yolo"))
print(isMonth("8"))
print(isMonth("2"))
print(isMonth("DICIEMBRE"))
