#######################   ALGORITHM    ####################
'''

step 1 : Read the size of an array n from the keyboard .
step 2 : Initialize the array elements from the index 0 to n-1 .
step 3 : for i -> 0 to i -> n-1 if it is satisfy put the value of i into new varibale index goto step 4 .
step 4 : for j -> i+1 to j-> n ,
         check the condition a[i] >= a[j] if it is true put the value of the j into index
        if value of index and i is not same swap a[i]  and a[index] .
step 5 : End .

'''
#######################      CODE      ####################


# Read the size of an array from the user
n  = int(input("Enter the size of an array : "))
a = [] # Declare the array

# Read the elements of an array  from the user
for i in range(n):
    value = int(input("Enter the array element : "))
    a.append(value) # store the value  into array

print("Array elements before sorting : ",end=" ")
for i in a:
    print(i,end =" ")
print()
#  Applying selection sort algorithm
for i in range(n-1):
    index  = i
    for j in range(i+1,n):
        if a[i] >= a[j]:
            index = j
    if i != index :
        a[i],a[index] = a[index],a[i] # swap the values of a[i]  and a[index]


print("Array elements after sorting : ",end=' ')
for i in a:
    print(i,end =" ")
