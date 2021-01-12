# Question 1
a) Insertion sort:
[8,1,4,1,5,9,2,6,5]
swap(arr[0],arr[1])
[1,8,4,1,5,9,2,6,5]
swap(arr[1],arr[2])
[1,4,1,8,5,9,2,6,5]
swap(arr[0],arr[1])
[1,1,4,8,5,9,2,6,5]
swap(arr[4],arr[3])
[1,1,4,5,8,9,2,6,5]
swap(arr[6],arr[5])
[1,1,4,5,8,2,9,6,5]
swap(arr[5],arr[4])
[1,1,4,5,2,8,9,6,5]
swap(arr[4],arr[3])
[1,1,4,2,5,8,9,6,5]
swap(arr[3],arr[2])
[1,1,2,4,5,8,9,6,5]
swap(arr[7],arr[6])
[1,1,4,2,5,8,6,9,5]
swap(arr[6],arr[5])
[1,1,4,2,5,6,8,9,5]
swap(arr[8],arr[7])
[1,1,4,2,5,6,8,5,9]
swap(arr[7],arr[6])
[1,1,4,2,5,6,5,8,9]
swap(arr[6],arr[5])
[1,1,4,2,5,5,6,8,9]

b) Heap sort:
max heapify arr
[9,6,8,5,5,4,2,1,1]
swap(arr[0],arr[-1])
[1,6,8,5,5,4,2,1,9]
heapify arr[:-1]
[8,6,4,5,5,1,2,1,9]
swap(arr[0],arr[-2])
[1,6,4,5,5,1,2,8,9]
heapify arr[:-2]
[6,5,4,1,5,1,2,8,9]
swap(arr[0],arr[-3])
[2,5,4,1,5,1,6,8,9]
heapify arr[:-3]
[5,5,4,1,2,1,6,8,9]
swap(arr[0],arr[-4])
[1,5,4,1,2,5,6,8,9]
heapify arr[:-4]
[5,2,4,1,1,5,6,8,9]
swap(arr[0],arr[-5])
[1,2,4,1,5,5,6,8,9]
heapify arr[:-5]
[4,2,1,1,5,5,6,8,9]
swap(arr[0],arr[-6])
[1,2,1,4,5,5,6,8,9]
heapify arr[:-6]
[2,1,1,4,5,5,6,8,9]
swap(arr[0],arr[-7])
[1,1,2,4,5,5,6,8,9]

c) Merge sort

d) Quick sort by followin the psudo code provided
[8, 1, 4, 1, 5, 9, 2, 6, 5] ,p = 5 ,l = 0 ,r = 8
[8, 1, 4, 1, 5, 9, 2, 6, 5] the important part of the array on which the algorithm is working
swapping arr[0], arr[8]
array after swapping = [5, 1, 4, 1, 5, 9, 2, 6, 8] ,l = 1 ,r = 7
swapping arr[4], arr[6]
array after swapping = [5, 1, 4, 1, 2, 9, 5, 6, 8] ,l = 5 ,r = 5
swapping arr[5], arr[6]
array after swapping = [5, 1, 4, 1, 2, 5, 9, 6, 8] ,l = 5 ,r = 4
[5, 1, 4, 1, 2, 5, 9, 6, 8] full array after modification

[5, 1, 4, 1, 2, 5, 9, 6, 8] ,p = 6 ,l = 6 ,r = 8
[9, 6, 8] the important part of the array on which the algorithm is working
swapping arr[6], arr[7]
array after swapping = [6, 9, 8] ,l = 7 ,r = 6
swapping arr[6], arr[6]
array after swapping = [6, 9, 8] ,l = 7 ,r = 6
[5, 1, 4, 1, 2, 5, 6, 9, 8]

[5, 1, 4, 1, 2, 5, 6, 9, 8] ,p = 9 ,l = 7 ,r = 8
[9, 8] the important part of the array on which the algorithm is working
swapping arr[7], arr[8]
array after swapping = [8, 9] ,l = 8 ,r = 7
swapping arr[8], arr[8]
array after swapping = [8, 9] ,l = 8 ,r = 7
[5, 1, 4, 1, 2, 5, 6, 8, 9] full array after modification

