import os

# Add Task Funtion()
def add_task(dct):
    n = int(input("How many tasks do you want to enter: "))
    for i in range(0,n):
        a = input(f"Task {len(dct) + 1}: ")
        dct[len(dct) + 1] = a
        print(f"Task {len(dct)} is Added.")

    # Adding Tasks in todo.txt file
    if(not"todo.txt"):
        with open("todo.txt", "a") as f:
            for key,value in dct.items():
                f.write(f"Task {key}: {value}\n")
    else:
        with open("todo.txt", "a") as f:
            for key,value in dct.items():
                f.write(f"Task {key}: {value}\n")
    return dct


# View Task Funtion()
def view_task(dct, done_dict):
    if(len(dct) == 0):
        print("No Tasks Available...")
    else:
        print("Pending Tasks: ")
        for key,value in sorted(dct.items()):
            print("Task ",key, ": ", value)

    if(len(done_dict) == 0):
        print("No Tasks is Done...")
    else:
        print("Done Tasks: ")
        for key,value in sorted(done_dict.items()):
            print("Task ",key, ": ", value)
    return 


# Mark Task Funtion()
def mark_task(dct, done_dict):
    if(len(dct) == 0):
        print("No Task Available...")
    else:
        n = int(input("How many tasks you want to mark as done? "))
        if(len(dct) < n):
            print(f"Error! {n} tasks are not present in Todo File. Total Task Present: {len(dct)}")
        else:  
            for i in range(0,n):
                dn_tsk = int(input("Enter the task number which is done: "))
                if dn_tsk in dct:
                    done_dict[dn_tsk] = dct[dn_tsk]
                    print(f"Task {dn_tsk} is Done...")
                    dct.pop(dn_tsk)
                else:
                    print(f"Task {dn_tsk} is not present")
    return dct, done_dict


# Delete Task Funtion()
def delete_task(dct):
    if(len(dct) == 0):
        print("No Task Available...")
    else:
        n = int(input("How many tasks you want to delete? "))
        if(len(dct) < n):
            print(f"Error! {n} tasks are not present in Todo File. Total Task Present: {len(dct)}")
        else:    
            for i in range(0,n):
                d = int(input("Enter the Task Number you want to delete: "))
                if d in dct:
                    dct.pop(d)
                    print(f"Task {d} is deleted successfully")
                else:
                    print(f"Task {d} is not present")
    return dct


# To_Do Block
def To_Do():
    done_dict = {}
    task_dict = {}
    cont = 'y'
    while(cont == 'y' or cont == 'Y'):
        # Add, View, Mark and Delete Task menu is shown
        print("*****Command Line To-Do Application*****")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task")
        print("4. Delete Task")
        try: 
            # In try Block, Choice is taken.
            choice = int(input("Enter you choice(1, 2, 3, 4): "))
            if(choice == 1):
                try:
                    add_task(task_dict)
                except Exception as e:
                    print(e)
            elif(choice == 2):
                try:
                    view_task(task_dict, done_dict)
                except Exception as e:
                    print(e)
            elif(choice == 3):
                try:
                    mark_task(task_dict, done_dict)
                except Exception as e:
                    print(e)
            elif(choice == 4):
                try:
                    delete_task(task_dict)
                except Exception as e:
                    print(e)
        except:
            print("Please Enter an Integer between 1 to 4")
        
        # Quit or Continue this Application
        cont = input("Do you want to continue? (Y/N) : ")
        if(cont == 'n' or cont == 'N'):
            x = input("Do you want to save the To-Do file: (Y/N)")
            if(x.lower() == 'y'):
                print("File is saved...")
            elif(x.lower() == 'n'):
                try:
                    os.remove("D:/IDRAK AI Software House/todo.txt")
                except OSError as error:
                    print(error, " File is not present...")
            print("Quiting the Application...")
            exit(0)
        elif(cont == 'y' or cont == 'Y'):
            None
        elif(cont!='n' or cont!='N' or cont!="y" or cont!="Y"):
            while(cont!='n' or cont!='N' or cont!="y" or cont!="Y"):
                cont = input("Invalid Input! Please Enter (Y/N): ")
                if(cont == 'n' or cont == 'N'):
                    x = input("Do you want to save the To-Do file: (Y/N)")
                    if(x.lower() == 'y'):
                        print("File is saved...")
                    elif(x.lower() == 'n'):
                        try:
                            os.remove("D:/IDRAK AI Software House/todo.txt")
                        except OSError as error:
                            print(error, " File is not present...")
                    print("Quiting the Application...")
                    exit(0)
                elif(cont == 'y' or cont == 'Y'):
                    break



# Main Block
if __name__ == "__main__":
    To_Do()