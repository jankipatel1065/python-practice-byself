weight = int(input('weight:'))
unit = input('(L) or (k)')
if unit.upper() == "L":
    converted = weight*0.45
    print(f"you are {converted}")
else:
    converted= weight / 0.45
