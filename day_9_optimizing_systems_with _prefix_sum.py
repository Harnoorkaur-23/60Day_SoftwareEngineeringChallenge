# Input numbers
numbers = list(map(int, input("Enter numbers: ").split()))

# Build prefix sum array
prefix = []
total = 0
for num in numbers:
    total = total + num
    prefix.append(total)
print("\nOriginal array:", numbers)
print("Prefix sum array:", prefix)

# Take number of queries
q = int(input("\nEnter number of queries: "))
print("\nEnter queries using 0-based index.")
for i in range(0, q):
    left = int(input("Enter starting index: "))
    right = int(input("Enter ending index: "))

    # Prefix sum calculation
    if left == 0:
        range_sum = prefix[right]
    else:
        range_sum = prefix[right] - prefix[left - 1]

    print("Range sum:", range_sum)