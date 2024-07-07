def count_divisibles(l, r, k):
    if l % k == 0:
        first_divisible = l
    else:
        first_divisible = l + (k - l % k)
    
    if r % k == 0:
        last_divisible = r
    else:
        last_divisible = r - (r % k)
    
    if first_divisible > r or last_divisible < l:
        count = 0
    else:
        count = (last_divisible - first_divisible) // k + 1
    
    return count

l, r, k = map(int, input().split())

print(count_divisibles(l, r, k))
