"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
class MatchAwards:
    def __init__(self, js: dict):
        try:
            self._cards = js["cards"]
        except KeyError:
            self._cards = 0
        self._medals = js["medals"]
        self._medalsBronze = js["medalsBronze"]
        self._medalsGold = js["medalsGold"]
        self._medalsSilver = js["medalsSilver"]

    @property
    def cards(self):
        return self._cards

    @property
    def medals(self):
        return self._medals

    @property
    def medalsBronze(self):
        return self._medalsBronze

    @property
    def medalsGold(self):
        return self._medalsGold

    @property
    def medalsSilver(self):
        return self._medalsSilver
