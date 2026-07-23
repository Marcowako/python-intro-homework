# Mini Project: Activity Suggestion

day = input("Enter a day of the week: ").lower()
time = input("Enter the time of day (morning, afternoon, or evening): ").lower()

if day == "monday":
    if time == "morning":
        print("Start your week by planning your goals.")
    elif time == "afternoon":
        print("Work on a school or work project.")
    elif time == "evening":
        print("Relax with a good book.")
    else:
        print("Sorry, I don't recognize that time of day.")

elif day == "tuesday":
    if time == "morning":
        print("Go for a morning walk.")
    elif time == "afternoon":
        print("Practice a hobby or learn something new.")
    elif time == "evening":
        print("Watch your favorite TV show.")
    else:
        print("Sorry, I don't recognize that time of day.")

elif day == "wednesday":
    if time == "morning":
        print("Exercise to stay healthy.")
    elif time == "afternoon":
        print("Meet up with a friend or study together.")
    elif time == "evening":
        print("Prepare for the rest of the week.")
    else:
        print("Sorry, I don't recognize that time of day.")

else:
    print("Sorry, I don't recognize that day of the week.")