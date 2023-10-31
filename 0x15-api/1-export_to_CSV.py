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
    # Filter completed todos
    completed = [todo for todo in todos if todo.get("completed")]
    # Specify the CSV file name based on user ID
    csv_file = '{}.csv'.format(user_id)
    # Open CSV file for writing
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        # Write the CSV header row
        # Write data for each todo
        for todo in todos:
            writer.writerow([
                user_id,
                user['username'],  # Extract the 'username' attribute from user data
                "Completed" if todo["completed"] else "Not Completed",
                todo["title"]
            ])
