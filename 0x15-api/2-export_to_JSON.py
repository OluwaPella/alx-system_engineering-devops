#!/usr/bin/python3
"""Exporting todo list information data in json format"""
import json
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    # Fetch user data
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    # Fetch todos for the user
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    # Specify the CSV file name based on user ID
    with open("{}.json".format(user_id), 'w') as jsonfile:
        for todo in todos:
            json.dump({user_id: [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")}]}, jsonfile)
