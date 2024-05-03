
import datetime
from win10toast import ToastNotifier
import time
datetime_time=datetime.datetime.now()
year=datetime_time.year
month=datetime_time.month

toaster = ToastNotifier()

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

print(year,month)
task_list=[]
name=input("Input Your Name: ")
# if not name.isalpha():
if len(name)<=1:
    print('Input correct parameters')
    name=input("Input Your Name: ")
loop_checker=True
task_number=0
list_tasks_importance=['high','medium','low']
while loop_checker:
    # task_details=[] 
    task_number+=1
    text=input(f'Input task {task_number}: ')   
    if len(text)>=1:
 
        
        task_importance=input("Enter task's importance (between :*'high','medium','low'*): ")
        # if  isinstance(task_details,str) and (task_importance.lower()=="high" or task_importance.lower()=="medium" or task_importance.lower()=="low"):     
        if  isinstance(task_importance,str) and (task_importance.lower() in list_tasks_importance):
            print(task_importance)
                 
        
        day = int(input("tasks can only made for this month, enter the day: "))
        hour = int(input("Enter the hour: "))
        date = datetime.datetime(year=year, month=month, day=day, hour=hour)
        task_list.append([f"{str(text)},deadline:{date}",task_importance])
        toaster.show_toast(f"Task {task_number}",f"{text}",icon_path=None,duration=5,threaded=True)
        
        # text_list.append(f"{str(text)},deadline:{date}")
        print(f"'{text}' was added succesfully")
        task_list = sort_tasks(task_list)
        while toaster.notification_active(): time.sleep(0.1)
        print(f"{name}'s Tasks:")
        print(task_list)
        
        # File writing
        # f= open(f"{name}.txt", "a")
        # f.write(f"task {task_number}: {text}.\n")
        # f.close()

        
        check=input("Do You want to continue? Y/N (Click 'y' or 'Y' to continue): ")
        if not  check.upper()=="Y":
            loop_checker=False
        
            

    
   

    
             