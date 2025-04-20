# Frozen Sets: 
# These are immutable sets and hashable, 
# so they can be used as keys in dictionaries or elements in other sets.

# Using frozenset as dictionary keys
frozen1 = frozenset([1, 2, 3])
frozen2 = frozenset([4, 5, 6])

# Creating a dictionary with frozenset keys
frozen_dict = {
    frozen1: "First Set",
    frozen2: "Second Set"
}

print("Dictionary with frozenset keys:")
for key, value in frozen_dict.items():
    print(f"{key} -> {value}")

# Using frozenset as elements in a set
frozen3 = frozenset([7, 8, 9])

# Creating a set of frozensets
frozen_set_collection = {frozen1, frozen2, frozen3}

print("\nSet containing frozensets:")
for item in frozen_set_collection:
    print(item)