[5, 1, 4, 1, 2, 5, 6, 8, 9] ,p = 4 ,l = 0 ,r = 4
[5, 1, 4, 1, 2] the important part of the array on which the algorithm is working
swapping arr[0], arr[4]
array after swapping = [2, 1, 4, 1, 5] ,l = 1 ,r = 3
swapping arr[2], arr[3]
array after swapping = [2, 1, 1, 4, 5] ,l = 3 ,r = 2
swapping arr[3], arr[3]
array after swapping = [2, 1, 1, 4, 5] ,l = 3 ,r = 2
[2, 1, 1, 4, 5, 5, 6, 8, 9] full array after modification

[2, 1, 1, 4, 5, 5, 6, 8, 9] ,p = 1 ,l = 0 ,r = 2
[2, 1, 1] the important part of the array on which the algorithm is working
swapping arr[0], arr[2]
array after swapping = [1, 1, 2] ,l = 1 ,r = 1
swapping arr[1], arr[1]
array after swapping = [1, 1, 2] ,l = 2 ,r = 0
[1, 1, 2, 4, 5, 5, 6, 8, 9] full array after modification

[1, 1, 2, 4, 5, 5, 6, 8, 9] ,p = 1 ,l = 0 ,r = 1
[1, 1] the important part of the array on which the algorithm is working
swapping arr[0], arr[1]
array after swapping = [1, 1] ,l = 1 ,r = 0
[1, 1, 2, 4, 5, 5, 6, 8, 9] full array after modification

[1, 1, 2, 4, 5, 5, 6, 8, 9]  Final result




# Question 3
transfer the two strings into arrays then sort them using heap sort, each charecter has an ascii value thus it can be treated as a number when comparing it to other charecters
going through bith the arrays and if they arer the same then the words are an anagrams if the arrays are not the same then the words are not an anagrams

arr1=[1,4,8], arr2=[5,9]
i = 0 ,j = 0
ansArr=[NULL,NULL,NULL,NULL,NULL]
arr1[i] < arr2[j] so i = i+1 and ansArr[i] = arr1[i]
i = 1, j = 0
ansArr=[1,NULL,NULL,NULL,NULL]
arr1[i] < arr2[j] so i = i+1 and ansArr[i] = arr1[i]
i = 2, j = 0
ansArr=[1,4,NULL,NULL,NULL]
arr1[i] > arr2[j] so j = j+1 and ansArr[j] = arr2[j]
i = 2, j = 1
ansArr=[1,4,5,NULL,NULL]
arr1[i] < arr2[j] so i = i+1 and ansArr[i] = arr1[i]
i = 3, j = 1
ansArr=[1,4,5,8,NULL]
i is out of range so ansArr[j:] = arr2[j:]
ansArr=[1,4,5,8,9]

First, we need to make it that once each iteration is done the pivot is in it is right place after sorting and is not going to be moved, after that if the number of elements is odd, we need to find the n/2 element, if it is even, we need to find the n//2, n//2 + 1, elements and add them then divide them by 2.
We find the element in a position X by doing quick sort with the pivot being the middle element, and seeing if the new pivot location is X, greater than X or smaller than X. if it is X then the pivot element is the one we are looking for, if it is greater then we quick sort the side of the array that is to the left of the pivot and if it is smaller than X then we quick sort the side of the array that is to the right of the pivot.

He should go wtih bubble sort as the implementation stops once it finds a pair that needs no swapping it breaks.
in his case the swapping will happen for one iteration as the naughty boy only shifted once thus the bubble sort alogrithm will swap the first element with every element untill it is at the end then once it starts the secound iteration the alogrithm will find that there is no swapping needed as the elements are sorted and breaks.
thus doing the sorting in O(n)

Pivot Location in subarray = 3
subarray = [2, 1, 4, 9, 3, 5, 18]
The arrangement of the numbers = [2, 1, 4, 5, 3, 9, 18]

Pivot Location in subarray = 0
subarray = [9, 18]
The arrangement of the numbers = [2, 1, 4, 5, 3, 9, 18]

Pivot Location in subarray = 2
subarray = [2, 1, 4, 5, 3]
The arrangement of the numbers = [2, 1, 3, 5, 4, 9, 18]

Pivot Location in subarray = 0
subarray = [5, 4]
The arrangement of the numbers = [2, 1, 3, 4, 5, 9, 18]

Pivot Location in subarray = 1
subarray = [2, 1, 3]
The arrangement of the numbers = [1, 2, 3, 4, 5, 9, 18]

Pivot Location in subarray = 0
subarray = [2, 3]
The arrangement of the numbers = [1, 2, 3, 4, 5, 9, 18]


