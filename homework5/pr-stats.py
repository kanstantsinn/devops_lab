#!/root/.pyenv/shims/python
import requests
import json
import getpass
import re
import datefinder
import datetime
import calendar
import argparse

arg_input = argparse.ArgumentParser(prog='pr-stats', description='Get statistics from GitHub')
arg_input.add_argument('-v', '--version', help='Print the version of programm', action='version', version='version 1.0')
arg_input.add_argument('-r', '--rate', help='Basic statistics about merged/closed rate', action='store_true')
arg_input.add_argument('-d', '--days_opened', help='Number of days opened', action='store_true')
arg_input.add_argument('-w', '--d_w_opened', help='Day of week opened', action='store_true')
arg_input.add_argument('-c', '--d_w_closed', help='Day of week closed', action='store_true')
arg_input.add_argument('-o', '--w_opened', help='Weeks opened', action='store_true')
arg_input.add_argument('-k', '--w_closed', help='Weeks closed', action='store_true')
arg_input.add_argument('-a', '--after_date', help='pull requests opend on or after this date', action='store_true')
arg_input.add_argument('-b', '--before_date', help='pull requests opend before this date', action='store_true')
arg_input.add_argument('-u', '--user', type=str, required=True, default='kanstantsinn', help='username on git')
arg_input.add_argument('-R', '--repo', type=str, required=True, default='devops_lab', help='repo')

option = arg_input.parse_args()
user = option.user
repo = option.repo

username = input ("Input GIT login:\n")
password = input ("Input password:\n")

pulls = []
for l in range (1, 50):
    p = requests.get("https://api.github.com/repos/alenaPy/{}/pulls?page={}&state=all".format(repo, l), auth=(username, password))
    pulls += p.json()
    if l == 1:
        all_requests = json.dumps(p.json()[0]["number"], indent=1, sort_keys=True) # get all_requests
    l +=  1
    if int(json.dumps(p.json()[-1]["number"], indent=1, sort_keys=True)) == 1:
        break
'''
file = open("/home/student/PycharmProjects/untitled/venv/t5_json", "w")
file.write(json.dumps(pulls, indent=1, sort_keys=True))
file.close()
'''
# Basic statisctics about merget/closed rate**************
if option.rate:
	merged = 0
	open_pulls = 0
	for i in range(len(pulls)):
	    if json.dumps(pulls[i]["merged_at"], indent=1, sort_keys=True) != "null":
	        merged += 1
	    state = json.dumps(pulls[i]["state"], indent=1, sort_keys=True)
	    if state == '"open"':
	        open_pulls += 1
	print("merged :{}".format(merged))
	print ("Open :{}".format(open_pulls))
	print ("all_requests :{}".format(all_requests))
# Opend request before this date*****************************************
elif option.before_date:
	while True:
	    temp_date = input ("input date in format YYYY-MM-DD\n")
	    if re.match("^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$", temp_date):
	        break
	user_git = input ("Input GIT username:\n")
	for i in range(len(pulls)):
	    temp = (json.dumps(pulls[i]["head"]["repo"]["owner"]["login"], indent=1, sort_keys=True))[1:-1]
	    if temp == user_git:
	        temp_state = json.dumps(pulls[i]["state"], indent=1, sort_keys=True)[1:-1]
	        if temp_state == 'open':
	            created_time = (json.dumps(pulls[i]["created_at"], indent=1, sort_keys=True))[1:11]
	            created_time2 = created_time.replace('-', '')
	            temp_date2 = temp_date.replace('-', '')
	            if created_time2 < temp_date2:
	                title = json.dumps(pulls[i]["title"], indent=1, sort_keys=True)
	                print ("title: {:25} create at: {}".format(title, created_time))
# Opend request after this date*****************************************
elif option.after_date:
	while True:
	    temp_date = input ("input date in format YYYY-MM-DD\n")
	    if re.match("^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$", temp_date):
	        break
	user_git = input ("Input GIT username:\n")
	for i in range(len(pulls)):
	    temp = (json.dumps(pulls[i]["head"]["repo"]["owner"]["login"], indent=1, sort_keys=True))[1:-1]
	    if temp == user_git:
	        temp_state = json.dumps(pulls[i]["state"], indent=1, sort_keys=True)[1:-1]
	        if temp_state == 'open':
	            created_time = (json.dumps(pulls[i]["created_at"], indent=1, sort_keys=True))[1:11]
	            created_time2 = created_time.replace('-', '')
	
	            temp_date2 = temp_date.replace('-', '')
		
	            if created_time2 >= temp_date2:
	                title = json.dumps(pulls[i]["title"], indent=1, sort_keys=True)
	                print ("title: {:25} create at: {}".format(title, created_time))

