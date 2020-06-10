"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
class Lhero:
    def __init__(self, js: dict, hero: str):
        self.hero = hero
        try:
            self._time_played = js["timePlayed"]
        except KeyError:
            self._time_played = 0
        try:
            self._games_won = js["gamesWon"]
        except KeyError:
            self._games_won = 0
        try:
            self._win_percentage = js["winPercentage"]
        except KeyError:
            self._win_percentage = 0
        try:
            self._weapon_accuracy = js["weaponAccuracy"]
        except KeyError:
            self._weapon_accuracy = 0
        try:
            self._eliminations_per_life = js["eliminationsPerLife"]
        except KeyError:
            self._eliminations_per_life = 0
        try:
            self._multi_kill_best = js["multiKillBest"]
        except KeyError:
            self._multi_kill_best = 0
        try:
            self._objective_kills = js["objectiveKills"]
        except KeyError:
            self._objective_kills = 0

    @property
    def time_played(self):
        return self._time_played

    @property
    def games_won(self):
        return self._games_won

    @property
    def win_percentage(self):
        return self._win_percentage

    @property
    def weapon_accuracy(self):
        return self._weapon_accuracy

    @property
    def eliminations_per_life(self):
        return self._eliminations_per_life

    @property
    def multi_kill_best(self):
        return self._multi_kill_best

    @property
    def objective_kills(self):
        return self._objective_kills
