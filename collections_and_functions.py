# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 16:00:48 2025

@author: bbatte

Assignment: Collections and Functions
"""

# =============================================================================
# Part 1: Tuples
# =============================================================================

# Question 1: Create and Access
tuple_fibonacci = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)
print(f"\nFibonacci tuple: {tuple_fibonacci}")
print(f"Third item in Fibonacci tuple: {tuple_fibonacci[2]}")

# Question 2: Tuple Modification (Workaround)
tuple_primes = (2, 3, 5, 7, 11)
print(f"\nPrime tuple: {tuple_primes}")
prime_list = list(tuple_primes)
prime_list.remove(7)
modified_primes = tuple(prime_list)
print(f"Modified primes (removed 7): {modified_primes}")

# Question 3: Tuple Unpacking
tuple_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
a, b, *middle, i, j = tuple_numbers
print(f"\na = {a}")
print(f"b = {b}")
print(f"Middle = {middle}")
print(f"i = {i}")
print(f"j = {j}")

# Question 4: Tuple to String
message = ('N', 'e', 'v', 'e', 'r', ' ', 'G', 'i', 'v', 'e', ' ', 'u', 'p')
print(f"\nMessage Characters: {message}")
message_string = ''.join(message)
print(f"Message: {message_string}")

# Question 5: Find Duplicates
tuple_with_duplicate = (4, 5, 1, 16, 45, 4, 3, 45, 1, 16, 25, 35, 1, 4, 15)

duplicates, seen = set(), set()
for n in tuple_with_duplicate:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

print(f"\nDuplicates in tuple_with_duplicate: {duplicates}")

# Question 6: Reverse Tuple
animals = ("goat", "cow", "lion", "sheep", "horse", "sheep")
print(f"\nAnimals tuple: {animals}")
print(f"Reversed Animals: {animals[::-1]}")

# =============================================================================
# Part 2: Lists
# =============================================================================

# Question 7: Sum of List
numbers = [3, 7, 1, 9, 2]
result = 0
for num in numbers:
    result += num
print(f"\nList of numbers to be added: {numbers}")
print(f"The sum of elements in the list is: {result}")

# Using sum() with list comprehension
list_squares = [n**2 for n in range(1, 8)]
print(f"\nSquares list: {list_squares}")
print(f"Sum of squares: {sum(list_squares)}")

# Question 8: Remove Duplicates
names = ["Ben", "John", "John", "Ben", "Joseph", "Bob", "Frank", "Bob",
         "Ben", "Peter", "Bob", "John"]

unique_names = []
for n in names:
    if n not in unique_names:
        unique_names.append(n)

print(f"\nOriginal names list: {names}")
print(f"List of names without duplicates (order preserved): {unique_names}")

# Question 9: Clone a List
make = ["Jeep", "Toyota", "Mazda", "Benz", "Honda"]

# Method 1: copy()
cloned_copy1 = make.copy()
# Method 2: slicing [:]
cloned_copy2 = make[:]
# Method 3: list() constructor
cloned_copy3 = list(make)

print(f"\nOriginal make list: {make}")
print(f"Cloned Copy 1 (using copy()): {cloned_copy1}")
print(f"Cloned Copy 2 (using slicing [:]): {cloned_copy2}")
print(f"Cloned Copy 3 (using list() constructor): {cloned_copy3}")

# Question 10: Combine Lists
languages = ["Python", "Java", "Go", "Rust"]
databases = ["MongoDB", "Redis", "SQLite", "PostgreSQL"]

combined = languages + databases

print(f"\nProgramming Languages: {languages}")
print(f"Databases: {databases}")
print(f"Combined List: {combined}")

# Question 11: Sort by Last Element in Tuple (Students and Scores)
students_score = [
    ("Anita", 98),
    ("James", 95),
    ("Ken", 99),
    ("Joseph", 96),
    ("Adam", 100),
    ("Smith", 93),
    ("Zira", 95),
    ("Ake", 97)
]

sorted_students = sorted(students_score, key=lambda x: x[-1])
print(f"\nOriginal List: {students_score}")
print(f"Sorted by score: {sorted_students}")

# Question 12: List Slicing
people = ["James", "Ken", "Ben", "John", "Smith", "Adam",
          "Anita", "Zira", "Joseph", "Bob"]

first_four_names = people[:4]
print(f"\nFull list of people: {people}")
print(f"First 4 names: {first_four_names}")

# =============================================================================
# Part 3: Sets
# =============================================================================

# Question 13: Create a Set
space_missions = {"Apollo 11", "Voyager 1", "Hubble",
                  "Artemis I", "James Webb"}
print(f"\nFamous space missions set: {space_missions}")

# Question 14: Set Intersection
string_instruments = {"Violin", "Guitar", "Cello", "Harp", "Banjo"}
percussion_instruments = {"Drums", "Cajon", "Tambourine", "Guitar", "Banjo"}

# Method: intersection()
common_instruments = string_instruments.intersection(percussion_instruments)
# Operator: &
common_instruments_using_and = string_instruments & percussion_instruments

print(f"\nString instruments: {string_instruments}")
print(f"Percussion instruments: {percussion_instruments}")
print(f"Common instruments (using intersection()): {common_instruments}")
print(f"Common instruments (using & operator): {common_instruments_using_and}")

# Question 15: Set Union
ancient_empires = {"Roman", "Greek", "Persian", "Egyptian"}
medieval_empires = {"Mongol", "Ottoman", "Byzantine", "Persian"}

# Method: union()
all_empires_method = ancient_empires.union(medieval_empires)
# Operator: |
all_empires_operator = ancient_empires | medieval_empires

print(f"\nAncient empires: {ancient_empires}")
print(f"Medieval empires: {medieval_empires}")
print(f"Union of empires (using union()): {all_empires_method}")
print(f"Union of empires (using | operator): {all_empires_operator}")




# =============================================================================
# Part 4: Functions
# =============================================================================

# Question 16: Multiply List Elements
def multiply_list(numbers):
    product = 1
    
    for num in numbers:
        product *= num
    return product

nums =[2, 5, 3, 5, 2, 5, 4]
result = multiply_list(nums)
print(f"\nOriginal list: {nums}")
print(f"Product of all elements: {result:}")

# Question 17: Statistics Function

def statistics(scores):
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores)/len(scores)
    return minimum, maximum, average

exam_scores = [94, 89, 99, 100, 95, 94, 98, 92, 97]

min_score, max_score, avg_score = statistics(exam_scores)
        
print(f"\nExam scores: {exam_scores}")
print(f"Minimum score: {min_score}")
print(f"Maximum score: {max_score}")
print(f"Average score: {avg_score:.2f}")


# Question 18: Check Range Membership

def in_range(target, lower, higher):
    """Check if target is within the inclusive range [lower, higher]."""
    return lower <= target <= higher

# Test cases
print(f"\nIs 15 between 10 and 20? {in_range(15, 10, 20)}")   
print(f"Is 10 between 10 and 20? {in_range(10, 10, 20)}")   
print(f"Is 20 between 10 and 20? {in_range(20, 10, 20)}")   
print(f"Is 5 between 10 and 20? {in_range(5, 10, 20)}")     
print(f"Is 25 between 10 and 20? {in_range(25, 10, 20)}")   


# Question 19: Dog Speed Analyzer


# Nested list of dog breeds with their max running speeds (mph)
dog_speeds = [
    ["Greyhound", 45],
    ["Saluki", 43],
    ["Afghan Hound", 40],
    ["Bulldog", 15],
    ["Beagle", 20],
    ["Whippet", 35]
]

def dog_speed_analyzer(dogs):
    """Return the fastest and slowest dog breeds from a nested list."""
    # Find fastest using max(), slowest using min(), based on speed
    fastest = max(dogs, key=lambda x: x[1])
    slowest = min(dogs, key=lambda x: x[1])
    return fastest, slowest

# Analyze dog speeds
fastest_dog, slowest_dog = dog_speed_analyzer(dog_speeds)

print(f"\nDog speeds: {dog_speeds}")
print(f"Fastest dog: {fastest_dog[0]} ({fastest_dog[1]} mph)")
print(f"Slowest dog: {slowest_dog[0]} ({slowest_dog[1]} mph)")
















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







