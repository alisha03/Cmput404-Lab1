import requests
print(requests.__version__)

r = requests.get("http://www.google.com")
print(r.text)

r = requests.get("https://raw.githubusercontent.com/alisha03/Cmput404-Lab1/master/lab1.py")
print(r.text)