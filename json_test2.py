import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/comments')
comments = json.loads(response.text)

#which post have the max number of comments
comm_per_post = {}

for comment in comments:
	try:
		comm_per_post[comment['postId']] += 1
	except KeyError:
		comm_per_post[comment['postId']] = 1

sorted_comm_per_post = sorted(comm_per_post.items(), key=lambda x : x[1], reverse=True)
print(sorted_comm_per_post)

#user who comment most frequentlz
comm_users = {}
for comment in comments:
	try:
		comm_users[comment['email']] += 1
	except KeyError:
		comm_users[comment['email']] = 1

sorted_comm_users = sorted(comm_users.items(), key=lambda x: x[1], reverse=True)

print(sorted_comm_users)