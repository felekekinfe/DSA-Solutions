n = int(input())
heights = list(map(int, input().split()))

max_height_index = heights.index(max(heights))
min_height_index = heights[::-1].index(min(heights))

min_swaps = max_height_index + min_height_index


if max_height_index + min_height_index >= n:
    min_swaps -= 1

print(min_swaps)
