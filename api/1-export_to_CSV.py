#!/usr/bin/python3
"""Export all tasks of a given employee ID to a CSV file."""
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": user_id}).json()
    username = user.get("username")

    with open("{}.csv".format(user_id), "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username,
                             task.get("completed"), task.get("title")])
