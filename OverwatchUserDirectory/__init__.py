"""
MIT License
Copyright (c) 2020 Yotam Rechnitz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from OverwatchUserDirectory.ratings.Ratings import Ratings
import requests
from OverwatchUserDirectory.stats.stats import Stats


class User:
    def __init__(self, user: str):
        user = user.split("#")
        user = "-".join(user)
        website = requests.get(f"https://ovrstat.com/stats/pc/{user}")
        js = website.json()
        try:
            self.name = js["name"]
            self._icon = js["icon"]

            self.levelIcon = js["levelIcon"]
            self.endorsement = js["endorsement"]
            self.endorsementIcon = js["endorsementIcon"]
            self.prestigeIcon = js['prestigeIcon']
            if js["private"] is True:
                self.ratings = None
                self.gamesWon = None
                self.quickPlayStats = None
                self.competitiveStats = None
            else:
                self.ratings = Ratings(js["ratings"])
                self.gamesWon = js["gamesWon"]
                self.quickPlayStats = Stats(js["quickPlayStats"])
                self.competitiveStats = Stats(js["competitiveStats"])
            self.private = js["private"]
        except KeyError:
            self.name = None
            self.icon = None
            self.levelIcon = None
            self.endorsement = None
            self.endorsementIcon = None
            self.prestigeIcon = None
            self.ratings = None
            self.gamesWon = None
            self.quickPlayStats = None
            self.competitiveStats = None
            self.private = None
