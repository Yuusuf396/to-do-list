
import datetime
from win11toast import toast

# toast('Hello Python🐍') 
datetime_time=datetime.datetime.now()
year=datetime_time.year
month=datetime_time.month
today=datetime_time.day
 

# toaster.show_toast("Example two",
# "This notification is in it's own thread!",
# icon_path=None,
# duration=5,
# threaded=True)



# # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
# day_of_week = current_datetime.weekday()

# # Map the integer to the corresponding day name
# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# day_name = days_of_week[day_of_week]

def sort_tasks(task_list):
    importance_mapping = {'high': 3, 'medium': 2, 'low': 1}
    sorted_tasks = sorted(task_list, key=lambda task: importance_mapping[task[1]], reverse=True)
    return sorted_tasks

# Use the function to sort the tasks

print(f"curr_year: {year},curr_mount:{month},date:{today}")
task_list=[]
name=input("Input Your Name: ")
# if not name.isalpha():
if len(name)<=1:
    print('Input correct parameters')
    name=input("Input Your Name: ")
loop_checker=True
task_number=1
list_tasks_importance=['high','medium','low']
while loop_checker:
    # task_details=[] 
    text=input(f'Input task {task_number}: ')   
    if len(text)<1:
        print("Invalid task. Please enter a valid task.")
        continue
 
    while loop_checker:
        task_importance = input("Enter task's importance (between :*'high','medium','low'*): ")
        if task_importance.lower() in list_tasks_importance:
            break
        print("Invalid importance. Please enter 'high', 'medium', or 'low'.")
    # task_importance=input("Enter task's importance (between :*'high','medium','low'*): ")
    # if  isinstance(task_details,str) and (task_importance.lower()=="high" or task_importance.lower()=="medium" or task_importance.lower()=="low"):     
    if  isinstance(task_importance,str) and (task_importance.lower() in list_tasks_importance):
        print(task_importance)
                
    while loop_checker:
        day = input("tasks can only made for this month, enter the day: ")
        # if today<= int(day) and day.isdigit():
        if  day.isdigit():
            break
        print("Invalid day. Please enter a valid day of this month.")
    while loop_checker:
        hour = input("Enter the hour (0-23): ")
        # if hour.isdigit() and 0 <= int(hour) <= 23:
        if hour.isdigit():
            break
        print("Invalid hour. Please enter a valid hour between 0 and 23.")

    date = datetime.datetime(year=year, month=month, day=int(day), hour=int(hour))
    task_list.append([f"{str(text)},deadline:{date}",task_importance])
    toast(f"Task {task_number}, deadline:{date}, Priority:{task_importance}",f"{text}",duration='short', button='Dismiss')
    
    # text_list.append(f"{str(text)},deadline:{date}")
    print(f"'{text}' was added succesfully")
    task_list = sort_tasks(task_list)
    
    print(f"{name}'s Tasks:")
    print(task_list)
    task_number+=1
    
    # File writing
    # f= open(f"{name}.txt", "a")
    # # f.write(f"task {task_number}: {text}.\n")}
    # f.write(f"{str(text)},deadline:{date},{task_importance} \n")
    # f.close()

        
    check=input("Do You want to continue? Y/N (Click 'y' or 'Y' to continue): ")
    if not check.upper()=="Y":
        loop_checker=False
        
            
f= open(f"{name}.txt", "a")
for  i in task_list:
     f.write(f"task {i[0]}: {i[1]}.\n")
       
       
       
# day = int(input("tasks can only made for this month, enter the day: "))
#         if today> day:
#             day = int(input("tasks can only made for this month, enter the day: "))
             
#         else:
            
        
   
   
   

    
             