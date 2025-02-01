#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:09:36 2024

@author: tonystark
"""
"""
   Learnings :
    1. enumerate keyword - The enumerate function in Python is a built-in function that allows you 
    to loop over an iterable (like a list, tuple, or string) and have an automatic counter. 
    This is very useful when you need both the index and the value of each item in the iterable 
    during the iteration. enumerate(iterable, start=0)

    2. hashmap - In Python, a hashmap is implemented using the built-in dictionary data type. 
    A dictionary in Python is a collection of key-value pairs where each key is unique 
    and maps to a specific value. It provides average O(1) time complexity for 
    lookups, insertions, and deletions, making it an efficient data structure for many applications.
    
    Key Features of Python Dictionaries

    Key-Value Pairs: Each element in a dictionary is stored as a pair of a key and a value.
    Mutable: Dictionaries can be modified after their creation by adding, removing, or changing elements.
    Unordered: Prior to Python 3.7, dictionaries were unordered collections. Starting from Python 3.7, dictionaries maintain the insertion order of keys.
    Keys: Keys must be immutable (e.g., strings, numbers, tuples), and they must be unique within a dictionary.
    
    # Using curly braces
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    
    # Using the dict() function
    my_dict = dict(name='Alice', age=25, city='New York')
    
    # Modifying/Adding a key-value pair
    my_dict['age'] = 26          

    del my_dict['city']                     # Removes the key 'city'
    age = my_dict.pop('age')                # Removes the key 'age' and returns its value
    
    # Iterating over keys
    for key in my_dict:
        print(key)
    
    # Iterating over values
    for value in my_dict.values():
        print(value)
    
    # Iterating over key-value pairs
    for key, value in my_dict.items():
        print(key, value)

    
    3. array - List
    
    4. 
"""
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {} 
        for i,element in enumerate(nums):
            diff = target - element
            if diff in hashmap:
                return hashmap[diff], i
            else:
                hashmap[element] = i
                    



if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 17
    sol = Solution()
    result = sol.twoSum(nums, target)
    print(result)  