#!/usr/bin/python3
# This use REST API   
# its display on the standard output the employee todo list progress
""" this module uses http request """
import requests
""" this module uses  system arg """
import sys

def get_employee_todo_progress(employee_id):
    # sending a GET request to the api endpoint 
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    if response.status_code == 200:
        todos = response.json()
    compelet_task = [todo for todo in todos if todo['completed']]
    NUMBER_OF_DONE_TASKS = len(compelet_task)
    TOTAL_NUMBER_OF_TASKS = len(todos)
    EMPLOYEE_NAME = todos[0]['username']
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

    for task in compelet_task:
        print(f"\t{task['title']}")

if  __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py employee_id")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID should be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
