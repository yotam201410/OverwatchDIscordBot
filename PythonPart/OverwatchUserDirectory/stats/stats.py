"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.stats.Lhero import Lhero
from OverwatchUserDirectory.stats.careerstats import CareerStats


class Stats:
    def __init__(self, js: dict):
        self.top_heroes_list = []
        for lhero in js["topHeroes"].items():
            self.top_heroes_list.append(Lhero(lhero[1], lhero[0]))
        self.career_stats = CareerStats(js["careerStats"])

