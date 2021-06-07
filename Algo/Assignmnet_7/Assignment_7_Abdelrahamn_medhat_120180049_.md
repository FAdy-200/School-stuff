<p style="font-family: times; font-size:18pt">
    Name: Abdelrahman Medhat Saad Nawar</br>ID: 120180025
</p>
  
#  Assignment 7: Dynamic Programming
  
  
##  Question 1
  
  
as the matrix is not sorted in a way that makes doing a modified binary search possible we will be searching for the element by:
  
1. we start form the element in the first row and last column
2. if we are at an element that is bigger than the one we search for we go to the element to the left of it
3. if it is smaller we go to the element we go to the element under it
  
**Time complexity:**
since on each iteration we either increase i or decrease j we can only go <img src="https://latex.codecogs.com/gif.latex?2n"/> iterations and in each one we only do a simple comparison
<img src="https://latex.codecogs.com/gif.latex?&#x5C;therefore%20&#x5C;mathcal{O}(n)"/>
**Space complexity:**
<img src="https://latex.codecogs.com/gif.latex?&#x5C;mathcal{O}(1)"/>
  
##  Question 2
  
  
it is not efficient as it has a lot of redundant calls and will calculate some values more than once, a way to improve it is to use memoization technique and store the value of each call once it is done so it will only be done once
  
##  Question 3
  
  
1. We start traversing from <img src="https://latex.codecogs.com/gif.latex?i%20=%200,%20j%20=%200"/> until we get any out of range values.
   this way in each iteration we will not calculate every value it will rather be calculated in on of  the iterations that happened before it.
  
2. In this recursive call the function will always go to the diagonal values and evaluate them.
   thus we can traverse it in any order as long as we find the diagonal values first.
   we can calculate the diagonal value of each row first then loop on that row
  
3. there is no way of traversing that will solve this problem as in each other call we will be back calculating the same values.
   e.g.
   <img src="https://latex.codecogs.com/gif.latex?i%20=%203,%20j%20=%203"/> will lead to <img src="https://latex.codecogs.com/gif.latex?i%20=%201,j=1"/> and <img src="https://latex.codecogs.com/gif.latex?i%20=%205,j=5"/> which will give 
   <img src="https://latex.codecogs.com/gif.latex?i%20=%203,%20j%20=%203"/> and <img src="https://latex.codecogs.com/gif.latex?i%20=%207,j=7"/>
  
##  Question 4
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?MC(i,j)%20=&#x5C;left&#x5C;{%20&#x5C;begin{array}{ll}%20%20%20%20%20%20%20%200%20&amp;%20{if&#x5C;space}%20i%20=%20j+1&#x5C;&#x5C;%20%20%20%20%20%20%20%20min_{i&lt;k&lt;j}(MC(k,j)+MC(i,k)+(d_j-d_i))%20&amp;%20otherwise%20&#x5C;end{array}&#x5C;right."/></p>  
  
**Time complexity:**
The work needed in each call is <img src="https://latex.codecogs.com/gif.latex?&#x5C;mathcal{O}(n)"/> in order to do the summation and finding the minimum value.
 and we need to evaluate a total of <img src="https://latex.codecogs.com/gif.latex?&#x5C;mathcal{O}(n^2)"/> points
<img src="https://latex.codecogs.com/gif.latex?&#x5C;therefore%20&#x5C;mathcal{O}(n^3)"/>
**Space complexity:**
we need a matrix that is <img src="https://latex.codecogs.com/gif.latex?n*n"/> to hold intermediate values
<img src="https://latex.codecogs.com/gif.latex?&#x5C;therefore%20&#x5C;mathcal{O}(n^2)"/>
  
##  Question 5
  
  
We need first to calculate the total number of ways to get from <img src="https://latex.codecogs.com/gif.latex?s"/> to <img src="https://latex.codecogs.com/gif.latex?t"/>.
we do this by exploring every path from <img src="https://latex.codecogs.com/gif.latex?s"/> to <img src="https://latex.codecogs.com/gif.latex?t"/> in topological order.
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Paths(s,t)%20=&#x5C;left&#x5C;{%20&#x5C;begin{array}{ll}%20%20%20%20%20%20%20%201%20&amp;%20{if&#x5C;space}%20s%20=%20t&#x5C;&#x5C;%20%20%20%20%20%20%20%20&#x5C;sum_{(s,i)%20&#x5C;in%20E%20}{Paths(i,t)}%20&amp;%20otherwise%20&#x5C;end{array}&#x5C;right."/></p>  
  
**Time complexity:**
since we need to visit every edge and vertices and all intermediate values will be stored so it wont be calculated more that once
<img src="https://latex.codecogs.com/gif.latex?&#x5C;mathcal{O}(|V|+|E|)"/>
**Space complexity:**
we need a matrix to hold the values of the vertices we are at to reach <img src="https://latex.codecogs.com/gif.latex?t"/>
<img src="https://latex.codecogs.com/gif.latex?&#x5C;therefore"/> space complexity is <img src="https://latex.codecogs.com/gif.latex?&#x5C;mathcal{O}(|V|)"/>
  