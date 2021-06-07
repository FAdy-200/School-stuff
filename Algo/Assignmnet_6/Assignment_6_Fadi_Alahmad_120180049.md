<p style="font-family: times; font-size:18pt">
    Name: Fadi Alahmad Alomar</br>ID: 120180049
</p>

# Assignment 6: Dynamic Programming

## Question 1

**(a)**
$$
LCS(A,B,i,j) =
\left\{
 \begin{array}{ll}
  0  & {if \space} i = 0 \space or \space j=0 \\
  max(1+LCS(A,B,i-1,j-1),LCS(A,B,i-1,j),LCS(A,B,i,j-1),\\LCS(A,B,i-1,j-1)) & {if \space A[i]=B[j]} \\
        max(LCS(A,B,i-1,j-1),LCS(A,B,i-1,j),LCS(A,B,i,j-1),\\LCS(A,B,i-1,j-1)) & {if \space A[i]!=B[j]}
 \end{array}
\right.
$$
**(b)**
$$
SCS(A,B,i,j) =
\left\{
 \begin{array}{ll}
  0  & {if \space} i = 0 \space and \space j=0 \\
  i &{if \space} i!=0 \space and \space j=0\\
  j &{if \space} i=0 \space and \space j!=0\\
  1+SCS(A,B,i-1,j-1) & {if \space A[i]=B[j]} \\
        min(1 + SCS(A,B,i-1,j-1),1+SCS(A,B,i-1,j),1+SCS(A,B,i,j-1)) & {if \space A[i]!=B[j]}
 \end{array}
\right.
$$
**(c)**
$$
LIS(X,i,j) =
\left\{
 \begin{array}{ll}
        0 & {if\space} i = 0\\
        max(1+LIS(X,i-1,i),LIS(X,i-1,j)) &if \space X[j]>X[i]
 \end{array}
\right.
$$
$$
RDS(X,i,j) =
\left\{
 \begin{array}{ll}
        0 & {if\space} i = len(X)\\
        max(1+RDS(X,i+1,i),RDS(X,i+1,j)) &if \space X[j]<X[i]
 \end{array}
\right.
$$
$$
LBS(X,i) =
\left\{
 \begin{array}{ll}
        0 & if i = len(X)-2\\
        max(LBS(X,i+1),1+LIS(X,i,i)+RDS(X,i,i)) & otherwise
 \end{array}
\right.
$$
**(d)**
$$
LOSLOW(X,i,j) =
\left\{
 \begin{array}{ll}
        0 & if\space j>|X|\\
        LOSLOW(X,i,j+1)& if \space X[i]>x[j]\\
        max(LOSLOW(i,j+1),1+LOSHIGH(i,j+1))
 \end{array}
\right.
$$
$$
LOSHIGH(X,i,j) =
\left\{
 \begin{array}{ll}
        0 & if\space j>|X|\\
        LOSLOW(X,i,j+1)& if \space X[i]<x[j]\\
        max(LOSLOW(i,j+1),1+LOSHIGH(i,j+1))
 \end{array}
\right.
$$
$$
LOS(X) = max_i(LOSLOW(X,i,i+1)+1)
$$
**(e)**
$$
SOSHIGH(X,i) =
\left\{
 \begin{array}{ll}
        0 & if \space i = len(X)-1\\
        SOSHIGH(X,i+1)& if X[i]<X[i+1]\\
        SOSHIGH(X,i+1)+1  & otherwise
 \end{array}
\right.
$$
$$
SOSLOW(X,i) =
\left\{
 \begin{array}{ll}
        0 & if \space i = len(X)-1\\
        SOSLOW(X,i+1)& if X[i]>X[i+1]\\
        SOSLOW(X,i+1)+1  & otherwise
 \end{array}
\right.
$$
$$
SOS(X) = min(SOSLOW(X),1+SOSHIGH(X))
$$
**(f)**
$$
LXS(X,j,i,k) =
\left\{
 \begin{array}{ll}
        0 & if\space k>|X|\space or\space  i>k \space or \space j>i\\
        max(1+LXS(X,j+1,i+1,k+1),LXS(X,j,i+1,k),LXS(X,j+1,i,k),\\LXS(X,j,i,k+1))& if \space 2X[i]<X[j]+x[k]\\
        max(LXS(X,j+1,i+1,k+1),LXS(X,j+1,i+1,k),\\LXS(X,j,i+1,k+1),LXS(X,j+1,i,k+1),LXS(X,j,i+1,k),\\LXS(X,j+1,i,k),LXS(X,j,i,k+1)) &otherwise
 \end{array}
\right.
$$

## Question 2

**(a)**

```python
def checkSubsequence(x, y, i):
    if len(y) == 0:
        return False
    if i == len(x):
        return True
    if x[i] == y[0]:
        return checkSubsequence(x, y[1:], i + 1) or checkSubsequence(x, y[1:], i)
    return checkSubsequence(x, y[1:], i)
```

**(b)**

```python
def smallestSymbolsToBeRemoved(x, y):
    if len(y) < len(x):
        return 0
    elif len(x) == 0:
        return len(y)
    if not checkSubsequence(x, y, 0):
        return 0
    if x[0] == y[0]:
        return min(1 + smallestSymbolsToBeRemoved(x, y[1:]), smallestSymbolsToBeRemoved(x[1:], y))
    return smallestSymbolsToBeRemoved(x, y[1:])

```

**(c)**

```python
def checkTwiceOccurrence(x, y, i1=0, i2=0):
    if len(y) == 0:
        return False
    if i1 == len(x):
        return checkSubsequence(x, y, i2)
    if i2 == len(x):
        return checkSubsequence(x, y, i1)
    if x[i1] == y[0] and x[i2] == y[0]:
        a <- checkTwiceOccurrence(x, y[1:], i1 + 1, i2)
        b <- checkTwiceOccurrence(x, y[1:], i1, i2 + 1)
        c <- checkTwiceOccurrence(x, y[1:], i1, i2)
        return a or b or c
    elif x[i1] == y[0]:
        return checkTwiceOccurrence(x, y[1:], i1 + 1, i2) or checkTwiceOccurrence(x, y[1:], i1, i2)
    elif x[i2] == y[0]:
        return checkTwiceOccurrence(x, y[1:], i1, i2 + 1) or checkTwiceOccurrence(x, y[1:], i1, i2)
    return checkTwiceOccurrence(x, y[1:], i1, i2)

```

## Question 3

**(a)**

```python
def LSCS(x):
    currentMax = -math.inf
    maxSoFar = 0
    for i in x:
        currentMax <- currentMax + i
        maxSoFar <- max(currentMax, maxSoFar)
        currentMax <- max(currentMax, 0)
    return maxSoFar
```

the algorithm loops on the array once and does $\mathcal{O}(1)$ work thus the algorithm has a runtime of $\mathcal{O}(n)$

**(b)**

```python
def prod(x):
    mostNegative = x[0]
    mostPositive = x[0]
    current = x[0]
    for int i= 0, i < len(x), i++:
        if x[i] < 0:
            mostPositive, mostNegative = mostNegative, mostPositive
        mostPositive = max(x[i], mostPositive * x[i])
        mostNegative = min(x[i], mostNegative * x[i])
        current = max(current, mostNegative, mostPositive)
    return current
```

the algorithm loops on the array once and does $\mathcal{O}(1)$ work thus the algorithm has a runtime of $\mathcal{O}(n)$
