#Tanner Parks
#Insertion Sort

list_of_data = []

with open("data.txt", "r") as file:
    for line in file:
        data = line.split()
        data.pop(0)
        list_of_data.append([int(item) for item in data])

def insertSort(array: list):
    for i in range(1, len(array)):
        temp = array[i] # Temp value that we compare the value before to on each pass through
        current = i - 1 # Value being compared to the temp value (value to the left of temp)

        while current >= 0:
            if array[current] > temp:   # Compare temp value with current value
                array[current + 1] = array[current]
                current -= 1    # Current index is brought down so we can compare the next temp value with the next current value
            else:
                break
        array[current + 1] = temp
    return array

def main(array: list):
    for i in range(0, len(array)):
        #print(array[i])
        print(*insertSort(array[i]))
        #insertSort(array[i])
        

main(list_of_data)
