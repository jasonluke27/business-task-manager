 Here's a summary of the programs functionality:

1. User Authentication:

The program reads usernames and passwords from a file named "user.txt" and stores them in two separate lists (usernames and passwords).
Users are prompted to enter their username and password, and the program checks if the entered credentials match those in the lists.
If the credentials are correct, the user is welcomed; otherwise, they are prompted to try again.

2. User Registration:

An admin user with the username "admin" has the ability to register new users by providing a username and password.
The program ensures password confirmation and checks for duplicate usernames before adding a new user to the "user.txt" file.

3. Task Management:

Users can add tasks, providing details such as the username of the assigned user, task title, description, due date, and current date.
Tasks are appended to a file named "tasks.txt."

4. Task Viewing:

Users (both admin and non-admin) can view all tasks or only tasks assigned to them.

5.Task Overview:

The program calculates and displays task overview statistics, including total tasks, completed tasks, incomplete tasks, overdue tasks, incomplete task percentage, and overdue task percentage.
The results are written to a file named "task_overview.txt."

6. User Overview:

The program calculates and displays user-specific task statistics for each user (assigned tasks, completion percentages, etc.).
The results are written to a file named "user_overview.txt."

7. Menu System:

The program provides a menu-based interface for users (admin and non-admin) to perform various actions such as registering users, adding tasks, viewing tasks, and more.
The menu is displayed in a loop until the user chooses to exit.
