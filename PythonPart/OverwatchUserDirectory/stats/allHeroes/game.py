"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
class Game:
    def __init__(self, js: dict):
        try:
            self._gamesWon = js["gamesWon"]
        except KeyError:
            self._gamesWon = 0
        try:
            self._timePlayed = js["timePlayed"]
        except KeyError:
            self._timePlayed = "0:0:0"

    @property
    def gamesWon(self):
        return self._gamesWon

    @property
    def timePlayed(self):
        return self._timePlayed
