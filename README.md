# Algorithm-implementations 
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fthegergo02%2FAlgorithm-implementations.svg?type=shield)]

## insertion-sort.py
### How does it work?
![Insertion Sort algorithm visualisation](https://upload.wikimedia.org/wikipedia/commons/4/42/Insertion_sort.gif)

Insertion Sort (I'm going to call it "the algorithm", I don't want to type too much), sort one element at the time. It's not efficient on a large number of data.
### Then where you can use it?
* If you have an almost sorted data set, it will be a lot faster than any algorithm.
* It can sort the data set while it receives it.
* It's really simple to implement, you can create a three-line version of it in C.

```c
for (i = 1; i < n; i++)
  for (j = i; j > 0; j--)
    if (a[j] < a[j-1]) swap(a[j], a[j-1])
```
### Example
```
$: python insertion-sort.py 1 7 3 4 8 2 3 5 9 10 
[1, 7, 3, 4, 8, 2, 3, 5, 9, 10]
[1, 2, 3, 3, 4, 5, 7, 8, 9, 10]
```
##  insertion-sort-nonincreasing.py
It's the same as the 'insertion-sort.py', just it puts the array in decreasing order.
### Example
```
$: python insertion-sort-nonincreasing.py 1 3 3 5 4
[1, 3, 3, 5, 4]
[5, 4, 3, 3, 1]
```
## linearsearch.py
### How does it work?
![Linear Search algorithm visualisation](https://image.slidesharecdn.com/ch12searchlinearbinary-150930234148-lva1-app6891/95/linear-search-binary-search-2-638.jpg/cb=3D1443658121&f=1)
"It sequentially checks each element of the list until a match is found or the whole list has been searched." - Wikipedia
So we enumerate through the numbers we search in, an check for our value.
### Example
```
$: python linearsearch.py 1 0 2 3 4 1 6 7
1
[0, 2, 3, 4, 1, 6, 7]
4
5
```

## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fthegergo02%2FAlgorithm-implementations.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fthegergo02%2FAlgorithm-implementations?ref=badge_large)