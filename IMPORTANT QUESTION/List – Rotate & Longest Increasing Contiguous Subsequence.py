lst = [5, 1, 3, 4, 2]
k = 2

k = k % len(lst)
rotated = lst[-k:] + lst[:-k]
print("Rotated List:", rotated)

# Longest increasing contiguous subsequence
longest = curr = [rotated[0]]

for i in range(1, len(rotated)):
    if rotated[i] > rotated[i-1]:
        curr.append(rotated[i])
    else:
        curr = [rotated[i]]
    if len(curr) > len(longest):
        longest = curr

print("Longest Increasing Subsequence:", longest)
