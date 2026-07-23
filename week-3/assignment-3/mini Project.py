# Mini Project: Activity Suggestion

day = input("Enter a day of the week: ").lower()
time = input("Enter the time of day (morning, afternoon, or evening): ").lower()
#check if time is valid
if time not in ["morning", "afternoon", "evening"]:
    print("Sorry, I don't recognize that time of day. Please enter morning, afternoon, or evening.")
# Check the day
elif day == "monday":
    if time == "morning":
        print("Start your week by planning your goals.")
    elif time == "afternoon":
        print("Work on a school or work project.")
    else:
        print("Relax with a good book.")
elif day == "tuesday":
    if time == "morning":
        print("Go for a morning walk.")
    elif time == "afternoon":
        print("Practice a hobby or learn something new.")
    else:
        print("Watch your favorite TV show.")
elif day == "wednesday":
    if time == "morning":
        print("Exercise to stay healthy.")
    elif time == "afternoon":
        print("Meet up with a friend or study together.")
    else:
        print("Prepare for the rest of the week."
else:
    print("Sorry, I don't recognize that day of the week.")
