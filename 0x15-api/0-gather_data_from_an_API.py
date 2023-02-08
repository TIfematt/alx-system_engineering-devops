#!/usr/bin/python3
""" A script that fetches an API using JSONPlaceholder"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    """ Setting user endpoint with Id from terminal """
    user = '{}users/{}'.format(url, sys.argv[1])

    """ Response from endpoint stored """
    res = requests.get(user)

    """ Response converted to JSON """
    json_o = res.json()

    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    """ Checking for employees done tasks """
    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
