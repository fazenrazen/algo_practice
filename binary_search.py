
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

my_list = [1, 3, 5, 7, 9, 10]

print(binary_search(my_list, 9))
print(binary_search(my_list, -1))

"""
Common Big O Notations
O(log n) = Binary Search 
O(n) = Simple Search
O(n log n) = Quicksort
O(n^2) = Selection Sort
O(n!) = NP Problems

Chapter 1 Exercises (NOT CHECKED)
1.1: 128 max steps using BS will take 7 steps = log2 (128) = 7
1.2: 256 max steps using BS will take 8 steps = log2 (128 * 2) = 8  
1.3: BS or O(log n) on trying to find a persons name in a phone book 
1.4: O(n) because you go through each person in the book since you are only given the 
    phone number which can vary in value
1.5: O(n) worst case senario, the person can be the last item
1.6: You find all people w A's in the list so O(n), worst case the list can be all A's


"""        
        
