"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""


class Best:
    def __init__(self, js: dict):
        try:
            self._allDamageDoneMostInGame = js["allDamageDoneMostInGame"]
        except KeyError:
            self._allDamageDoneMostInGame = 0
        try:
            self._barrierDamageDoneMostInGame = js["barrierDamageDoneMostInGame"]
        except KeyError:
            self._barrierDamageDoneMostInGame = 0
        try:
            self._defensiveAssistsMostInGame = js["defensiveAssistsMostInGame"]
        except KeyError:
            self._defensiveAssistsMostInGame = 0
        try:
            self._eliminationsMostInGame = js["eliminationsMostInGame"]
        except KeyError:
            self._eliminationsMostInGame = 0
        try:
            self._environmentalKillsMostInGame = js["environmentalKillsMostInGame"]
        except KeyError:
            self._environmentalKillsMostInGame = 0
        try:
            self._finalBlowsMostInGame = js["finalBlowsMostInGame"]
        except KeyError:
            self._finalBlowsMostInGame = 0
        try:
            self._healingDoneMostInGame = js["healingDoneMostInGame"]
        except KeyError:
            self._healingDoneMostInGame = 0
        try:
            self._heroDamageDoneMostInGame = js["heroDamageDoneMostInGame"]
        except KeyError:
            self._heroDamageDoneMostInGame = 0
        try:
            self._killsStreakBest = js["killsStreakBest"]
        except KeyError:
            self._killsStreakBest = 0
        try:
            self._meleeFinalBlowsMostInGame = js["meleeFinalBlowsMostInGame"]
        except KeyError:
            self._meleeFinalBlowsMostInGame = 0
        try:
            self._multikillsBest = js["multikillsBest"]
        except KeyError:
            self._multikillsBest = 0
        try:
            self._objectiveKillsMostInGame = js["objectiveKillsMostInGame"]
        except KeyError:
            self._objectiveKillsMostInGame = 0
        try:
            self._objectiveTimeMostInGame = js["objectiveTimeMostInGame"]
        except KeyError:
            self._objectiveTimeMostInGame = 0
        try:
            self._offensiveAssistsMostInGame = js["offensiveAssistsMostInGame"]
        except KeyError:
            self._offensiveAssistsMostInGame = 0
        try:
            self._reconAssistsMostInGame = js["reconAssistsMostInGame"]
        except KeyError:
            self._reconAssistsMostInGame = 0
        try:
            self._soloKillsMostInGame = js["soloKillsMostInGame"]
        except KeyError:
            self._soloKillsMostInGame = 0
        try:
            self._teleporterPadsDestroyedMostInGame = js["teleporterPadsDestroyedMostInGame"]
        except KeyError:
            self._teleporterPadsDestroyedMostInGame = 0
        try:
            self._timeSpentOnFireMostInGame = js["timeSpentOnFireMostInGame"]
        except KeyError:
            self._timeSpentOnFireMostInGame = 0
        try:
            self._turretsDestroyedMostInGame = js["turretsDestroyedMostInGame"]
        except KeyError:
            self._turretsDestroyedMostInGame = 0

    @property
    def allDamageDoneMostInGame(self):
        return self._allDamageDoneMostInGame

    @property
    def barrierDamageDoneMostInGame(self):
        return self._barrierDamageDoneMostInGame

    @property
    def defensiveAssistsMostInGame(self):
        return self._defensiveAssistsMostInGame

    @property
    def eliminationsMostInGame(self):
        return self._eliminationsMostInGame

    @property
    def environmentalKillsMostInGame(self):
        return self._environmentalKillsMostInGame

    @property
    def finalBlowsMostInGame(self):
        return self._finalBlowsMostInGame

    @property
    def healingDoneMostInGame(self):
        return self._healingDoneMostInGame

    @property
    def heroDamageDoneMostInGame(self):
        return self._heroDamageDoneMostInGame

    @property
    def killsStreakBest(self):
        return self._killsStreakBest

    @property
    def meleeFinalBlowsMostInGame(self):
        return self._meleeFinalBlowsMostInGame

    @property
    def multikillsBest(self):
        return self._multikillsBest

    @property
    def objectiveKillsMostInGame(self):
        return self._objectiveKillsMostInGame

    @property
    def objectiveTimeMostInGame(self):
        return self._objectiveTimeMostInGame

    @property
    def offensiveAssistsMostInGame(self):
        return self._offensiveAssistsMostInGame

    @property
    def reconAssistsMostInGame(self):
        return self._reconAssistsMostInGame

    @property
    def soloKillsMostInGame(self):
        return self._soloKillsMostInGame

    @property
    def teleporterPadsDestroyedMostInGame(self):
        return self._teleporterPadsDestroyedMostInGame

    @property
    def timeSpentOnFireMostInGame(self):
        return self._timeSpentOnFireMostInGame

    @property
    def turretsDestroyedMostInGame(self):
        return self._turretsDestroyedMostInGame
