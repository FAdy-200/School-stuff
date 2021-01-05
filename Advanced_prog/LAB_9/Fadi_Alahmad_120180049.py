# CSE314- Lab 9
#
# Topic: Search
# Author : Fadi Alahmad 120180049
# Date : 05/01/2021
# Question 1:

def ransom(ransomNote, magazine):
    m = list(magazine)
    c = 0
    for i in ransomNote:
        for j in range(len(m)):
            if i == m[j]:
                m[j] = None
                c += 1
                break
    if c == len(ransomNote):
        return True
    return False


# Test cases
# n = "aa"
# m = "aab"
# print(ransomNote(n, m))


# Question 2:

def binary(arr, t):
    low = 0
    high = len(arr)
    mid = (low + high) // 2
    while arr[mid] != t and low < high - 1:
        if t > arr[mid]:
            low = mid
        else:
            high = mid
        mid = (low + high) // 2
    if low < high - 1:
        return mid
    return -1


# Test cases
# nums = [-1, 0, 3, 5, 9, 12]
# t = 9
# print(binary(nums, t))


# Question 3:

def towerOfHanoi(n, fr, to, aux):
    if n == 1:
        print("Move disk from ", fr, "to", to)
        return
    towerOfHanoi(n - 1, fr, aux, to)
    print("Move from", fr, "to", to)
    towerOfHanoi(n - 1, aux, to, fr)
