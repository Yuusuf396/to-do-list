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
        text_list.append(str(text))
        print(text_list)
        f= open(f"{name}.txt", "a")
        f.write(f"task {task_number}: {text}.\n")
        
        f.close()

        print(f"'{text}' was added succesfully")
        check=input("Do You want to continue? Y/N (Click 'y' or 'Y' to continue): ")
        if not  check.upper()=="Y":
            loop_checker=False
        
            

    
   

    
             