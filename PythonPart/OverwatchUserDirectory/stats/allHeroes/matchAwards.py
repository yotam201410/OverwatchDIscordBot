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
        try:
            self._medals = js["medals"]
        except KeyError:
            self._medals = 0
        try:
            self._medalsBronze = js["medalsBronze"]
        except KeyError:
            self._medalsBronze = 0
        try:
            self._medalsGold = js["medalsGold"]
        except KeyError:
            self._medalsGold = 0
        try:
            self._medalsSilver = js["medalsSilver"]
        except KeyError:
            self._medalsSilver = 0

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
