"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
class Miscellaneous:
    def __init__(self, js: dict):
        try:
            self._teleporterPadsDestroyed = js["teleporterPadsDestroyed"]
        except KeyError:
            self._teleporterPadsDestroyed = 0
        try:
            self._turretsDestroyed = js["turretsDestroyed"]
        except KeyError:
            self._turretsDestroyed = 0

    @property
    def teleporterPadsDestroyed(self):
        return self._teleporterPadsDestroyed

    @property
    def turretsDestroyed(self):
        return self._turretsDestroyed
