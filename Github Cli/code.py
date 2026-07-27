import urllib.request as urlreq
import urllib.error
import json

print(r"""

  ________.__  __     ___ ___      ___.     _________ .__  .__ 
 /  _____/|__|/  |_  /   |   \ __ _\_ |__   \_   ___ \|  | |__|
/   \  ___|  \   __\/    ~    \  |  \ __ \  /    \  \/|  | |  |
\    \_\  \  ||  |  \    Y    /  |  / \_\ \ \     \___|  |_|  |
 \______  /__||__|   \___|_  /|____/|___  /  \______  /____/__|
        \/                 \/           \/          \/         


""")


print(" Enter Username: ",end="")
username=input()
url = f"https://api.github.com/users/{username}/events"
try:
    response = urlreq.urlopen(url)
except urllib.error.HTTPError:
    print(" Invalid Username ")
    exit()
    
print(response.status)
raw_data = response.read()

data = json.loads(raw_data)

#print(json.dumps(data, indent=2))

for event in data:
    event_type = event["type"]
    repo_name = event["repo"]["name"]
    print(event_type, repo_name)