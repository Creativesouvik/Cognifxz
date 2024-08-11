def print_pyramid_pattern(levels):
    for i in range(1, levels + 1):
        # Print leading spaces
        for j in range(levels - i):
            print(" ", end="")

        # Print numbers
        for k in range(i):
            print(i, end=" ")

        # Move to the next line
        print()

# Step 4: Verify the Correctness of the Generated Pattern
levels = 5
print_pyramid_pattern(levels)