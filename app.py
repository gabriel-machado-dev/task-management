import os 
import datetime
import json
from time import sleep
from rich.console import Console
from rich.table import Table

# Colors
DEFAULT = '\033[0m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
YELLOW = '\033[3m\033[1;33m'
YELLOW2 = '\033[1;93m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
BOLD = '\033[1m'
BLINK = '\033[5m'

weekdays = [datetime.date(2023, 1, i).strftime("%A") for i in range(2, 9)]

def print_title():
    print('''

         {1}╔══════════════════════════════════════════════════════════╗{0}
         {1}║░▀█▀░█▀█░█▀▀░█░█░░░█▄█░█▀█░█▀█░█▀█░█▀▀░█▀▀░█▄█░█▀▀░█▀█░▀█▀║{0}
         {1}║░░█░░█▀█░▀▀█░█▀▄░░░█░█░█▀█░█░█░█▀█░█░█░█▀▀░█░█░█▀▀░█░█░░█░║{0}
         {1}║░░▀░░▀░▀░▀▀▀░▀░▀░░░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░░▀░║{0}
         {1}╚══════════════════════════════════════════════════════════╝{0}
       
         {2})    /\__/\ 
         {2}( = (˶ᵔ ᵕ ᵔ˶)
         {1}-------{2}U{1}-{2}U{1}----------------
         {1}|                        |       |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|
         {1}|  {3}Code Author: {2}Gabriel Machado  {0}{1}|       {3}GitHub: {2}https://github.com/gabriel-machado-dev{0}
         {1}|      {3}Version: {2}1.5      {0}{1}|             
         {1}|                        |       |_____________________________________________|
         {1}--------------------------                        {2}\ (˶ᵔ ᵕ ᵔ˶) /{0}
                                                            {2}\         /{0}

        '''.format(DEFAULT, GREEN, RED,YELLOW2
                   ,YELLOW, BLINK, MAGENTA, CYAN))
    
def select_day():
    print_title()

    print(f'{BLUE}Select a day of the week to add the task. 📅{DEFAULT}')
    print('')
    for i, day in enumerate(weekdays, 1):
        print(f'{CYAN}{i}. {day}{DEFAULT}')
    print('')
   
    day = input('Enter the number of the day: ')
    if day.isdigit() and 0 < int(day) <= len(weekdays):
        print(f'{GREEN}You selected {weekdays[int(day) - 1]}{DEFAULT}')
        print('')
    else:
        print(f'{RED}Invalid day!{DEFAULT}')
        print('')
        return select_day()
    

    return day
        
def add_task():
    day = select_day()
    if day:
        os.makedirs('weekdays', exist_ok=True)
        filename = f'weekdays/{weekdays[int(day) - 1]}.json'
        if os.path.exists(filename):
            while True:
                task = input('Enter the task: ')
                if not task or task.isspace() or task.isdigit():
                    print(f'{RED}Invalid task!{DEFAULT}')
                    print(f'{RED}Please enter a valid task{DEFAULT}')
                    print('')
                    continue
                break

        
            data = {'Task': task, 'Status': 'Pending'}
            with open(filename, 'r+', encoding='utf-8') as f:
                tasks = json.load(f)
                tasks.append(data)
                f.seek(0)
                json.dump(tasks, f, indent=4, ensure_ascii=False)
            print(f'{GREEN}Task added successfully!{DEFAULT}')
        
        else:
            while True:
                task = input('Enter the task: ')
                if not task or task.isspace() or task.isdigit():
                    print(f'{RED}Invalid task!{DEFAULT}')
                    print(f'{RED}Please enter a valid task{DEFAULT}')
                    print('')
                    continue
                break

            data = [{'Task': task, 'Status': 'Pending'}]
            with open(filename , 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f'{GREEN}Task added successfully!{DEFAULT}')
        print('')

def list_tasks():
    print(f'{BLUE}List of tasks for each day of the week. 📅{DEFAULT}')
    print('')
    for i, day in enumerate(weekdays, 1):
        filename = f'weekdays/{day}.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
                print(f'{CYAN}{i}. {day}{DEFAULT}')
                table = Table(title=f'{day}', show_lines=True)
                table.add_column('ID', justify='center', style='cyan', no_wrap=True)
                table.add_column('Task', justify='center', style='cyan', no_wrap=True)
                table.add_column('Status', justify='center', style='magenta', no_wrap=True)
                for i, task in enumerate(tasks):
                    table.add_row(f'{i + 1}', f'{task["Task"]}', task['Status'])
                console = Console()
                console.print(table)
                print('')
        else:
            print(f'{CYAN}{i}. {day}{DEFAULT}')
            print(f'{RED}No tasks added!{DEFAULT}')
            print('')

