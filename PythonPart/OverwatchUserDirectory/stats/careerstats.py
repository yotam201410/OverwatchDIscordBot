"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.stats.allHeroes.AllHeroes import AllHeroes
from OverwatchUserDirectory.stats.Heroes.Hero.hero import Hero


class CareerStats:
    def __init__(self, js: dict):
        hero_name_list = ["ana", "ashe", "baptiste", "bastion", "brigitte", "dVa", "doomfist", "echo", "genji", "hanzo",
                          "junkrat", "lucio", "mccree", "mei", "mercy", "moira", "orisa", "pharah", "reaper",
                          "reinhardt", "roadhog", "sigma", "soldier76", "sombra", "symmetra", "torbjorn", "tracer",
                          "widowmaker", "winston", "wreckingBall", "zarya", "zenyatta"]
        self.all_Heroes = AllHeroes(js["allHeroes"])
        self.hero_dict = {}
        for only_hero in hero_name_list:
            try:
                self.hero_dict[only_hero] = Hero(js[only_hero], only_hero)
            except KeyError:
                pass
