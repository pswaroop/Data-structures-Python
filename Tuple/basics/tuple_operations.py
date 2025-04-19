from tuple_demo import my_tuple, single_tuple

# Concatenate tuples: O(n+m)
final_tuple = my_tuple+single_tuple

# Length of tuple : O(1)
print(len(my_tuple))

# Count of specific element in tuple : O(n)
print(my_tuple.count("hello"))

# Retrieve index of an element
print(my_tuple.index(1))

# Tuples are immutable, which makes them memory-efficient and faster than lists in certain cases.
# Tuples can be directly compared and sorted lexicographically.
print((1, 2) < (1, 3))  # Output: True
sorted_tuples = sorted([(2, 1), (1, 3), (1, 2)])
print(sorted_tuples)  # Output: [(1, 2), (1, 3), (2, 1)]

# Since tuples are hashable, they can serve as keys in dictionaries, unlike lists.
my_dict = {(1, 2): "value"}
print(my_dict[(1, 2)])  # Output: value
