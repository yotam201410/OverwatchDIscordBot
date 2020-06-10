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
            self._allDamageDoneMostInLife = js["allDamageDoneMostInLife"]
        except KeyError:
            self._allDamageDoneMostInLife = 0
        try:
            self._barrierDamageDoneMostInGame = js["barrierDamageDoneMostInGame"]
        except KeyError:
            self._barrierDamageDoneMostInGame = 0
        try:
            self._eliminationsMostInGame = js["eliminationsMostInGame"]
        except KeyError:
            self._eliminationsMostInGame = 0
        try:
            self._eliminationsMostInLife = js["eliminationsMostInLife"]
        except KeyError:
            self._eliminationsMostInLife = 0
        try:
            self._finalBlowsMostInGame = js["finalBlowsMostInGame"]
        except KeyError:
            self._finalBlowsMostInGame = 0
        try:
            self._heroDamageDoneMostInGame = js["heroDamageDoneMostInGame"]
        except KeyError:
            self._heroDamageDoneMostInGame = 0
        try:
            self._heroDamageDoneMostInLife = js["heroDamageDoneMostInLife"]
        except KeyError:
            self._heroDamageDoneMostInLife = 0
        try:
            self._killsStreakBest = js["killsStreakBest"]
        except KeyError:
            self._killsStreakBest = 0
        try:
            self._objectiveKillsMostInGame = js["objectiveKillsMostInGame"]
        except KeyError:
            self._objectiveKillsMostInGame = 0
        try:
            self._objectiveTimeMostInGame = js["objectiveTimeMostInGame"]
        except KeyError:
            self._objectiveTimeMostInGame = 0
        try:
            self._soloKillsMostInGame = js["soloKillsMostInGame"]
        except KeyError:
            self._soloKillsMostInGame = 0
        try:
            self._timeSpentOnFireMostInGame = js["timeSpentOnFireMostInGame"]
        except KeyError:
            self._timeSpentOnFireMostInGame = 0
        try:
            self._weaponAccuracyBestInGame = js["weaponAccuracyBestInGame"]
        except KeyError:
            self._weaponAccuracyBestInGame = 0
        try:
            self._criticalHitsMostInGame = js["criticalHitsMostInGame"]
        except KeyError:
            self._criticalHitsMostInGame = 0
        try:
            self._criticalHitsMostInLife = js["criticalHitsMostInLife"]
        except KeyError:
            self._criticalHitsMostInLife = 0
        try:
            self._meleeFinalBlowsMostInGame = js["meleeFinalBlowsMostInGame"]
        except KeyError:
            self._meleeFinalBlowsMostInGame = 0
        try:
            self._multikillsBest = js["multikillsBest"]
        except KeyError:
            self._multikillsBest = 0

    @property
    def allDamageDoneMostInGam(self):
        return self._allDamageDoneMostInGame

    @property
    def allDamageDoneMostInLife(self):
        return self._allDamageDoneMostInLife

    @property
    def barrierDamageDoneMostInGame(self):
        return self._barrierDamageDoneMostInGame

    @property
    def eliminationsMostInGame(self):
        return self._eliminationsMostInGame

    @property
    def eliminationsMostInLife(self):
        return self._eliminationsMostInLife

    @property
    def finalBlowsMostInGame(self):
        return self._finalBlowsMostInGame

    @property
    def heroDamageDoneMostInGame(self):
        return self._heroDamageDoneMostInGame

    @property
    def heroDamageDoneMostInLife(self):
        return self._heroDamageDoneMostInLife

    @property
    def killsStreakBest(self):
        return self._killsStreakBest

    @property
    def objectiveKillsMostInGame(self):
        return self._objectiveKillsMostInGame

    @property
    def objectiveTimeMostInGame(self):
        return self._objectiveTimeMostInGame

    @property
    def soloKillsMostInGame(self):
        return self._soloKillsMostInGame

    @property
    def timeSpentOnFireMostInGame(self):
        return self._timeSpentOnFireMostInGame

    @property
    def weaponAccuracyBestInGame(self):
        return self._weaponAccuracyBestInGame

    @property
    def criticalHitsMostInGame(self):
        return self._criticalHitsMostInGame

    @property
    def criticalHitsMostInLife(self):
        return self._criticalHitsMostInLife

    @property
    def meleeFinalBlowsMostInGame(self):
        return self._meleeFinalBlowsMostInGame

    @property
    def multikillsBest(self):
        return self._multikillsBest
