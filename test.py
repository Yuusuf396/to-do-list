
import datetime

datetime_time=datetime.datetime.now()
year=datetime_time.year
month=datetime_time.month


# # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
# day_of_week = current_datetime.weekday()

# # Map the integer to the corresponding day name
# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# day_name = days_of_week[day_of_week]



print(year,month)
text_list=[]
name=input("Input Your Name: ")
# if not name.isalpha():
if len(name)<=1:
    print('Input correct parameters')
    name=input("Input Your Name: ")
loop_checker=True
task_number=0
list_tasks_importance=['high','medium','low']
while loop_checker:
    task_details=[]
    task_number+=1
    text=input(f'Input task {task_number}: ')   
    if len(text)>=1:
        
        
        
        task_importance=input("Enter task's importance (between :*'high','medium','low'*): ")
        day = int(input("tasks can only made for this month, enter the day: "))
        hour = int(input("Enter the hour: "))
        date = datetime.datetime(year=year, month=month, day=day, hour=hour)
        task_details.append(f"{str(text)},deadline:{date}")
        text_list.append(f"{str(text)},deadline:{date}")
        print(f"'{text}' was added succesfully")
        print(f"{name}'s Tasks:")
        print(text_list)
        
        # File writing
        # f= open(f"{name}.txt", "a")
        # f.write(f"task {task_number}: {text}.\n")
        # f.close()

        
        check=input("Do You want to continue? Y/N (Click 'y' or 'Y' to continue): ")
        if not  check.upper()=="Y":
            loop_checker=False
        
            

    
   

    
             