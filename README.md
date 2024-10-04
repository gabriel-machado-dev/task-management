# Task Management System

This is a simple task management system written in Python. It allows users to add, list, update, and delete tasks for each day of the week. The tasks are stored in JSON files, one for each day of the week.

## Features

- **Add Task**: Add a new task to a specific day of the week.
- **List Tasks**: List all tasks for each day of the week.
- **Update Task**: Update the status of a task (Pending, Done).
- **Delete Task**: Delete a task from a specific day of the week.

## Requirements

- Python 3.x
- `rich` library for enhanced console output

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gabriel-machado-dev/task-management-system.git
    cd task-management-system
    ```

2. Install the required libraries:
    ```sh
    pip install rich
    ```

## Usage

Run the script:
```sh
python [app.py]
```

## Main menu

When you run the script, you will see the main menu with the following options:

1. Add task
2. List tasks
3. Update task
4. Delete task
5. Exit

### Adding a Task

1. Select the option `1. Add task`.
2. Select a day of the week to add the task.
3. Enter the task description.

### Listing Tasks

1. Select the option `2. List tasks`.
2. The tasks for each day of the week will be displayed in a table format.

### Updating a Task

1. Select the option `3. Update task`.
2. Select the day of the week.
3. Select the task to update.
4. Enter the new status of the task (Pending, Done).

### Deleting a Task

1. Select the option `4. Delete task`.
2. Select the day of the week.
3. Select the task to delete.

### Exiting the Program

1. Select the option 5. Exit.

### File Structure
- `app.py`: The main script containing all the functionality.
- `weekdays/`: Directory where JSON files for each day of the week are stored.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

### Author

- Gabriel Machado
- GitHub

### Acknowledgments

- The `rich` library for enhanced console output.

```bash
This README file provides an overview of the project, including its features, installation instructions, usage guide, file structure, license, and author information.
```