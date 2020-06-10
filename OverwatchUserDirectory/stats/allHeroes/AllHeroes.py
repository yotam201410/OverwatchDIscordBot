"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.stats.allHeroes.assists import Assists
from OverwatchUserDirectory.stats.allHeroes.average import Average
from OverwatchUserDirectory.stats.allHeroes.combat import Combat
from OverwatchUserDirectory.stats.allHeroes.game import Game
from OverwatchUserDirectory.stats.allHeroes.matchAwards import MatchAwards
from OverwatchUserDirectory.stats.allHeroes.miscellaneous import Miscellaneous


class AllHeroes:
    def __init__(self, js: dict):
        if js["assists"] is not None:
            self.assists = Assists(js["assists"])
        else:
            self._assists = None
        if js["average"] is not None:
            self.average = Average(js["average"])
        else:
            self.average = None
        if js["combat"] is not None:
            self.combat = Combat(js["combat"])
        else:
            self.combat = None
        if js["game"] is not None:
            self.game = Game(js["game"])
        else:
            self.game = None
        if js["matchAwards"] is not None:
            self.matchAwards = MatchAwards(js["matchAwards"])
        else:
            self.matchAwards = None
        if js["miscellaneous"] is not None:
            self.miscellaneous = Miscellaneous(js["miscellaneous"])
        else:
            self.miscellaneous = None
