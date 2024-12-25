#sequence of unsorted values
def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop() #pop removes the last element and also return it

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item) 
        
        else:
            items_lower.append(item)

    return quick_sort(items_greater) + [pivot] + quick_sort(items_lower) #interchangable to output from ascending to descending order

print(quick_sort([7,5,6,4,8,1,3,5,49,98,7,4,5,1,3,3,64,48,9,9,4,2])) #example array 