def update_task():
    list_tasks()
    print(f'{BLUE}Update the status of a task. 📅{DEFAULT}')
    print('')
    day = input('Enter the number of the day: ')
    if day.isdigit() and 0 < int(day) <= len(weekdays):
        print(f'{GREEN}You selected {weekdays[int(day) - 1]}{DEFAULT}')
        print('')
    else:
        print(f'{RED}Invalid day!{DEFAULT}')
        print('')
        return

    filename = f'weekdays/{weekdays[int(day) - 1]}.json'
    if os.path.exists(filename):
        with open(filename, 'r+', encoding='utf-8') as f:
            tasks = json.load(f)
            table = Table(title=f'{weekdays[int(day) - 1]}')
            table.add_column('ID', justify='center', style='cyan', no_wrap=True)
            table.add_column('Task', justify='center', style='cyan', no_wrap=True)
            table.add_column('Status', justify='center', style='magenta', no_wrap=True)
            for i, task in enumerate(tasks):
                table.add_row(f'{i + 1}', f'{task["Task"]}', task['Status'])
            console = Console()
            console.print(table)
            print('')

            task = input('Enter the number of the task: ')
            if task.isdigit() and 0 < int(task) <= len(tasks):
                print(f'{GREEN}You selected the task {tasks[int(task) - 1]["Task"]}{DEFAULT}')
                print('')
            else:
                print(f'{RED}Invalid task!{DEFAULT}')
                print('')
                return

            status = input('Enter the status of the task (Pending, Done): ')
            if status.lower() in ['pending', 'done']:
                tasks[int(task) - 1]['Status'] = status.capitalize()
                f.seek(0)
                json.dump(tasks, f, indent=4)
                f.truncate()
                print(f'{GREEN}Task updated successfully!{DEFAULT}')
            else:
                print(f'{RED}Invalid status!{DEFAULT}')
                print('')
    else:
        print(f'{RED}No tasks added!{DEFAULT}')
        print('')

def delete_task():
    list_tasks()
    print(f'{BLUE}Delete a task. 📅{DEFAULT}')
    print('')
    day = input('Enter the number of the day: ')
    if day.isdigit() and 0 < int(day) <= len(weekdays):
        print(f'{GREEN}You selected {weekdays[int(day) - 1]}{DEFAULT}')
        print('')
    else:
        print(f'{RED}Invalid day!{DEFAULT}')
        print('')
        return

    filename = f'weekdays/{weekdays[int(day) - 1]}.json'
    if os.path.exists(filename):
        with open(filename, 'r+', encoding='utf-8') as f:
            tasks = json.load(f)
            table = Table(title=f'{weekdays[int(day) - 1]}')
            table.add_column('ID', justify='center', style='cyan', no_wrap=True)
            table.add_column('Task', justify='center', style='cyan', no_wrap=True)
            table.add_column('Status', justify='center', style='magenta', no_wrap=True)
            for i, task in enumerate(tasks):
                table.add_row(f'{i + 1}', f'{task["Task"]}', task['Status'])
            console = Console()
            console.print(table)
            print('')

            task = input('Enter the number of the task: ')
            if task.isdigit() and 0 < int(task) <= len(tasks):
                print(f'{GREEN}You selected the task {tasks[int(task) - 1]["Task"]}{DEFAULT}')
                print('')
            else:
                print(f'{RED}Invalid task!{DEFAULT}')
                print('')
                return

            tasks.pop(int(task) - 1)
            f.seek(0)
            json.dump(tasks, f, indent=4)
            f.truncate()
            print(f'{GREEN}Task deleted successfully!{DEFAULT}')
    else:
        print(f'{RED}No tasks added!{DEFAULT}')
        print('')

def main(): 
    print_title()  
    while True:
        print(f'{BLUE}Select an option:{DEFAULT}')
        print(f'{CYAN}1. Add task{DEFAULT}')
        print(f'{CYAN}2. List tasks{DEFAULT}')
        print(f'{CYAN}3. Update task{DEFAULT}')
        print(f'{CYAN}4. Delete task{DEFAULT}')
        print(f'{CYAN}5. Exit{DEFAULT}')
        print('')
        option = input('Enter the number of the option: ')
        print('')
        if option == '1':
            os.system('clear') if os.name == 'posix' else os.system('cls')
            add_task()
        elif option == '2':
            os.system('clear') if os.name == 'posix' else os.system('cls')
            list_tasks()
        elif option == '3':
            os.system('clear') if os.name == 'posix' else os.system('cls')
            update_task()
            os.system('clear') if os.name == 'posix' else os.system('cls')
            list_tasks()
        elif option == '4':
            os.system('clear') if os.name == 'posix' else os.system('cls')
            delete_task()
        elif option == '5':
            print(f'{YELLOW}Goodbye!{DEFAULT}')
            sleep(3)
            break
        else:
            print(f'{RED}Invalid option!{DEFAULT}')
            print(f'{YELLOW}Please enter a number between 1 and 5{DEFAULT}')
            print('')
            continue

if __name__ == '__main__':
    main()