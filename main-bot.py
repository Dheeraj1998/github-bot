import json
import urllib.request as ur

service_url = 'https://api.github.com/users/'
user_name = input('Enter the name of the user: ')
service_url = service_url + user_name + '/repos'

json_data = json.loads(ur.urlopen(service_url).read())

print("\nThe list of the repos & number of unassigned issues under the user are: ")

for x in json_data:
	total_issue = 0
	print(x["name"]," : ")
	
	issue_url = 'https://api.github.com/repos/' + user_name + '/' + x["name"] + '/issues?state=all'
	issue_data = json.loads(ur.urlopen(issue_url).read())
	
	for x in issue_data:
		print(x)

