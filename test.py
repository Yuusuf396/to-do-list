
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
while loop_checker:
    task_number+=1
    text=input(f'Input task {task_number}: ')   
    if len(text)>=1:
        print(f"{name}'s Tasks:")
        
        
        
        day = int(input("tasks can only made for this month, enter the day: "))
        hour = int(input("Enter the hour: "))
        date = datetime.datetime(year=year, month=month, day=day, hour=hour)
        text_list.append(f"{str(text)},deadline:{date}")
        print(text_list)
        
        # File writing
        # f= open(f"{name}.txt", "a")
        # f.write(f"task {task_number}: {text}.\n")
        # f.close()

        print(f"'{text}' was added succesfully")
        check=input("Do You want to continue? Y/N (Click 'y' or 'Y' to continue): ")
        if not  check.upper()=="Y":
            loop_checker=False
        
            

    
   

    
             