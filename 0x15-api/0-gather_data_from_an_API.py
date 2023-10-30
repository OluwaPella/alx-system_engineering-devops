#!/usr/bin/python3
# This use REST API
# its display on the standard output the employee todo list progress
"""this module uses http request"""
import requests
import sys
if  __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + 'users/{}'.format(sys.argv[1])).json()
    todos = requests.get(url + 'todos',  params={"userId": sys.argv[1]}).json()
    completed = [todo for todo in todos if todo.get("completed") is True]
    print('Employee {} is done with tasks({}/{}):'.format
            (user.get("name"), len(completed), len(todos)))
    [print('\t {}'.format(c.get("title"))) for c in completed]
