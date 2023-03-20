import requests

url = f"https://idiotcreaturehater.pythonanywhere.com/api?input={question}"
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
print(f"{response.text}")
