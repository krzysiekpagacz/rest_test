import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    #print(todo)
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

print(todos_by_user.items())
print(todos_by_user.keys())

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)
print(f'top_users: {top_users}')

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

s = "s" if len(users) > 1 else ""
print(f"user{s} {max_users} completed {max_complete} TODOs")

print(max_users)

# Define a function to filter out completed TODOs
# of users with max completed TODOS.
"""
The filter() function takes a function and a sequence as arguments and returns an iterable, only yielding the items in sequence for which function returns True.
If None is passed instead of a function, all the items of the sequence which evaluates to False are removed.
To produce the result at once we can use the list() function.
"""
def keep(todo):
    is_complete = todo["completed"]
    has_max_count = str(todo["userId"]) in users
    return is_complete and has_max_count

print(list(filter(keep, todos)))

# Write filtered TODOs to file.
with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)

