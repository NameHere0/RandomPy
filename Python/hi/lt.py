s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# Combine strings and ignore spaces
s = (s1 + s2).replace(" ", "")

# Step 1: count occurrences of each letter in the combined string
counts = [s.count(ch) for ch in s]

# Step 2: repeat symmetric reduction until only two numbers remain
while len(counts) > 2:
    new_counts = []
    n = len(counts)
    for i in range(n // 2):
        new_counts.append(counts[i] + counts[n - 1 - i])
    if n % 2 == 1:  # keep middle if odd
        new_counts.append(counts[n // 2])
    counts = new_counts

# Step 3: output the final two numbers as digits
print("".join(str(num) for num in counts))
