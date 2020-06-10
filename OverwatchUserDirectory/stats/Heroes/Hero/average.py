"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
class Average:
    def __init__(self, js: dict):
        try:
            self._allDamageDoneAvgPer10Min = js["allDamageDoneAvgPer10Min"]
        except KeyError:
            self._allDamageDoneAvgPer10Min = 0
        try:
            self._barrierDamageDoneAvgPer10Min = js["barrierDamageDoneAvgPer10Min"]
        except KeyError:
            self._barrierDamageDoneAvgPer10Min = 0
        try:
            self._deathsAvgPer10Min = js["deathsAvgPer10Min"]
        except KeyError:
            self._deathsAvgPer10Min = 0
        try:
            self._eliminationsAvgPer10Min = js["eliminationsAvgPer10Min"]
        except KeyError:
            self._eliminationsAvgPer10Min = 0
        try:
            self._eliminationsPerLife = js["eliminationsPerLife"]
        except KeyError:
            self._eliminationsPerLife = 0
        try:
            self._finalBlowsAvgPer10Min = js["finalBlowsAvgPer10Min"]
        except KeyError:
            self._finalBlowsAvgPer10Min = 0
        try:
            self._healingDoneAvgPer10Min = js["healingDoneAvgPer10Min"]
        except KeyError:
            self._healingDoneAvgPer10Min = 0
        try:
            self._heroDamageDoneAvgPer10Min = js["heroDamageDoneAvgPer10Min"]
        except KeyError:
            self._heroDamageDoneAvgPer10Min = 0
        try:
            self._meleeFinalBlowsAvgPer10Min = js["meleeFinalBlowsAvgPer10Min"]
        except KeyError:
            self._meleeFinalBlowsAvgPer10Min = 0
        try:
            self._objectiveKillsAvgPer10Min = js["objectiveKillsAvgPer10Min"]
        except KeyError:
            self._objectiveKillsAvgPer10Min = 0
        try:
            self._objectiveTimeAvgPer10Min = js["objectiveTimeAvgPer10Min"]
        except KeyError:
            self._objectiveTimeAvgPer10Min = 0
        try:
            self._soloKillsAvgPer10Min = js["soloKillsAvgPer10Min"]
        except KeyError:
            self._soloKillsAvgPer10Min = 0
        try:
            self._timeSpentOnFireAvgPer10Min = js["timeSpentOnFireAvgPer10Min"]
        except KeyError:
            self._timeSpentOnFireAvgPer10Min = 0
        try:
            self._criticalHitsAvgPer10Min = js["criticalHitsAvgPer10Min"]
        except KeyError:
            self._criticalHitsAvgPer10Min = 0

    @property
    def allDamageDoneAvgPer10Min(self):
        return self._allDamageDoneAvgPer10Min

    @property
    def barrierDamageDoneAvgPer10Min(self):
        return self._barrierDamageDoneAvgPer10Min

    @property
    def deathsAvgPer10Min(self):
        return self._deathsAvgPer10Min

    @property
    def eliminationsAvgPer10Min(self):
        return self._eliminationsAvgPer10Min

    @property
    def eliminationsPerLife(self):
        return self._eliminationsPerLife

    @property
    def finalBlowsAvgPer10Min(self):
        return self._finalBlowsAvgPer10Min

    @property
    def healingDoneAvgPer10Min(self):
        return self._healingDoneAvgPer10Min

    @property
    def heroDamageDoneAvgPer10Min(self):
        return self._heroDamageDoneAvgPer10Min

    @property
    def meleeFinalBlowsAvgPer10Min(self):
        return self._meleeFinalBlowsAvgPer10Min

    @property
    def objectiveKillsAvgPer10Min(self):
        return self._objectiveKillsAvgPer10Min

    @property
    def objectiveTimeAvgPer10Min(self):
        return self._objectiveTimeAvgPer10Min

    @property
    def soloKillsAvgPer10Min(self):
        return self._soloKillsAvgPer10Min

    @property
    def timeSpentOnFireAvgPer10Min(self):
        return self._timeSpentOnFireAvgPer10Min

    @property
    def criticalHitsAvgPer10Min(self):
        return self._criticalHitsAvgPer10Min
