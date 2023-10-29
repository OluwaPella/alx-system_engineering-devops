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
    num_compelet_task = len(compelet_task)
    total_task = len(todos)
    employee_name = todos[0].get['username']
    print(f"Employee {employee_name} is done with tasks({num_compelet_task}/{total_task}):")

    for task in compelet_task:
        print(f"\t{task['title']}")
    else:
        print(f"Error:failed to retrieve TODO list for {employee_id}.")

    if  __name__ == "__main__":
        employee_id = 1  # Set the employee ID
        get_employee_todo_progress(employee_id)
