from set_demo import my_set, second_set

# Adding element to set - O(1)
my_set.add("hello")
print(my_set)

# Removing element from set - O(1) - Raises KeyError if element not found
my_set.remove("hello")
# my_set.remove(10) # Raises KeyError here as 10 is not existing in my_set
print(my_set)

# Removing/Discarding element from set - O(1) - will not raise KeyError if elm not found
my_set.discard("hello")
my_set.discard(10)
my_set.discard(4)
print(my_set)

# Remove arbitrary(random) element from set
my_set.pop()
print(my_set)

# clear the set
new_set = my_set.clear()
print(new_set)

#  Union of two sets
new_set_union = my_set.union(second_set)
# (or) new_set_union = my_set | second_set
print(new_set_union)

# Intersection of two sets
print(my_set.intersection(new_set_union))
print(my_set & second_set)

# Difference between two sets
print(new_set_union-my_set)
print(my_set.difference(second_set))

# Symmetric difference between two sets
print(new_set_union^my_set)
print(my_set.symmetric_difference(second_set))

# Set comprehension
squares = {x ** 2 for x in range(1, 6)}
print(squares)



"""
Use Set Operations to Simplify Logic:

Use intersection() or & for common elements.

Use difference() or - to find elements in one set but not the other.

Use symmetric_difference() or ^ for non-overlapping elements between sets.

Avoid Using Sets for Ordered Data: 
If you need sorted data, consider using a list combined with sorted() 
or use a specialized data structure (like heapq for heaps).

Precompute with Sets: 
In problems where precomputation is allowed, 
populate a set with all "valid" or "precalculated" results 
to quickly verify conditions during runtime.

"""