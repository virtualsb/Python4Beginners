def pyramid_height(blocks):
    height = 0
    total_blocks_used = 0


    while True:
        blocks_needed_for_next_layer = (height + 1) * (height + 2) // 2

        if total_blocks_used + blocks_needed_for_next_layer <= blocks:
            height += 1
            total_blocks_used += blocks_needed_for_next_layer
        else:
            break

    return height

blocks = int(input("Enter the number of blocks available: "))

height = pyramid_height(blocks)

print(f"The height of the pyramid is: {height}")