"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.ratings.rate import Rate


class Ratings:
    def __init__(self, js: list):
        self.tank = None
        self.support = None
        self.damage = None
        for role in js:
            if role["role"] == "tank":
                self.tank = Rate(role)
            elif role["role"] == "damage":
                self.damage = Rate(role)
            elif role["role"] == "support":
                self.support = Rate(role)
        if self.tank is not None and self.damage is not None and self.support is not None:
            self._average_level = round(float(self.tank.level + self.damage.level + self.support.level) / 3)
        else:
            self._average_level = None

    @property
    def average_level(self):
        return self._average_level
