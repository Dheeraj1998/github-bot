import json
import urllib.request as ur

service_url = 'https://api.github.com/users/'
user_name = input('Enter the name of the user: ')
service_url = service_url + user_name + '/repos'

json_data = json.loads(ur.urlopen(service_url).read())

print("\nThe list of the repos & number of unassigned issues under the user are: ")

for data in json_data:	
	issue_url = 'https://api.github.com/repos/' + user_name + '/' + data["name"] + '/issues?state=all'
	issue_data = json.loads(ur.urlopen(issue_url).read())
	
	if(issue_data == []):
		print(data["name"]," : No issues!")
	
	else:
		for issue in issue_data:
			if (issue["assignee"] == None):
				print(data["name"]," : Unassigned issues. Hurry now to get assigned!")

