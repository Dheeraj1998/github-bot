import json
import urllib.request as ur
import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

github_url = 'https://api.github.com/users/'
user_name = input('Enter the name of the user: ')

#Remove '?access_token' in case of un-registred API usage
github_url = github_url + user_name + '/repos?access_token=<Enter your personal Github API>'
twitter_post = []

json_data = json.loads(ur.urlopen(github_url).read())

print("\nThe list of the repos & number of unassigned issues under the user are: ")

for data in json_data:	
	issue_url = 'https://api.github.com/repos/' + user_name + '/' + data["name"] + '/issues?access_token=<Enter your personal Github API>'
	issue_data = json.loads(ur.urlopen(issue_url).read())
	total_issue = 0

	if(issue_data == []):
		print(data["name"]," : No open issues!")
	
	else:
		for issue in issue_data:
			if (issue["assignee"] == None):
				#The twitter character limit means only essential info about the issue can be given.
				twitter_post.append([data["name"],issue["number"]])
				total_issue = total_issue + 1
				
		print(data["name"]," : Open issues are present." + str(total_issue) + " issues are unassigned.")

if twitter_post != '':
	cfg = { 
		"consumer_key"        : "<Enter your consumer key>",
		"consumer_secret"     : "<Enter your consumer key (secret)>",
		"access_token"        : "<Enter your acccess token>",
		"access_token_secret" : "<Enter your acccess token (secret)>" 
		}
		
	api = get_api(cfg)
	tweet = "Check these out:"
	count = 1

	for x in twitter_post:
		tweet = tweet + "\n" + str(count) + '.' + x[0] + ":#" + str(x[1])
		count = count + 1
		
	status = api.update_status(status=tweet)
	print("Issues has been tweeted! :)") 

else:
	print("\nNo un-assigned issues found!")
