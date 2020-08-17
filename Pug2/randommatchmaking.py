import random


def is_full(team: tuple):
    counter = 0
    for i in team:
        if i is not None:
            counter += 1
    return True if counter == len(team) else False


def swapNoneWithValue(team: list, value):
    for i in range(len(team)):
        if team[i] is None:
            team[i] = value
            break
    return tuple(team)


class RandomMatch:
    def __init__(self, members: list, limit: int):
        self.members = members
        if limit == 5:
            self.red = (None, None, None, None, None)
            self.blue = (None, None, None, None, None)
            for i in range(10):
                r = random.randint(1, 2)
                if r == 1:
                    if not is_full(self.red):
                        red = list(self.red)
                        self.red = swapNoneWithValue(red, members[i])
                    else:
                        blue = list(self.blue)
                        self.blue = swapNoneWithValue(blue, members[i])
                if r == 2:
                    if not is_full(self.blue):
                        blue = list(self.blue)
                        self.blue = swapNoneWithValue(blue, members[i])
                    else:
                        red = list(self.red)
                        self.red = swapNoneWithValue(red, members[i])
        if limit == 6:
            self.red = (None, None, None, None, None, None)
            self.blue = (None, None, None, None, None, None)
            for i in range(10):
                r = random.randint(1, 2)
                if r == 1:
                    if not is_full(self.red):
                        red = list(self.red)
                        self.red = swapNoneWithValue(red, members[i])
                    else:
                        blue = list(self.blue)
                        self.blue = swapNoneWithValue(blue, members[i])
                if r == 2:
                    if not is_full(self.blue):
                        blue = list(self.blue)
                        self.blue = swapNoneWithValue(blue, members[i])
                    else:
                        red = list(self.red)
                        self.red = swapNoneWithValue(red, members[i])
        self.red_cap = self.red[0]
        self.blue_cap = self.blue[0]
