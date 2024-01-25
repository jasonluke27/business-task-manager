#=====importing libraries===========
usernames = [] # usernames list to be appended.
passwords = [] # passwords list to be appended.
user_file = open("user.txt", "r") # open user.txt file for reading.
for lines in user_file : # This section will strip and split the lines in the user.txt file and append each list accordingly.
    temp = lines.strip()
    temp = temp.split(", ")
    usernames.append(temp[0])
    passwords.append(temp[1])
login = False # login is set as false to be changed in our while loop.

#====Login Section====
# This while loop will check that the user enters the correct username and password that is stored in the user.txt file.
while login == False :
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    # if the username and password is in the usernames and passwords list then the login becomes True.
    if username in usernames and password in passwords :
        login = True
        print(f"Welcome {username}!")
    # if the username and password is not in the usernames and passwords list then the login remains False.
    else :
        print("You have entered the wrong username or password, please try again.")
    user_file.close()


def reg_user():
        #if username is not admin then the user cannot add a new user.
        if username != "admin" :
            print("You are not the admin so you cannot add a new user")
        # if the username is admin then the program must present the admin with the option to add a new username and password.
        elif username == "admin" :
            pass
            new_username = input("Please enter the username you would like to create: ")
            new_password = input("Please enter your password: ")
            # Initially the user check password must be set to false to be verified in the while loop.
            user_check_password = False
            
            # While the user_check_password is False, the user must be prompted to confirm their new password.
            while user_check_password == False :
                user_confirmed_password = input("Please confirm your password: ")
                # If the user_confirmed_password matches the new password then the user_check_password becomes true.
                if user_confirmed_password == new_password :
                    user_check_password = True
                # Otherwise the user_confirmed_password does not match and the corresponding message must be printed.
                elif user_confirmed_password != new_password :
                    print("Passwords do not match, please try again")
            
            # if the new username and new password is in each of the usernames or passwords list then the program must say the user already exists and prompt for a new username and password.
            if new_username in usernames and new_password in passwords :
                print("This user already exists, please try a different username!")
                new_username = input("Please enter the username you would like to create: ")
                new_password = input("Please enter your password: ")
                user_check_password = False
            
            # While the user_check_password is False, the user must be prompted to confirm their new password.
                while user_check_password == False :
                    user_confirmed_password = input("Please confirm your password: ")
                    # If the user_confirmed_password matches the new password then the user_check_password becomes true.
                    if user_confirmed_password == new_password :
                        user_check_password = True
                    # Otherwise the user_confirmed_password does not match and the corresponding message must be printed.
                    elif user_confirmed_password != new_password :
                        print("Passwords do not match, please try again")
                # otherwise the program must write the new user login details to the user.txt file.
                else:
                    user_file = open("user.txt", "a")
                    user_file.write(f"\n{new_username}, {new_password}")
                    print("The new user has been added!")
                    user_file.close()

                    
            # otherwise the program must write the new user login details to the user.txt file.
            else:
                user_file = open("user.txt", "a")
                user_file.write(f"\n{new_username}, {new_password}")
                print("The new user has been added!")
                user_file.close()

def add_task():
    pass
        # import date from datetime function.
    tasks = open("tasks.txt", "a") # open tasks.txt file for appending too.
    user_task = input("Enter the username of the user who's task you would like to add too: ")
    task_title = input("Enter the title of the task you are adding: ")
    task_description = input("Enter a description for the task you are adding: ")
    task_due_date = input("What is the due date of the task you are adding?: ")
    current_date = input("Enter todays date for the given task date(eg.10 Oct 2020): ")
    task_completion = "No"
    # After the user has input all the information, the program must write all the new information to the tasks.txt file.
    tasks.write(f"\n{user_task}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_completion}")
    print("The new task has been added!")
    tasks.close()

def view_all():
    pass
    tasks = open("tasks.txt", "r") # open tasks.txt file for reading.
    # Split all the information in the task.txt file by the commas and white spaces.
        
        # The display must show the user all the current task information in an easy to read format.
    for lines in tasks:
        user_task , task_title , task_description , current_date, task_due_date , task_completion = lines.split(", ")
    print(f"Username : {user_task}" f"\nTask Title : {task_title}" f"\nTask Description: {task_description}"
                  f"\nDue Date : {task_due_date}" f"\nTask Completion : {task_completion}")
    tasks.close()

