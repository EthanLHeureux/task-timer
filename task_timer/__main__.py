import click
import time
import csv
 

@click.command()
def main():
    """This is my main cli."""

    click.echo("How may I Help:\n")

    idea = str(input())
    if idea == 'create':
        create()
    if idea == 'start':
        start()
    elif idea == 'stop':
        stop()
    elif idea == 'time_of':
        time_of()
    elif idea == 'delete':
        delete()
    elif idea == 'list_tasks':
        list_tasks()
    elif idea == 'export_timeSheet':
        export_timeSheet()
    else:
        click.echo("Sorry command does not exist,\n use cmd '--help' for list of commands")



@click.command()
def create():
    """
    Creates a new task in the CSV file if it doesn't already exist. 
    Prompts the user for a task name and adds it with an initial time of '00'.
    """


    click.echo("\nName of  Task?\n")
    taskName = input()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows:

            if row[0] == taskName:
                click.echo("Already exists.")
                break

            else:
                with open('task_list.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([taskName, "00"])
                click.echo("Task Created.")



@click.command()
def start():
    """
    Starts tracking time for a task by updating its time field. 
    If the task is found and not already started, it sets the current timestamp.
    """

    click.echo("\nName of  Task?\n")
    taskName = input()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in rows:
            if (row[0] == taskName) and (row[1] == '00'):  
                row[1] = str(time.time())
                break  
        else:
            click.echo("\nTask Does Not Exist or time is already started.")

    with open('task_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)



@click.command()
def stop():
    """
    Stops the timer for a task and calculates the total time spent. 
    Displays the total time and updates the task's record in the file.
    """

    click.echo("\nName of  Task?\n")
    taskName = input()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows:
        
            if (row[0] == taskName):  
                total_time = float(time.time()) - float(row[1])
                row[1] = total_time
                click.echo("\nTotal time of task was: " + str(total_time))
                break
        
        else:
            click.echo("Task Does Not Exist.")



@click.command()
def delete():
    """
    Deletes a task from the CSV file based on its name. 
    Removes the task and updates the file accordingly.
    """

    rows_to_keep = []  
    click.echo("\nName of  Task?\n")
    taskName = input()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows: 
        
            if row[0] != taskName: 
                rows_to_keep.append(row)        

    with open('task_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows_to_keep)
    
    click.echo("Task Stopped.")



@click.command()
def time_of():
    """
    Displays the time spent on a task so far. 
    Calculates the time by subtracting the initial time from the current time.
    """

    click.echo("\nName of  Task?\n")
    taskName = input()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows:

            if (row[0] == taskName):  
                total_time = float(time.time()) - float(row[1])
                click.echo("\nTime of task so far is: " + str(total_time))
                break
        
        else:
            click.echo("Task Does Not Exist.")



@click.command()
def list_tasks():
    """
    Lists all tasks and the time spent on each task. 
    Displays the task name and the time difference between the current time and the stored start time.
    """

    now = time.time()

    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

        for row in rows:
            click.echo("\nTask: " + row[0] + "\tTime spent on Task: " + str(now - float(row[1]) ) )




@click.command()
def export_timeSheet():
    with open('task_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
     

    with open('export.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)



if __name__ == '__main__':
    main()