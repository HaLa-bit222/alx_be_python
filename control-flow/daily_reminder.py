task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unrecognized priority level"
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    print(f"Reminder: {reminder}")
else:
    if priority == "high":
        reminder += ". Take action immediately!"
        print(f"Reminder: {reminder}")
    elif priority == "medium":
        reminder += ". Schedule time for this task."
        print(f"Note: {reminder}")
    elif priority == "low":
        reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
        print(f"Note: {reminder}")
    else:
        print(f"Note: {reminder}")