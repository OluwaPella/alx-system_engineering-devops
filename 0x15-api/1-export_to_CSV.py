#!/usr/bin/python3
"""  exporting todo list information  data in  CSV format"""
import request
import csv
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user = requests.get(url + 'user{}'.format(user_id)).json()
    todos = requests.get(url + 'todos', params={"userId": user_id}).json()
    compeleted = (todo for todo in todos if todo.get("compeleted") is True)
    csv_file = '{}.csv'.format(user_id)
    with open(csv_file, 'w' newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([
                user_Id,
                user['username'],
                "compeleted" if todo["compeleted"] else "not completed",
                todo["title"]
                ])
