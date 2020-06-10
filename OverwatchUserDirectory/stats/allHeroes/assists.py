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
            self._healing_done = js["healingDone"]
        except KeyError:
            self._healing_done = 0
        try:
            self._offensive_assists = js["offensiveAssists"]
        except KeyError:
            self._offensive_assists = 0
        try:
            self._recon_assists = js["reconAssists"]
        except KeyError:
            self._recon_assists = 0

    @property
    def defensive_assists(self):
        return self._defensive_assists

    @property
    def healing_done(self):
        return self._healing_done

    @property
    def offensive_assists(self):
        return self._offensive_assists

    @property
    def recon_assists(self):
        return self._recon_assists
