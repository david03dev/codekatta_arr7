def difference_indices(arr):
    # Find the index of the smallest and largest numbers
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))
    
    # Calculate the difference of indices
    difference = max_index - min_index
    
    return difference

# Read input
n = int(input().strip())  # Read the number of elements (not actually used in code)
arr = list(map(int, input().strip().split()))  # Read the array of numbers

# Calculate and print the result
result = difference_indices(arr)
print(result)