def view_mine():
    pass
    tasks = open("tasks.txt", "r")  # Open tasks.txt file for reading.
    task_list = tasks.readlines()  # Read all lines from the file into a list.
    tasks.close()

    print("Tasks:")

    for index, line in enumerate(task_list):
        user_task, task_title, task_description, current_date, task_due_date, task_completion = line.strip().split(", ")
        # If the username matches the username for their task, print only the task for that username.
        if username == user_task:
            print(f"Task #{index + 1}:")
            print(f"Username: {user_task}")
            print(f"Task Title: {task_title}")
            print(f"Task Description: {task_description}")
            print(f"Due Date: {task_due_date}")
            print(f"Task Completion: {task_completion}")
            print()
      # requuest the users input for the task number or -1 to return to menu.      
    task_number = input("Enter the task number you want to select (-1 to return to the main menu): ")

    if task_number == "-1":
        # Return to the main menu
        pass
    else:
        task_index = int(task_number) - 1
        # output statement to show user if they input a  wrong number.
        if task_index < 0 or task_index >= len(task_list):
            print("Invalid task number.")
        else:
            user_task, task_title, task_description, current_date, task_due_date, task_completion = task_list[task_index].strip().split(", ")
            # ask the user what changes they would like to make to the chosen task.
            action = input("Select an action: \n1. Mark task as complete \n2. Edit task\n")
            # if the user selects 1 the program must change the no to a yes in the tasks.txt file.
            if action == "1":
                if task_completion.lower() != "yes":
                    task_completion = "Yes"
                    task_list[task_index] = f"{user_task}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_completion}\n"
                    with open("tasks.txt", "w") as tasks:
                        tasks.writelines(task_list)
                    print("Task marked as complete.")
                else:
                    print("Task is already marked as complete.")
            # if the user selects 2 then the program must first identify if the task is completed and if not the user must be asked to input the changes they want to make.
            elif action == "2":
                if task_completion.lower() == "yes":
                    print("Task cannot be edited as it is already marked as complete.")
                else:
                    new_user_task = input("Enter the new username (leave empty to keep the current username): ")
                    new_due_date = input("Enter the new due date (leave empty to keep the current due date): ")
                    # show output if no changes are made to the task.
                    if new_user_task == "" and new_due_date == "":
                        print("No changes made.")
                    # otherwise the program must make the changes below and write the changes to the tasks.txt file.
                    else:
                        if new_user_task != "":
                            user_task = new_user_task
                        if new_due_date != "":
                            task_due_date = new_due_date

                        task_list[task_index] = f"{user_task}, {task_title}, {task_description}, {current_date}, {task_due_date}, {task_completion}\n"
                        with open("tasks.txt", "w") as tasks:
                            tasks.writelines(task_list)
                        print("Task updated.")
            # otherwise output the user has made an invalid selection.        
            else:
                print("Invalid action.")

def task_overview_function():
    # the function must first count the lines in the tasks.txt file and for every line the the loop counts, the line count must increment by 1.
    line_count = 0
    with open("tasks.txt", "r") as file:
        for line in file:
                line_count += 1

    total_tasks = line_count
    completed_tasks = 0 
    incomplete_tasks = 0
    overdue_tasks = 0
    # open the tasks.txt file for reading and then split all the lines by the the commas.
    with open("tasks.txt", "r") as tasks:
        for lines in tasks:
            user_task, task_title, task_description, current_date, task_due_date, task_completion = lines.strip().split(", ")
            # if the the loop identifies that the task is completed then completed tasks must add 1.
            if task_completion == "No":
                incomplete_tasks += 1
            # if the loop identifies that the task is incomplete then the incomplete tasks must add 1. 
            else:
                completed_tasks += 1
            # if our task completion is equal to no and the task due date is passed then the overdue tasks must add 1.
            if task_completion == "No" and task_due_date < current_date:
                overdue_tasks += 1
    incomplete_tasks_percentage = round((incomplete_tasks / total_tasks) * 100) # calculation to calculate the incomplete tasks percentage.
    overdue_tasks_percentage = round((overdue_tasks / total_tasks) * 100) # calculation to calculate the overdue tasks percentage.
    # the program must then write the relevant information to the "task_overview.txt" file.
    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(f"{total_tasks}, {completed_tasks}, {incomplete_tasks}, {overdue_tasks}, {incomplete_tasks_percentage}%, {overdue_tasks_percentage}%")
    # the program must then display the information in the "task_overview.txt" file for the user to see.
    with open("task_overview.txt", "r") as task_overview:
        for line in task_overview:
            total_tasks, completed_tasks, incomplete_tasks, overdue_tasks, incomplete_tasks_percentage, overdue_tasks_percentage = line.split(", ")
        print(f"Total Tasks: {total_tasks}\nCompleted Tasks: {completed_tasks}\nIncomplete Tasks: {incomplete_tasks}\nOverdue Tasks: {overdue_tasks}\nIncomplete Tasks Percentage: {incomplete_tasks_percentage}\nOverdue Tasks Percentage: {overdue_tasks_percentage}")
    print()
