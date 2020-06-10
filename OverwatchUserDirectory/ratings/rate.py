"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""


class Rate:
    def __init__(self, js: dict):
        self._level = js["level"]
        self._role = js["role"]
        self._roleIcon = js["roleIcon"]
        self._rankIcon = js["rankIcon"]


    @property
    def level(self):
        return self._level

    @property
    def role(self):
        return self._role

    @property
    def roleIcon(self):
        return self._roleIcon

    @property
    def rankIcon(self):
        return self._rankIcon
