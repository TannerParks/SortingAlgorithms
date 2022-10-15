#Tanner Parks
#Merge Sort

list_of_data = []
testData = [5, 1, 4]

with open("data.txt", "r") as file:
    for line in file:
        data = line.split()
        data.pop(0) # deletes the length of the list
        list_of_data.append([int(item) for item in data])   # changes the data from strings to integers


def mergeSort(array: list):
    leftIter = 0    # iterator for left list
    rightIter = 0   # iterator for right list
    arrayIter = 0   # iterator for the main list (final list)
    
    if len(array) == 1: # returns list that only has one value
        return array

    mid = len(array)//2
    leftList = array[:mid]  # list from the beginning to the midpoint
    rightList = array[mid:] # list from the midpoint to the end

    mergeSort(leftList)
    mergeSort(rightList)
    
    while leftIter < len(leftList) and rightIter < len(rightList):
        if leftList[leftIter] <= rightList[rightIter]:
            array[arrayIter] = leftList[leftIter]   # can't use append since we're sorting using the list passed to the function and not a new list 
            leftIter += 1   # Next spot in left list iterator
        else:
            array[arrayIter] = rightList[rightIter]
            rightIter += 1  # Next spot in right list iterator
        arrayIter += 1  # Next spot in sorted list iterator

    # The loops below here make sure nothing gets left behind so we don't have an incomplete list
    while leftIter < len(leftList):
        array[arrayIter] = leftList[leftIter]
        leftIter += 1
        arrayIter += 1

    while rightIter < len(rightList):
        array[arrayIter] = rightList[rightIter]
        rightIter += 1
        arrayIter += 1
    
    return array

def main(array: list):
    for i in range(0, len(array)):
        #print(array[i])
        print(*mergeSort(array[i]))
        #mergeSort(array[i])


main(list_of_data)


