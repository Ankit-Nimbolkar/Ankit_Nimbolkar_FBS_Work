# Fuzzy Sets
fuzzy_set_A = {'a': 0.8, 'b': 0.6, 'c': 0.2}
fuzzy_set_B = {'a': 0.9, 'b': 0.3, 'd': 0.7}

print("Fuzzy Set A:", fuzzy_set_A)
print("Fuzzy Set B:", fuzzy_set_B)

# Union Operation
def fuzzy_union(A, B):
    result = {}
    for x in set(A.keys()).union(B.keys()):
        result[x] = max(A.get(x, 0), B.get(x, 0))
    return result

# Intersection Operation
def fuzzy_intersection(A, B):
    result = {}
    for x in set(A.keys()).union(B.keys()):
        result[x] = min(A.get(x, 0), B.get(x, 0))
    return result

# Complement Operation
def fuzzy_complement(A):
    result = {}
    for x, value in A.items():
        result[x] = round(1 - value, 2)
    return result

# Results
print("Union of A and B:", fuzzy_union(fuzzy_set_A, fuzzy_set_B))
print("Intersection of A and B:", fuzzy_intersection(fuzzy_set_A, fuzzy_set_B))
print("Complement of A:", fuzzy_complement(fuzzy_set_A))
print("Complement of B:", fuzzy_complement(fuzzy_set_B))
