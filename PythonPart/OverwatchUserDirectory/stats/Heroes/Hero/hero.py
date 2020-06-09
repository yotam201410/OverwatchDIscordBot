"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.stats.Heroes.Hero.assists import Assists
from OverwatchUserDirectory.stats.Heroes.Hero.average import Average
from OverwatchUserDirectory.stats.Heroes.Hero.best import Best
from OverwatchUserDirectory.stats.Heroes.Hero.combat import Combat
from OverwatchUserDirectory.stats.Heroes.Hero.game import Game
from OverwatchUserDirectory.stats.Heroes.Hero.heroSpecific import HeroSpecific
from OverwatchUserDirectory.stats.Heroes.Hero.matchAwards import MatchAwards
from OverwatchUserDirectory.stats.Heroes.Hero.miscellaneous import Miscellaneous


class Hero:
    def __init__(self, js: dict, hero: str):
        self.hero = hero
        if js["assists"] is not None:
            self._assists = Assists(js["assists"])
        else:
            self._assists = None
        if js["average"] is not None:
            self._average = Average(js["average"])
        else:
            self._average = None
        if js["best"] is not None:
            self._best = Best(js["best"])
        else:
            self._best = None
        if js["combat"] is not None:
            self._combat = Combat(js["combat"])
        else:
            self._combat = None
        if js["game"] is not None:
            self._game = Game(js["game"])
        else:
            self._game = None
        if js["heroSpecific"] is not None:
            self._heroSpecific = HeroSpecific(js["heroSpecific"], self.hero)
        else:
            self._heroSpecific = None
        if js["matchAwards"] is not None:
            self._matchAwards = MatchAwards(js["matchAwards"])
        else:
            self._matchAwards = None
        if js["miscellaneous"] is not None:
            self._miscellaneous = Miscellaneous(js["miscellaneous"])

    @property
    def assists(self):
        return self._assists

    @property
    def average(self):
        return self._average

    @property
    def best(self):
        return self._best

    @property
    def combat(self):
        return self._combat

    @property
    def game(self):
        return self._game

    @property
    def matchAwards(self):
        return self._matchAwards

    @property
    def miscellaneous(self):
        return self._miscellaneous
