#!/usr/bin/python3
"""Exporting todo list information data in json format"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    # Fetch user data
    user = requests.get(url + 'users/{}').json()
    # Fetch todos for the user
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    # Specify the CSV file name based on user ID
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump({: [{todo.get("user")
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")} for todo in todos]}, jsonfile)
