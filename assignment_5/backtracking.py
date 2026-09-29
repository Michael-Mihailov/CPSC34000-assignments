def backtrack(L: list, target:int):
    def backtrack_sum(L: list, target: int, depth: int):
        if target < 0 or (depth >= len(L) and target > 0):
            return None
        if target == 0:
            return []
        
        temp = backtrack_sum(L, target - L[depth], depth + 1)
        if temp == None:
            return backtrack_sum(L, target, depth + 1) # backtrack
        temp.insert(0, depth)
        return temp

    return backtrack_sum(L, target, 0)



# ----- HERE ARE SOME TEST CASES -----

# non-edge case
print(backtrack([3, 4, 7, 8], 11))            # Answer: [0, 3]

# No solution
print(backtrack([2, 4, 6], 5))                # Answer: None
print(backtrack([1, 3, 5], 2))                # Answer: None

# Target is zero
print(backtrack([1, 2, 3], 0))                # Answer: []

# Empty list
print(backtrack([], 0))                       # Answer: []
print(backtrack([], 5))                       # Answer: None

# Single-element lists
print(backtrack([7], 7))                      # Answer: [0]
print(backtrack([7], 5))                      # Answer: None

# Solution uses the last element
print(backtrack([2, 4, 6], 10))               # Answer: [1, 2]

# Solution uses all elements
print(backtrack([1, 2, 3], 6))                # Answer: [0, 1, 2]

# Duplicate values
print(backtrack([3, 3, 6], 6))                # Answer: [0, 1]
print(backtrack([2, 2, 2], 4))                # Answer: [0, 1]

# Target larger than sum
print(backtrack([1, 2, 3], 100))              # Answer: None