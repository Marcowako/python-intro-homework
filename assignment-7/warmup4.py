from datetime import datetime

# Get current date and time
now = datetime.now()

# Format date as "Month DD, YYYY" (e.g., "April 24, 2026")
formatted_date = now.strftime("%B %d, %Y")

# Print output
print(f"Today is {formatted_date}.")