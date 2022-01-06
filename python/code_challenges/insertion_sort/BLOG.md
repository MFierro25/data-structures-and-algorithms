# Insertion Sort

Today we will be taking an array and using a method to rearrange it by lowest to highest. we will be usint the insertion sort method
we begin by comparing the first two values agains each other, organizing them and then walking down the array to compare the rest of the values.
  
for our example we will be using this Pseudo Code:
  ```
    InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
  ```
  
and this example array : <br>
[8,4,23,42,16,15]
  
below i will walk you through what this method is doing step by step
  
#### Step 1:
we will insert our array into our method, we get the length of our array and set our variables. <br> 
J = first item in array <br>
I = second item in array <br>
and our temporary value which for now will be the highest value will be equal to the value of i
so after we insert this example we are left with this below.
![step 1](/python/code_challenges/insertion_sort/blog_assets/step-1.png)
#### Step 2:
we get to test our while loop, since temp is < arr[j] or ( 4 < 8) 
we then move j + 1 so we move it to the right and set that value to arr[j] or in this case 8.
then j is reassigned the value j - 1 = 0 - 1 = -1 we try check the while loop again and since j is less than 0 we do not enter
and instead the first index is assigned the value of 4
  
so we end up with <br>
[ 4, 8, 23, 42, 16, 15]
  
we step back into our for loop. now i is 2 and j is 1
and since temp is list[1] our new temp value is 15 so we get left with this below:
![step 3](/python/code_challenges/insertion_sort/blog_assets/step-3.png)
  
we check our while loop if J is >=0 which is true, then we check if temp is < arr[j] which is false. 
we do not enter the while loop and instead leave the array as is and move to the next step in the for loop. so we are left with
the same array that we entereed with : <br>
[ 4, 8, 23, 42, 16, 15]
  
#### step 4:
back in our for loop for the 3rd time we set 
i = 3 <br>
J = i - 1 (j = 3 -2) = 2 <br>
temp = arry[1] = 42 <br>
so we are left with the picture below <br>
![step 4](/python/code_challenges/insertion_sort/blog_assets/step-4.png)
  
after this we check our while loop and j >= 0 is true and 42 is not < 23 so the second part is false , 
we do not enter the while loop and instead move j + 1 so now we have moved down the array once more
we end up with same array we entered with <br>
[ 4, 8, 23, 42, 16, 15]
  
#### step 5:
this is where things get interesting. we are back in the for loop for the 4th time
i = 4 <br>
j = (i - 1 ) = 3 <br>
temp = list[4] = 16  <br>
and we are left with the below image
![step 5](/python/code_challenges/insertion_sort/blog_assets/step-5.png)
  
ima break down the next couple steps slowly:
- check while loop j >= 0 which is true
- check temp < arr[j] which is also true
- enter the while loop, now j+1 = arr[j] so 42 takes the place of where 16 was
- then j - 1 = 2 and we go through the while loop and check index 2 (23) vs our current temp of 16
- image below 
- ![step5.2](/python/code_challenges/insertion_sort/blog_assets/step-5.2.png)
- since both things are true once again 
- we move 23 to the right once more ( arr[j + 1] = list[j] )
- and J moves to the left again ( j = j - 1 )
now we are left with this below 
![step 5.3](/python/code_challenges/insertion_sort/blog_assets/step-5.3.png)
> notice our temp value has not changed, it is still 16, the only things that have changed is j and the placement of those values
- again we check our while loop again, this time the first part is true j >= 0 but the second is false we set j + 1 as our temp
- so this takes that empty area and places 16 in there 
- now we are left with the following <br> 

[ 4, 8, 16, 23, 42, 15]

#### step 6:
we repeat step 5 and since this time our temp is 15 we will go down again and end up with 15 in between 8 and 16 and will look like the image below
![step 6](/python/code_challenges/insertion_sort/blog_assets/step-6.png)

#### step 7:
for our final step since we have completed our for loop, we can leave this loop and do the last part of the method
which is return the list and the returned list will be <br>

[4, 8, 15, 16, 23, 42]
