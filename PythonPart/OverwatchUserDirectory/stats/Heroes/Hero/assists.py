"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
class Assists:
    def __init__(self, js: dict):
        try:
            self._defensive_assists = js["defensiveAssists"]
        except KeyError:
            self._defensive_assists = 0
        try:
            self._defensiveAssistsAvgPer10Min = js["defensiveAssistsAvgPer10Min"]
        except KeyError:
            self._defensiveAssistsAvgPer10Min = 0
        try:
            self._defensiveAssistsMostInGame = js["defensiveAssistsMostInGame"]
        except KeyError:
            self._defensiveAssistsMostInGame = 0
        try:
            self._healing_done = js["healingDone"]
        except KeyError:
            self._healing_done = 0
        try:
            self._healingDoneMostInGame = js["healingDoneMostInGame"]
        except KeyError:
            self._healingDoneMostInGame = 0
        try:
            self._offensive_assists = js["offensiveAssists"]
        except KeyError:
            self._offensive_assists = 0
        try:
            self._offensiveAssistsAvgPer10Min = js["offensiveAssistsAvgPer10Min"]
        except KeyError:
            self._offensiveAssistsAvgPer10Min = 0
        try:
            self._offensiveAssistsMostInGame = js["offensiveAssistsMostInGame"]
        except KeyError:
            self._offensiveAssistsMostInGame = 0
        try:
            self._reconAssists = js["reconAssists"]
        except KeyError:
            self._reconAssists = 0
        try:
            self._reconAssistsAvgPer10Min = js["reconAssistsAvgPer10Min"]
        except KeyError:
            self._reconAssistsAvgPer10Min = 0
        try:
            self._reconAssistsMostInGame = js["reconAssistsMostInGame"]
        except KeyError:
            self._reconAssistsMostInGame = 0

    @property
    def defensive_assists(self):
        return self._defensive_assists

    @property
    def defensiveAssistsAvgPer10Min(self):
        return self._defensiveAssistsAvgPer10Min

    @property
    def defensiveAssistsMostInGame(self):
        return self._defensiveAssistsMostInGame

    @property
    def healing_done(self):
        return self._healing_done

    @property
    def healingDoneMostInGame(self):
        return self._healingDoneMostInGame

    @property
    def offensive_assists(self):
        return self._offensive_assists

    @property
    def offensiveAssistsAvgPer10Min(self):
        return self._offensiveAssistsAvgPer10Min

    @property
    def offensiveAssistsMostInGame(self):
        return self._offensiveAssistsMostInGame

    @property
    def reconAssists(self):
        return self._reconAssists

    @property
    def reconAssistsAvgPer10Min(self):
        return self._reconAssistsAvgPer10Min

    @property
    def reconAssistsMostInGame(self):
        return self._reconAssistsMostInGame
