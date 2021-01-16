n, m, k = tuple(map(int, input().split()))

itmes = tuple(map(int, input().split()))

current_box_remaining_vol = k
items_count = 0
for item in itmes[::-1]:
    if item > current_box_remaining_vol:
        current_box_remaining_vol = k - item
        m -= 1
    
    if m == 0:
        break

    items_count += 1
    current_box_remaining_vol -= item

print(items_count)