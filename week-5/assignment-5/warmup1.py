# Initialize a running total
total_sum = 0

# Loop through numbers from 1 to 100 (range stop value is non-inclusive, so 101 goes up to 100)
for num in range(1, 101):
    total_sum += num

# Print the final result
print("The sum of 1 to 100 is", total_sum)