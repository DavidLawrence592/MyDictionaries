with open("WorldSeriesWinners.txt", "r") as file:
    data = file.read()

    data = data.split("\n")

print(data)


dictyears = {}
dictfrequency = {}

initial = 1903

for line in data:
    if initial == 1904 or initial == 1994:
        initial += 1

    dictyears[initial] = line

    initial += 1

print(dictyears)


for line in data:
    if line in dictfrequency:
        dictfrequency[line] += 1

    else:
        dictfrequency[line] = 1

print(dictfrequency)


year = int(input("Enter the Year:"))
if year in dictyears:
    print("Winners were:", dictyears[year])
    print("total Wins:", dictfrequency[dictyears[year]])

else:
    print("Invalid Year Entered")
