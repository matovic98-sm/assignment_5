# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

#Original Solution: numbers.count()
# def most_frequent(numbers):
#     most_common = None
#     highest_count = 0

#     for number in numbers:
#         count = numbers.count(number)
#         if count > highest_count:
#             highest_count = count
#             most_common = number
#     return most_common


#Optimized Solution: Dictionary
def most_frequent(numbers):
    counts = {}
    
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    
    most_common = None
    highest_count = 0
    
    for number in counts:
        if counts[number] > highest_count:
            highest_count = counts[number]
            most_common = number
    return most_common

print(most_frequent([1, 3, 2, 3, 4, 1, 3]))
print(most_frequent([]))
print(most_frequent([1, 2, 3, 4, 5]))
print(most_frequent([0]))
print(most_frequent([2, 2, 4, 4, 6, 6]))


"""
Time and Space Analysis for problem 1:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""
#Time and Space Analysis for problem 1 Original Solution:
#Best-case: O(n^2) because the function uses a loop to process the numbers and then numbers.count() to count the 
#occurrences of each number.
#Worst-case: O(n^2) because even if every number is unique, the function must still loop through every number and
#then call numbers.count() for each number to count the number of occurrences.
#Average-case: O(n^2) because the behavior of the function doesn't change based on the input and will always have
#to scan through every number to process and again for each number processed to count the number of occurrences.
#Space complexity: O(1) because the function uses a fixed amount of variables and doesn't create more data 
#structures that grow with the input.
#Why this approach? I used numbers.count() to find out how many times each number appears, then compared the counts
#to determine which number appeared with the greatest frequency.
#Could it be optimized? Yes, using a dictionary would be a way to optimize this solution because it can store
#the count of each number, meaning the function can count each number in one loop and find the highest count in 
#a second loop rather than looping through each item in the list and calling numbers.count() for every number in
#the list. A trade-off of using a dictionary is the additonal space needed, but it greatly reduces the amount 
#of work the function needs to do as input grows.

#Performance and Space Usage Compared to Original Solution
#Compared to the original solution with a time complexity of O(n^2) and a space complexity of O(1), the 
#optimized solution has a time and space complexity of O(n). While the dictionary version uses additional 
#memory to store the numbers and their counts as key value pairs, this means that the function avoids having
#to loop through each number and having to call numbers.count() for each number in the loop to search for counts.
#Instead, the dictionary stores the numbers and counts in one loop and uses a separate loop to compare the counts. 
#This makes it a more efficient approach to the problem. 




# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result

print(remove_duplicates([4, 5, 4, 6, 5, 7]))
print(remove_duplicates([]))
print(remove_duplicates([1, 2, 3, 4, 5, 6]))
print(remove_duplicates([2, 2, 4, 4, 6, 6]))
print(remove_duplicates([5, 2, 5, 3, 2, 1]))

"""
Time and Space Analysis for problem 2:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""
#Time and Space Analysis for problem 2:
#Best-case: O(n) because the function must check every number even if there are no duplicates.
#Worst-case: O(n) because the function checks every number and uses set lookups to determine if a number was
#already seen.
#Average-case: O(n) because the function does one loop through the input and uses set operations that generally
#take a constant amount of time.
#Space complexity: O(n) because the set and result list can both grow as the input grows.
#Why this approach? I chose this approach because using a set works well for tracking duplicates, and adding 
#the resulting numbers to the result list preserves order.
#Could it be optimized? As the function has a Big O of O(n) which is linear with the size of its input, changing
#the solution would likely not result in an overall improved Big O time complexity. One trade-off with the current
#solution is that the set and result list use additional memory, but using the set prevents having to repeatedly
#search through the result list.


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        needed = target - number
        if needed in seen:
            pairs.append((needed, number))
        seen.add(number)
    return pairs

print(find_pairs([1, 2, 3, 4], 5))
print(find_pairs([], 5))
print(find_pairs([0], 4))
print(find_pairs([3, 4, 5, 6], 6))

"""
Time and Space Analysis for problem 3:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""
#Time and Space Analysis for problem 3:
#Best-case: O(n) because the function must check every number even if there are no pairs found.
#Worst-case:  O(n) because loops through each number and uses set lookups to see if the needed number was seen.
#Average-case: O(n) because the function loops through each number once and uses set operations that generally
#take a constant amount of time
#Space complexity: O(n) because the set can store numbers and the pairs list can grow as pairs are found.
#Why this approach? Using a set allows the function to check if a needed number was already seen without having
#to use a nested loop to compare every possible pair.
#Could it be optimized? Another solution may use less additional memory, but as both the time and space complexity
#are O(n), changing the solution likely wouldn't result in an overall improved time complexity. The trade-off
#present in this solution is that the set requires additional memory, but it allows the function to find pairs
#without having to repeatedly loop through the list and compare every possible pair.


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 4
    items = []

    for i in range(n):
        if len(items) == capacity:
            print("Resizing from", capacity, "to", capacity * 2)
           
            new_items = []
           
            for item in items:
                new_items.append(item)
            
            items = new_items
            capacity = capacity * 2
       
        items.append(i)
    
    print("Final List:", items)

add_n_items(6)
add_n_items(0)
add_n_items(1)
add_n_items(4)
add_n_items(5)
add_n_items(8)
add_n_items(24)

"""
Time and Space Analysis for problem 4:
- When do resizes happen?
- What is the worst-case for a single append?
- What is the amortized time per append overall?
- Space complexity:
- Why does doubling reduce the cost overall?
"""
#Time and Space Analysis for problem 4:
#When do resizes happen? Resizes happen when the list is at capacity and the function is about to append another
#item. For example, if the capacity is 4, a resize would occur when the 5th item is about to be added and the 
#capacity then doubles.
#Worst-case for a single append? O(n) when the list needs to be resized and its items need to be copied over to 
#the new list
#Amortized time per append overall? O(1) because most appends are fast and the slower resizing only happens occasionally.
#Space complexity: O(n) because the list grows with number of items and because during resizing, a second list is
#created to copy over the values in the full list.
#Why does doubling reduce the cost overall? Doubling reduces the cost overall because it increases the list's
#capacity and slows down the rate in which resizes happen.


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    total = 0

    for number in nums:
        total += number
        result.append(total)
    return result

print(running_total([1, 2, 3, 4]))
print(running_total([]))
print(running_total([10]))
print(running_total([5, 6, 7, 8]))
print(running_total([-2, -4, -6, 3]))

"""
Time and Space Analysis for problem 5:
- Best-case:
- Worst-case:
- Average-case:
- Space complexity:
- Why this approach?
- Could it be optimized?
"""
#Time and Space Analysis for problem 5:
#Best-case: O(n) because the function loops through each number in the input list.
#Worst-case: O(n) because it processes every number without any early exits or nested loops.
#Average-case: O(n) because the function always loops through every number once.
#Space complexity: O(n) because the result list stores one running total for every number in the input.
#Why this approach? Using a total variable to keep track of the current sum and the result list to store each 
#running total avoids needing to constantly recalculate the sum of all previous numbers.
#Could it be optimized? The solution already has a Big O of O(n) time and space complexity, so optimization
#likely wouldn't result in an improved time complexity. One trade-off is that the new list created requires O(n)
#additional memory, but it preserves the original input list and stores the running totals in one loop.
