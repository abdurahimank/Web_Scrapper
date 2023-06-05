# Stage 1/5: Wanna Talk to the Internet?
import requests


url = input()
response = requests.get(url)
if response.status_code == 200:
    try:
        print("\n", response.json()['content'], sep="")
    except KeyError:
        print("\nInvalid quote resource!")
else:
    print("\nInvalid quote resource!")
    