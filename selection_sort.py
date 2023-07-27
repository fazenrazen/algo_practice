    
"""
Arrays 
Pro: Finding an element and allocatiing space
Con: Adding space or wastage of space

Linked List
Pro: Easy to add space to the list
Con: Have to go through one by one

Array  
Read/Find   O(1)  
Insertion   O(n)
Deletion    O(n)
Can do random access and read O(1) which is way faster

Linked List
Read/Find   O(n)
Insertion   O(1)
Deletion    O(1)
Can only do sequential access and this take time O(n) read

Chapter 2 Excerises (NOT CHECKED)
2.1: I would implement a linked list cause I want to add up the sums and
    not find or read anything from my list of finances. 

2.2: In a restaurant I would want to create a list of insertion and deletion that only
    require O(1) time when recieving the order and deleting the order after the chief has 
    cooked the meal. 
    
2.3: I would implement an array that uses random access memory that is required by BS.
    List can only do sequential access. Random access is O(1) which is a fast process. 
    
2.4: In the worst case senario inserting into an array we must move all the elements up 
    or down in memory. In addition, using an array we are limited or wasting space depending 
    on the size of the elements, we must make more space which is a O(n) process. 
    
2.5: The new hybrid structure would be faster. The insertion and deletion are now handled
    by the list. The reading is cut down significantly with the use of arrays random access,
    the starting of the letter, although the worst case can be argued that if all the 
    names started w A for example, then the search wont matter.

"""

# Selection Sort Algo O(n x n) = O(n^2)
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))


    
        

    
    