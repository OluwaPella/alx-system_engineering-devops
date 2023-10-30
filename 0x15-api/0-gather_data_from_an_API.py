#!/usr/bin/python3
# This use REST API   
# its display on the standard output the employee todo list progress
""" this module uses http request """
import requests

def get_employee_todo_progress(employee_id):
    # sending a GET request to the api endpoint 
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userid={employee_id}")
    if response.status_code == 200:
        todos = response.json()
    compelet_task = [todo for todo in todos if todo['completed']]
    NUMBER_OF_DONE = len(completede)
    TOTAL_NUMBER_OF_TASKS = len(todos)
    EMPLOYEE_NAME = todos[0]['username]
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE}/{TOTAL_NUMBER_OF_TASKS}):")

    for task in compelet_task:
        print(f"\t{task[' TASK_TITLE']}")
    else:
        print(f"Error:failed to retrieve TODO list for {employee_id}.")

    if  __name__ == "__main__":
        employee_id = 1  # Set the employee ID
        get_employee_todo_progress(employee_id)
