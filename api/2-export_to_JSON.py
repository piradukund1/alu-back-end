#!/usr/bin/python3
"""Export all tasks of a given employee ID to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": user_id}).json()
    username = user.get("username")

    data = {user_id: [{"task": task.get("title"),
                       "completed": task.get("completed"),
                       "username": username} for task in todos]}

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(data, json_file)