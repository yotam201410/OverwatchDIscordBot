import json


class Globals:
    def __init__(self):
        self.jsonfile = json.load(open("../java/Repositories/users.json", 'r', encoding="utf-8"))
