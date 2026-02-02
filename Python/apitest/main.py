import requests


def getJoke():
    url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"

    response = requests.get(url)
    data = response.json()

    if not data["error"]:
        match data["type"]:
            case "single":
                return data["joke"]
            case "twopart":
                return f"{data['setup']}\n{data['delivery']}"
            case _:
                return "what"
    else:
        return "oh god"


print(getJoke())
