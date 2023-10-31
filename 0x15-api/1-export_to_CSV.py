#!/usr/bin/python3
"""Exporting todo list information data in CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    # Fetch user data
    user = requests.get(url + 'users/{}'.format(user_id)).json()
    # Fetch todos for the user
    todos = requests.get(url + 'todos', params={"userId": user_id}).json()
    # Specify the CSV file name based on user ID
    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # Write the CSV header row
             writer.writerow([
                user_id,
                user.get("username"),
                todo.get("completed"),
                todo.get("title")
                ]) for todo in todos:
