# Create two hardcoded lists with some overlapping and unique items
list1 = ["Python", "JavaScript", "C++", "HTML", "SQL"]
list2 = ["Java", "Python", "JavaScript", "Go", "Rust"]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)

# 1. Union: All languages from both sets, with no duplicates
union_set = set1.union(set2)  # Alternatively: set1 | set2
print("Union:", union_set)

# 2. Intersection: Languages that appear in both sets
intersection_set = set1.intersection(set2)  # Alternatively: set1 & set2
print("Intersection:", intersection_set)

# 3. Difference: Languages only in the first set (not in the second)
difference_set = set1.difference(set2)  # Alternatively: set1 - set2
print("Difference (set1 - set2):", difference_set)