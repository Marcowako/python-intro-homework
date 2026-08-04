# Sample students list (representing the data from week-4/data/roster.py)
students = [
    {"name": "Sara", "score": 91, "subject": "Python"},
    {"name": "Jazmine", "score": 85, "subject": "Data"},
    {"name": "Priya", "score": 78, "subject": "Web"},
    {"name": "Mia", "score": 82, "subject": "Python"},
    {"name": "Eli", "score": 77, "subject": "Data"},
    {"name": "Alex", "score": 64, "subject": "Web"},
]

# Variables to track data
top_scorer_name = ""
top_score = -1  # Start lower than any possible score
total_score = 0
unique_subjects = set()
high_scorers = []

# Loop through the list of student dictionaries once to perform all operations
for student in students:
    name = student["name"]
    score = student["score"]
    subject = student["subject"]

    # 1. Track the top scorer (without using max())
    if score > top_score:
        top_score = score
        top_scorer_name = name

    # 2. Accumulate the total score for average calculation
    total_score += score

    # 3. Collect unique subjects into a set
    unique_subjects.add(subject)

    # 4. List high scorers (score > 75)
    if score > 75:
        high_scorers.append(name)

# Calculate class average
class_average = round(total_score / len(students), 1)

# Display Results
print(f"Top scorer:       {top_scorer_name} ({top_score})")
print(f"Class average:    {class_average}")
print(f"Subjects offered: {unique_subjects}")
print(f"High scorers:     {high_scorers}")