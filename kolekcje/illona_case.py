array = [6, 2, 1, 12, 18, 3, 5]
maxValue = max(array)
minValue = min(array)
maxIndex = array.index(maxValue)
minIndex = array.index(minValue)
#print(maxValue)
#print(minValue)
for i, elem in enumerate(array):
    if elem == maxValue:
        print('weszło', elem)
        array.remove(elem)
        print(array)
        array.insert(i, minValue)
        print(array)
    elif i == minIndex:
        print(array)
        array.remove(elem)
        array.insert(i, maxValue)

print(array)
# print(minIndex)