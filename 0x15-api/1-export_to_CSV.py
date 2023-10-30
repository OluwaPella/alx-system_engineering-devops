#!/usr/bin/python3
# this script print todo list in ssv format
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
        fieldnames = ["id", "title", "completed"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
 for todo in completed:
            writer.writerow({"id": todo["id"], "title": todo["title"], "completed": todo["completed"]})
