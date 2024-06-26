task = (str(input('Enter your task:')))
priority = (str(input('Priority (high/medium/low)')))
time = (str(input('Is it time-bound? (yes/no)')))

highyes = print(f'{task} is a high priority task that requires immediate attention today!')
highno = print(f'{task} is a high priority task with no time bound')
medyes = print(f'{task} is a medium priority task with time bound')
medno = print(f'{task} is a medium priority task with no time bound')
lowyes = print(f'{task} is a low priority task with time bound')
lowno = print(f'{task} is a low priority task. Consider completing it when you have free time.')

match priority:
    case 'high':
       if time == 'yes' :
       
         print(highyes)
       
       else : 
      
         print(highno)
       

    case 'medium':
        if time == 'yes' :
       
         print(medyes)
       
        else : 
      
         print(medno)
      

    case 'low':
        
        if time == 'yes' :
         print(lowyes)
       
       
        else  : 
         print(lowno)
      
     
    

