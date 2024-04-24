import json
from random import randint


def read_json(key):
    with open("cards.json", "r") as file:
        data = json.load(file)[key]
    return data[randint(0, len(data))]


if __name__ == '__main__':
    print(read_json("objects"))
