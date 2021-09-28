# This script shows who has unfollowed you until last execution.
# Developed by Hardin Argent 2021
import os
from datetime import date
import instaloader as instaloader

today = date.today()
str_today = today.strftime('%d-%m-%Y')
path = "archive/" + str_today + ".txt"
L = instaloader.Instaloader()

username = "FILL YOUR USERNAME"
password = "FILL YOUR PASSWORD"
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, username)
os.rename("old.txt", path)
os.rename("now.txt", "old.txt")
follow_list = []
count = 0
for followee in profile.get_followers():
    follow_list.append(followee.username)
    file = open("now.txt", "a+")
    file.write(follow_list[count])
    file.write("\n")
    file.close()
    count = count + 1
old_list = []
with open('old.txt') as old_list_file:
    for line in old_list_file:
        stripped = line.strip('\n')
        old_list.append(stripped)
print("Those users are idiots, unfollow them:")
for follower in old_list:
    if follower not in follow_list:
        print(follower)
