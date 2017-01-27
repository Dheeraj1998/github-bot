import json
import urllib.request as ur

service_url = 'https://api.github.com/users/'
user_name = input('Enter the name of the user: ')
service_url = service_url + user_name + '/repos'

json_data = json.loads(ur.urlopen(service_url).read())

print("\n")
print("The list of the repos under the user are: ")

for x in json_data:
	print(x["name"])
