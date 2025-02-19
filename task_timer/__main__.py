"""
__main__.py
Author: Ethan L'Heureux
Date: 04 02 2025

Description:
This program is a command-line task timer that allows users to create, 
start, stop, delete, list and search time spent on tasks. It stores task data in 
a CSV file which can be exportd.

Usage:
- Run the script using 'uv run task-timer' and enter commands as prompted.
- Type '--help' for list of commands
- Type 'exit' to quit the program.
"""

import click
import csv
from datetime import datetime


def main():
    """Main loop."""

    click.echo("\nHow may I help? Type '--help' for a list of commands and 'exit' to leave application:")

    while True:
        click.echo("")
        idea = input().lower()
        if idea == "exit":
            click.echo("\nGoodbye!")
            break
        tasker(idea)


def tasker(idea):
    """ List of functions to execute. """

    if idea == 'create':
        create()
    elif idea == 'start':
        start()
    elif idea == 'stop':
        stop()
    elif idea == 'time_of':
        time_of()
    elif idea == 'delete':
        delete()
    elif idea == 'list_tasks':
        list_tasks()
    elif idea == 'export_csv':
        export_csv()
    elif idea == '--help':
        get_help()
    else:
        click.echo("Sorry command does not exist,\nuse cmd '--help' for list of commands")
    return False


def get_help():
    """Displays a help menu with available commands."""

    help_msg = """
    Available Commands:
    -------------------
    create      - Create a new task.
    start       - Start tracking time for a task.
    stop        - Stop a task and show time spent.
    time_of     - Show time spent on a specific task.
    delete      - Delete a task.
    list_tasks  - List all tasks and their time spent.
    export_csv  - Export tasks to a CSV file.
    exit        - Quit the application.
    """
    click.echo(help_msg)


def create():
    """
    Creates a new task in the CSV file if it doesn't already exist. 
    Prompts the user for a task name and adds it with an initial time of '00'.
    """

    task_exists = False

    click.echo("\nName of Task?")
    taskName = input()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:

            if row[0] == taskName:
                click.echo("\nAlready exists.")
                task_exists = True
                break
        if not task_exists:
            with open('task_list.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([taskName, "00"])
            click.echo("\nTask Created " + str(datetime.now()) + ".")


def start():
    """
    Starts tracking time for a task by updating its time field. 
    If the task is found and not already started, it sets the current timestamp.
    """

    click.echo("\nName of  Task?")
    taskName = input()

    updated_rows = []

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
            if (row[0] == taskName) and (row[1] == '00'):  
                row[1] = datetime.now().isoformat()
                updated_rows.append(row)
                click.echo("\nTask Started " + str(datetime.now()) + ".")
                break
            updated_rows.append(row)
        else:
            click.echo("\nTask Does Not Exist or time is already started.")

    with open('task_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(updated_rows)


def stop():
    """
    Stops the timer for a task and calculates the total time spent. 
    Displays the total time and updates the task's record in the file.
    """

    click.echo("\nName of  Task?")
    taskName = input()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
        
            if (row[0] == taskName):  
                start_time = datetime.fromisoformat(row[1])  # Convert stored time back to datetime
                total_time = datetime.now() - start_time  # Calculate total time spent
                row[1] = str(total_time.total_seconds())
                click.echo("\nTotal time of task was: " + str(total_time.total_seconds()) + " on " + str(datetime.now()))
                break
        
        else:
            click.echo("\nTask Does Not Exist.")


def delete():
    """
    Deletes a task from the CSV file based on its name. 
    Removes the task and updates the file accordingly.
    """

    rows_to_keep = []  
    click.echo("\nName of  Task?")
    taskName = input()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader: 
        
            if row[0] != taskName: 
                rows_to_keep.append(row)        

    with open('task_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows_to_keep)
    
    click.echo("\nTask Deleted " + str(datetime.now()) + ".")


def time_of():
    """
    Displays the time spent on a task so far. 
    Calculates the time by subtracting the initial time from the current time.
    """

    click.echo("\nName of  Task?")
    taskName = input()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:

            if (row[0] == taskName):  
                start_time = datetime.fromisoformat(row[1])  # Convert stored time back to datetime
                total_time = datetime.now() - start_time
                click.echo("\nTime of task so far is: " + str(total_time.total_seconds()))
                break
        
        else:
            click.echo("\nTask Does Not Exist.")


def list_tasks():
    """
    Lists all tasks and the time spent on each task. 
    Displays the task name and the time difference between the current time and the stored start time.
    """

    now = datetime.now()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
            if row[1] == "00":
                click.echo("\nTask: " + row[0] + "\tTime spent on Task: 00" + "\t\tStarted:  " + row[1])
            else:
                start_time = datetime.fromisoformat(row[1]) 
                total_time = now - start_time
                click.echo("\nTask: " + row[0] + "\tTime spent on Task: " + str(total_time.total_seconds()) + "\t\tStarted:  " + row[1])


def export_csv():
    """
    Exports the task data from 'task_list.csv' to 'export.csv'.
    """

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open('export.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("\nExported file at:\t /export.csv")


if __name__ == '__main__':
    main()

