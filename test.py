import requests

# First Program tested ping to Google
response = requests.get("https://www.google.com")

# print(response.status_code)

for i in response:
    if response.status_code == 200:
        print("Request is successful")
        break
    else:
        print("Connection refused...")

# VS Code multiple comment of codes - Ctrl + /

print("Please add your target")

target = input(str())

response = requests.get("https://{}".format(target))

if response.status_code == 200:
    print("{} successfully pinging".format(target))
else:
    print("{} not available".format(target))

