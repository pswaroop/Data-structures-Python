from tuple_demo import my_tuple, nested_tuple

# Accessing tuple elements
# print(my_tuple[0])
# print(my_tuple[-1])

# Iterating over tuple
for elm in my_tuple:
    print(elm)

# Tuple slicing
print(my_tuple[0:2])

# Unpacking
a, b, c = my_tuple[0:3]
print(a,b,c)

# nested tuple: (1, (2, 3), 4)
print(nested_tuple[1][1])

# membership check in tuple : O(n)
print("hello" in my_tuple)