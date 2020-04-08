"""
API description:
    We can get a summary list of tasks that need to be done.
    We can get much more detailed information about a specific task.
    We can add a new task to our to-do list.
    We can mark a task as done.
    We can modify an existing task (changing its description, and so on).
"""

import requests

def _url(path):
    return 'https://todo.example.com' + path

def get_tasks():
    return requests.get(_url('/tasks/'))

def describe_task(task_id):
    return requests.get(_url('/tasks/{:d}/'.format(task_id)))

def add_task(summary, description=""):
    return requests.post(_url('/tasks/'), json={
        'summary': summary,
        'description': description,
        })

def task_done(task_id):
    return requests.delete(_url('/tasks/{:d}/'.format(task_id)))

def update_task(task_id, summary, description):
    url = _url('/tasks/{:d}/'.format(task_id))
    return requests.put(url, json={
        'summary': summary,
        'description': description,
        })
