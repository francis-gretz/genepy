import requests

try:
    r = requests.get("https://api.github.com/users/python", auth=("user", "pass"))

    print(r.text)
except:
    print("No internet connectivity.")
