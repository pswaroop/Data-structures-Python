from list_demo import li,second_list

# li = [1,2,3,4]
# Adding elements - append() - Time complexity: O(1)
li.append("hello")
li.append(5)

# Inserting element in the list at index - insert(index,value) - Time complexity: O(n)
li.insert(0,1)
li.insert(1,"Hi")
li.insert(2,2.67)

# Removing element from the list - remove(value) - Time complexity: O(n)
li.remove(1)
li.remove("hello")

# Popping last element from the list - pop() - Time complexity: O(1)
li.pop()

# Popping ith element from the list - pop(index) - Time complexity: O(n)
li.pop(1)
li.pop(0)

# Sorting the list - sort() - Time complexity: O(nlogn)
li.sort(reverse=True) #Reverse=True for descending order

# Reversing the list - reverse() - Time complexity: O(n)
li.reverse()

# Retrieve length of list - O(1)
size_of_list = len(li)

# Concatenation of two lists - Time complexity: O(n+m)
new_list = li+second_list

# List slicing - Time complexity: O(k) where k is the slice length
sliced_list = new_list[0:3]

# List iteration - Time complexity: O(n)
for elm in sliced_list:
    pass
    # print(elm)

# List extend - extend() - Time complexity: O(k) where k is number of elements being added
new_list.extend(li)

# Other operations - Sum, min, max - Only work on numerical lists - Time complexity: O(n)
print(sum(sliced_list))
print(min(sliced_list))
print(max(sliced_list))

# Deleting list using del keyword - Time complexity: O(1)
del li

# sort list with custom criteria
sliced_list.sort(key=lambda x: x % 2)  # Sort by remainder when divided by 2

# print(sliced_list)
# print(size_of_list)
# print(li)