# days opend*****************************************
elif option.days_opened:
	user_git = input ("Input GIT username:\n")
	for i in range(len(pulls)):
	    temp = (json.dumps(pulls[i]["head"]["repo"]["owner"]["login"], indent=1, sort_keys=True))[1:-1]
	    if temp == user_git:
	        temp_state = json.dumps(pulls[i]["state"], indent=1, sort_keys=True)[1:-1]
	        if temp_state == 'open':
	            created_time = (json.dumps(pulls[i]["created_at"], indent=1, sort_keys=True))[1:11]
	            matches = datefinder.find_dates(created_time)
	            match_list = []
	            for match in matches:
	                match_list.append(match)
	            diff = datetime.datetime.today() - match_list[0]
	            title = json.dumps(pulls[i]["title"], indent=1, sort_keys=True)
	            print("title: {:25} opened :{} days ago".format(title, diff.days))

# Day of week opened ***************************************8
elif option.d_w_opened:
	user_git = input ("Input GIT username:\n")
	for i in range(len(pulls)):
	    temp = (json.dumps(pulls[i]["head"]["repo"]["owner"]["login"], indent=1, sort_keys=True))[1:-1]
	    if temp == user_git:
	        temp_state = json.dumps(pulls[i]["state"], indent=1, sort_keys=True)[1:-1]
	        if temp_state == 'open':
	            created_time = (json.dumps(pulls[i]["created_at"], indent=1, sort_keys=True))[1:11]
	            matches = datefinder.find_dates(created_time)
	            match_list = []
	            for match in matches:
	                match_list.append(match)
	            created_date  = (match_list[0]).date()
	            day_week_name = calendar.day_name[match_list[0].date().weekday()]
	            title = json.dumps(pulls[i]["title"], indent=1, sort_keys=True)
	            print("title: {:25} opened on:{}".format(title, day_week_name))

# Day of week closed ***************************************8
elif option.d_w_closed:
	user_git = input ("Input GIT username:\n")
	for i in range(len(pulls)):
	    temp = (json.dumps(pulls[i]["head"]["repo"]["owner"]["login"], indent=1, sort_keys=True))[1:-1]
	    if temp == user_git:
	        temp_state = json.dumps(pulls[i]["state"], indent=1, sort_keys=True)[1:-1]
	        if temp_state == 'closed':
	            created_time = (json.dumps(pulls[i]["created_at"], indent=1, sort_keys=True))[1:11]
	            matches = datefinder.find_dates(created_time)
	            match_list = []
	            for match in matches:
	                match_list.append(match)
	            created_date  = (match_list[0]).date()
	            day_week_name = calendar.day_name[match_list[0].date().weekday()]
	            title = json.dumps(pulls[i]["title"], indent=1, sort_keys=True)
	            print("title: {:25} closed on:{}".format(title, day_week_name))
# week opend*****************************************
elif option.w_opened:
	user_git = input ("Input GIT username:\n")
	for i in range(len(pulls)):
	    temp = (json.dumps(pulls[i]["head"]["repo"]["owner"]["login"], indent=1, sort_keys=True))[1:-1]
	    if temp == user_git:
	        temp_state = json.dumps(pulls[i]["state"], indent=1, sort_keys=True)[1:-1]
	        if temp_state == 'open':
	            created_time = (json.dumps(pulls[i]["created_at"], indent=1, sort_keys=True))[1:11]
	            matches = datefinder.find_dates(created_time)
	            match_list = []
	            for match in matches:
	                match_list.append(match)
	            diff = datetime.datetime.today() - match_list[0]
	            number_week = diff.days // 7
	            title = json.dumps(pulls[i]["title"], indent=1, sort_keys=True)
	            print("title: {:25} opened :{} weeks ago".format(title, number_week))
# week closed*****************************************
elif option.w_closed:
	user_git = input ("Input GIT username:\n")
	for i in range(len(pulls)):
	    temp = (json.dumps(pulls[i]["head"]["repo"]["owner"]["login"], indent=1, sort_keys=True))[1:-1]
	    if temp == user_git:
	        temp_state = json.dumps(pulls[i]["state"], indent=1, sort_keys=True)[1:-1]
	        if temp_state == 'closed':
	            created_time = (json.dumps(pulls[i]["created_at"], indent=1, sort_keys=True))[1:11]
	            matches = datefinder.find_dates(created_time)
	            match_list = []
	            for match in matches:
	                match_list.append(match)
	            diff = datetime.datetime.today() - match_list[0]
	            number_week = diff.days // 7
	            title = json.dumps(pulls[i]["title"], indent=1, sort_keys=True)
	            print("title: {:25} closed :{} weeks ago".format(title, number_week))

