task = input('Enter your task:')
priority = input('Priority (high/medium/low):')
time_bound = input('Is it time-bound? (yes/no):')

#highyes = print(f'{task} is a high priority task that requires immediate attention today!')
#highno = print(f'{task} is a high priority task with no time bound')
#medyes = print(f'{task} is a medium priority task with time bound')
#medno = print(f'{task} is a medium priority task with no time bound')
#lowyes = print(f'{task} is a low priority task with time bound')
#lowno = print(f'{task} is a low priority task. Consider completing it when you have free time.')

 
match priority:
    case "high":
        reminder = f"Task: {task} (Priority: High)"
    case "medium":
        reminder = f"Task: {task} (Priority: Medium)"
    case "low":
        reminder = f"Task: {task} (Priority: Low)"
    case _:
        reminder = "Invalid priority. Please enter high, medium, or low."
     
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(f'Reminder:{reminder}')    

