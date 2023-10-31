#!/usr/bin/python3
"""  exporting todo list information  data in  CSV format"""
import requests
import csv
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = requests.get(url + 'user{}'.format(user_id)).json()
    todos = requests.get(url + 'todos', params={"userId": user_id}).json()
    completed = (todo for todo in todos if todo.get("completed") is True)
    csv_file = '{}.csv'.format(user_id)
    with open(csv_file, 'w' newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            (writer.writerow[
                [user_id,
                user, todo.get("completed"),
                todo.get("title")
                ]) for todo in todos]
