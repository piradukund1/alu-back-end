#!/usr/bin/python3
"""Return TODO list progress for a given employee ID."""
import requests
import sys
if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = int(sys.argv[1])
    user = requests.get(
        "{}/users/{}".format(base_url, employee_id)
    ).json()
    todos = requests.get(
        "{}/todos".format(base_url),
        params={"userId": employee_id}
    ).json()
    completed_tasks = [
        task["title"] for task in todos if task["completed"]
    ]
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user["name"], len(completed_tasks), len(todos)
        )
    )
    for task in completed_tasks:
        print("\t {}".format(task))
