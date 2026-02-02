import requests
from random import randint
import json


def getJoke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

    response = requests.get(url)
    data = response.json()

    if not data["error"]:
        match data["type"]:
            case "single":
                return data["joke"]  # Single joke? RETURN JOKE
            case "twopart":
                return f"{data['setup']}\n{data['delivery']}"  # Two part joke? RETURN BOTH PARTS
            case _:
                return "what"  # oh god, oh no, something's not right
    else:
        return "oh god"  # OH GOD NO


def getPlaceholder():
    url = f"https://jsonplaceholder.typicode.com/posts/{randint(1, 100)}"

    response = requests.get(url)
    data = response.json()

    return f"Title: {data['title']}\n\nBody: {data['body']}"


print(getPlaceholder())
