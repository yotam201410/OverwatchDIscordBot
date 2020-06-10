"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
class Combat:
    def __init__(self, js: dict):
        try:
            self._barrierDamageDone = js["barrierDamageDone"]
        except KeyError:
            self._barrierDamageDone = 0
        try:
            self._damageDone = js["damageDone"]
        except KeyError:
            self._damageDone = 0
        try:
            self._deaths = js["deaths"]
        except KeyError:
            self._deaths = 0
        try:
            self._eliminations = js["eliminations"]
        except KeyError:
            self._eliminations = 0
        try:
            self._environmentalKills = js["environmentalKills"]
        except KeyError:
            self._environmentalKills = 0
        try:
            self._finalBlows = js["finalBlows"]
        except KeyError:
            self._finalBlows = 0
        try:
            self._heroDamageDone = js["heroDamageDone"]
        except KeyError:
            self._heroDamageDone = 0
        try:
            self._meleeFinalBlows = js["meleeFinalBlows"]
        except KeyError:
            self._meleeFinalBlows = 0
        try:
            self._multikills = js["multikills"]
        except KeyError:
            self._multikills = 0
        try:
            self._objectiveKills = js["objectiveKills"]
        except KeyError:
            self._objectiveKills = 0
        try:
            self._objectiveTime = js["objectiveTime"]
        except KeyError:
            self._objectiveTime = 0
        try:
            self._soloKills = js["soloKills"]
        except KeyError:
            self._soloKills = 0
        try:
            self._timeSpentOnFire = js["timeSpentOnFire"]
        except KeyError:
            self._timeSpentOnFire = 0

    @property
    def barrierDamageDone(self):
        return self._barrierDamageDone

    @property
    def damageDone(self):
        return self._damageDone

    @property
    def deaths(self):
        return self._deaths

    @property
    def eliminations(self):
        return self._eliminations

    @property
    def environmentalKills(self):
        return self._environmentalKills

    @property
    def finalBlows(self):
        return self._finalBlows

    @property
    def heroDamageDone(self):
        return self._heroDamageDone

    @property
    def meleeFinalBlows(self):
        return self._meleeFinalBlows

    @property
    def multikills(self):
        return self._multikills

    @property
    def objectiveKills(self):
        return self._objectiveKills

    @property
    def objectiveTime(self):
        return self._objectiveTime

    @property
    def soloKills(self):
        return self._soloKills

    @property
    def timeSpentOnFire(self):
        return self._timeSpentOnFire
