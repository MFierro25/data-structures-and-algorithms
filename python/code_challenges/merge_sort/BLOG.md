# Merge Sort

Today we will be taking an array and using a method to rearrange it by lowest to highest. we will be using the merge sort method
<br> this method takes in an array splits it into half, sorts the first half by splitting and comparing, does the same thing to the second
half and then brings both halfs back and arranges them again.

for our example we will be using this Pseudo Code:
  ```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
  ```
  
and this example array : <br>
[8,4,23,42,16,15]
  
below i will walk you through what this method is doing step by step

#### Step 1:

First thing we do is split our array into half and will have two halves to work with.
8, 4, 23 on the left and 42, 16, 15 on the right.

#### Step 2:

we will start with the first sub array [8, 4, 23] and split again:
[8, 4] and [23]
#### step 3: 
split one more time<br>
[8] [4] and [23]
will be left with something looking like this below:
![merge-1](/code_challenges/merge_sort/blog_assets/merge-1.png)

#### step 4
select the minimum between both these values and add to sorted array. copy second value into the array
now we have [4, 8] and [23]

#### step 5
since 23 cannot be split again it is ready for merge <br>
select the minimum value and merge back to the sorted array <br>
select second smallest value and merge to sorted array <br>
select the last value and merge back into the sorted array . 
will be left with below 
![merge-2](/code_challenges/merge_sort/blog_assets/merge-2.png)

#### step 6 
split the right side of the array
keep splitting until cant anymore and will be left with the bottom image <br>
![merge-3](/code_challenges/merge_sort/blog_assets/merge-3.png)

#### step 7
select the minumum of the 2 values so in ur case it is 16 and insert back to merge list
copy the remaining and insert to sorted list so this case will be 42 <br>
now these two values are finished merging

#### step 8
the last item of [15] cannot be split so we merge this back into our array in sorted order
with minimum first, so [15, 16, 42]
and will be left with this below 
![merge-4](/code_challenges/merge_sort/blog_assets/merge-4.png)

#### step 9
now that our two seperated lists are sorted we compare them with each other
so we compare the front value [4] to [15] and put the smallest value first

#### step 10 
we then compare the second value [8] to [15] again and [8] is lower so it gets added 

#### step 11
we keep comparing the front value [23] to [15] and this time since 15 is lower it gets added to the sorted list
we are left with this below ![merge-5](/code_challenges/merge_sort/blog_assets/merge-5.png)

#### step 12
this final process of comparing the two fron values gets repeated until we get left with our final product below
![merge-6](/code_challenges/merge_sort/blog_assets/merge-6.png)