def user_overview_function():
    # Open the user file for reading
    user_file = open("user.txt", "r")
    users = user_file.readlines()  # Read the lines of the file

    # Open the tasks file for reading
    tasks_file = open("tasks.txt", "r")
    tasks = tasks_file.readlines()  # Read the lines of the file

    user_tasks = {}

    # Loop through each user
    for user in users:
        # Split the line into username and password
        username, password = user.strip().split(", ")

        assigned_tasks = 0
        completed_assigned_tasks = 0
        uncompleted_assigned_tasks = 0
        overdue_assigned_tasks = 0

        # Loop through each task
        for task in tasks:
            task_data = task.strip().split(", ")

            if len(task_data) == 6:
                # Split the task data into individual variables
                user_task, task_title, task_description, current_date, task_due_date, task_completion = task_data

                # Check if the task belongs to the current user
                if user_task == username:
                    assigned_tasks += 1
                    if task_completion == "No":
                        uncompleted_assigned_tasks += 1
                    else:
                        completed_assigned_tasks += 1

                    if task_completion == "No" and task_due_date < current_date:
                        overdue_assigned_tasks += 1

        # Calculate task statistics for the user
        assigned_tasks_percentage = round((assigned_tasks / len(tasks)) * 100 if len(tasks) > 0 else 0)
        completed_percentage = round((completed_assigned_tasks / assigned_tasks) * 100 if assigned_tasks > 0 else 0)
        uncomplete_percentage = round((uncompleted_assigned_tasks / assigned_tasks) * 100 if assigned_tasks > 0 else 0)
        overdue_percentage = round((overdue_assigned_tasks / assigned_tasks) * 100 if assigned_tasks > 0 else 0)

        # Store the user overview data in a dictionary
        user_tasks[username] = {
            "assigned_tasks": assigned_tasks,
            "assigned_tasks_percentage": assigned_tasks_percentage,
            "completed_percentage": completed_percentage,
            "uncomplete_percentage": uncomplete_percentage,
            "overdue_percentage": overdue_percentage
        }

    # Write the user overview data to a file
    with open("user_overview.txt", "w") as user_overview:
        for username, task_data in user_tasks.items():
            # Write the user overview data as a comma-separated line in the file
            user_overview.write(f"{username}, {task_data['assigned_tasks']}, {task_data['assigned_tasks_percentage']}, {task_data['completed_percentage']}, {task_data['uncomplete_percentage']}, {task_data['overdue_percentage']}\n")

    # Read and print the user overview data
    with open("user_overview.txt", "r") as user_overview:
        for line in user_overview:
            # Split the line into individual variables
            username, assigned_tasks, assigned_tasks_percentage, completed_percentage, uncomplete_percentage, overdue_percentage = line.strip().split(", ")
            # Print the user overview information
            print(f"Username: {username}\nAssigned Percentage: {assigned_tasks_percentage}\nCompleted Percentage: {completed_percentage}\nUncomplete Percentage: {uncomplete_percentage}\nOverdue Percentage: {overdue_percentage}\n")

    # Inform the user that the user overview data has been written to a file
    print("User overview data has been written to 'user_overview.txt'")
    print()
    # Close the opened files
    user_file.close()
    tasks_file.close()

#====Menu Section====    
while True:
    # presenting the admin menu to the admin user. and 
    # making sure that the user input is converted to lower case.
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate report
ds - display statistics
e - Exit
: ''').lower()
    # presenting a different menu if the user is not the admin user.
    #making sure that the user input is converted to lower case.
    elif username != "admin":
         menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    
    # if the user selects menu option r, the program must first identify if the user is the admin user. 
    if menu == 'r':
        reg_user()
       
    # if the user selects option a, they must be asked to enter all the information to assign the new task.    
    elif menu == 'a':
        add_task()
       

    # if the user selects option va, they must be shown all the tasks that are in the tasks.txt file.
    elif menu == 'va':
        view_all()

    # If the user selects option vm, they must only be shown the tasks for their username.
    elif menu == 'vm':
       view_mine()

    
    # If the admin selects option ds, the program must display the total number of tasks and users for the admin.   
    elif menu == 'ds' :
        user_file = open("user.txt" , "r")
        pass

        total_tasks = 0 # to be incremented in for loop.
        total_users = 0 # to be incremented in for loop.

        tasks = open("tasks.txt", "r") # open task.txt file for reading.
        # This for loop takes each line into account and increments it by every line that is in the file to get the total number of tasks.
        for line in tasks :
            total_tasks += 1
        print(f"The total number of tasks are {total_tasks}")
            
        # This for loop takes each line from the user.txt file and increments it by every line that is in the file.
        for line in user_file :
            total_users += 1
        print(f"The total number of users are {total_users}")
        task_overview_function()
        user_overview_function()
        user_file.close()
        tasks.close()
        
    elif menu == 'gr':
        task_overview_function()
        user_overview_function()
      
        
        
    # if the user selects option e, the program must print Goodbye and exit the menu.
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")