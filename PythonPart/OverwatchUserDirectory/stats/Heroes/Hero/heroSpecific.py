"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
class HeroSpecific:
    def __init__(self, js: dict, hero: str):
        if hero == "ana":
            try:
                self._bioticGrenadeKills = js["bioticGrenadeKills"]
            except KeyError:
                self._bioticGrenadeKills = 0
            try:
                self._enemiesSlept = js["enemiesSlept"]
            except KeyError:
                self._enemiesSlept = 0
            try:
                self._enemiesSleptAvgPer10Min = js["enemiesSleptAvgPer10Min"]
            except KeyError:
                self._enemiesSleptAvgPer10Min = 0
            try:
                self._enemiesSleptMostInGame = js["enemiesSleptMostInGame"]
            except KeyError:
                self._enemiesSleptMostInGame = 0
            try:
                self._healingAmplified = js["healingAmplified"]
            except KeyError:
                self._healingAmplified = 0
            try:
                self._healingAmplifiedAvgPer10Min = js["healingAmplifiedAvgPer10Min"]
            except KeyError:
                self._healingAmplifiedAvgPer10Min = 0
            try:
                self._healingAmplifiedMostInGame = js["healingAmplifiedMostInGame"]
            except KeyError:
                self._healingAmplifiedMostInGame = 0
            try:
                self._nanoBoostAssists = js["nanoBoostAssists"]
            except KeyError:
                self._nanoBoostAssists = 0
            try:
                self._nanoBoostAssistsAvgPer10Min = js["nanoBoostAssistsAvgPer10Min"]
            except KeyError:
                self._nanoBoostAssistsAvgPer10Min = 0
            try:
                self._nanoBoostAssistsMostInGame = js["nanoBoostAssistsMostInGame"]
            except KeyError:
                self._nanoBoostAssistsMostInGame = 0
            try:
                self._nanoBoostsApplied = js["nanoBoostsApplied"]
            except KeyError:
                self._nanoBoostsApplied = 0
            try:
                self._nanoBoostsAppliedAvgPer10Min = js["nanoBoostsAppliedAvgPer10Min"]
            except KeyError:
                self._nanoBoostAssistsAvgPer10Min = 0
            try:
                self._nanoBoostsAppliedMostInGame = js["nanoBoostsAppliedMostInGame"]
            except KeyError:
                self._nanoBoostsAppliedMostInGame = 0
            try:
                self._scopedAccuracy = js["scopedAccuracy"]
            except KeyError:
                self._scopedAccuracy = "0%"
            try:
                self._scopedAccuracyBestInGame = js["scopedAccuracyBestInGame"]
            except KeyError:
                self._scopedAccuracyBestInGame = "0%"
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
            try:
                self._unscopedAccuracy = js["unscopedAccuracy"]
            except KeyError:
                self._unscopedAccuracy = 0
            try:
                self._unscopedAccuracyBestInGame = js["unscopedAccuracyBestInGame"]
            except KeyError:
                self._unscopedAccuracyBestInGame = 0
        elif hero == "ashe":

            try:
                self._dynamiteKills = js["dynamiteKills"]
            except KeyError:
                self._dynamiteKills = 0
            try:
                self._dynamiteKillsAvgPer10Min = js["dynamiteKillsAvgPer10Min"]
            except KeyError:
                self._dynamiteKillsAvgPer10Min = 0
            try:
                self._dynamiteKillsMostInGame = js["dynamiteKillsMostInGame"]
            except KeyError:
                self._dynamiteKillsMostInGame = 0
            try:
                self._scopedAccuracy = js["scopedAccuracy"]
            except KeyError:
                self._scopedAccuracy = 0
            try:
                self._scopedAccuracyBestInGame = js["scopedAccuracyBestInGame"]
            except KeyError:
                self._scopedAccuracyBestInGame = 0
            try:
                self._scopedCriticalHits = js["scopedCriticalHits"]
            except KeyError:
                self._scopedCriticalHits = 0
            try:
                self._scopedCriticalHitsAccuracy = js["scopedCriticalHitsAccuracy"]
            except KeyError:
                self._scopedCriticalHitsAccuracy = 0
            try:
                self._scopedCriticalHitsAvgPer10Min = js["scopedCriticalHitsAvgPer10Min"]
            except KeyError:
                self._scopedCriticalHitsAvgPer10Min = 0
            try:
                self._scopedCriticalHitsMostInGame = js["scopedCriticalHitsMostInGame"]
            except KeyError:
                self._scopedCriticalHitsMostInGame = 0
        elif hero == "baptiste":
            try:
                self._amplificationMatrixAssists = js["amplificationMatrixAssists"]
            except KeyError:
                self._amplificationMatrixAssists = 0
            try:
                self._amplificationMatrixAssistsAvgPer10Min = js["amplificationMatrixAssistsAvgPer10Min"]
            except KeyError:
                self._amplificationMatrixAssistsAvgPer10Min = 0
            try:
                self._amplificationMatrixAssistsBestInGame = js["amplificationMatrixAssistsBestInGame"]
            except KeyError:
                self._amplificationMatrixAssistsBestInGame = 0
            try:
                self._amplificationMatrixCastsAvgPer10Min = js["amplificationMatrixCastsAvgPer10Min"]
            except KeyError:
                self._amplificationMatrixCastsAvgPer10Min = 0
            try:
                self._amplificationMatrixCastsMostInGame = js["amplificationMatrixCastsMostInGame"]
            except KeyError:
                self._amplificationMatrixCastsMostInGame = 0
            try:
                self._damageAmplified = js["damageAmplified"]
            except KeyError:
                self._damageAmplified = 0
            try:
                self._damageAmplifiedAvgPer10Min = js["damageAmplifiedAvgPer10Min"]
            except KeyError:
                self._damageAmplifiedAvgPer10Min = 0
            try:
                self._damageAmplifiedMostInGame = js["damageAmplifiedMostInGame"]
            except KeyError:
                self._damageAmplifiedMostInGame = 0
            try:
                self._healingAccuracy = js["healingAccuracy"]
            except KeyError:
                self._healingAccuracy = 0
            try:
                self._healingAccuracyBestInGame = js["healingAccuracyBestInGame"]
            except KeyError:
                self._healingAccuracyBestInGame = 0
            try:
                self._healingAmplified = js["healingAmplified"]
            except KeyError:
                self._healingAmplified = 0
            try:
                self._healingAmplifiedAvgPer10Min = js["healingAmplifiedAvgPer10Min"]
            except KeyError:
                self._healingAmplifiedAvgPer10Min = 0
            try:
                self._healingAmplifiedMostInGame = js["healingAmplifiedMostInGame"]
            except KeyError:
                self._healingAmplifiedMostInGame = 0
            try:
                self._immortalityFieldDeathsPrevented = js["immortalityFieldDeathsPrevented"]
            except KeyError:
                self._immortalityFieldDeathsPrevented = 0
            try:
                self._immortalityFieldDeathsPreventedAvgPer10Min = js["immortalityFieldDeathsPreventedAvgPer10Min"]
            except KeyError:
                self._immortalityFieldDeathsPreventedAvgPer10Min = 0
            try:
                self._immortalityFieldDeathsPreventedMostInGame = js["immortalityFieldDeathsPreventedMostInGame"]
            except KeyError:
                self._immortalityFieldDeathsPreventedMostInGame = 0
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
        elif hero == "bastion":
            try:
                self._reconKills = js["reconKills"]
            except KeyError:
                self._reconKills = 0
            try:
                self._reconKillsAvgPer10Min = js["reconKillsAvgPer10Min"]
            except KeyError:
                self._reconKillsAvgPer10Min = 0
            try:
                self._reconKillsMostInGame = js["reconKillsMostInGame"]
            except KeyError:
                self._reconKillsMostInGame = 0
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
            try:
                self._sentryKills = js["sentryKills"]
            except KeyError:
                self._sentryKills = 0
            try:
                self._sentryKillsAvgPer10Min = js["sentryKillsAvgPer10Min"]
            except KeyError:
                self._sentryKillsAvgPer10Min = 0
            try:
                self._sentryKillsMostInGame = js["sentryKillsMostInGame"]
            except KeyError:
                self._sentryKillsMostInGame = 0
            try:
                self._tankKills = js["tankKills"]
            except KeyError:
                self._tankKills = 0
            try:
                self._tankKillsAvgPer10Min = js["tankKillsAvgPer10Min"]
            except KeyError:
                self._tankKillsAvgPer10Min = 0
            try:
                self._tankKillsMostInGame = js["tankKillsMostInGame"]
            except KeyError:
                self._tankKillsMostInGame = 0
        elif hero == "brigitte":
            try:
                self._armorProvided = js["armorProvided"]
            except KeyError:
                self._armorProvided = 0
            try:
                self._armorProvidedAvgPer10Min = js["armorProvidedAvgPer10Min"]
            except KeyError:
                self._armorProvidedAvgPer10Min = 0
            try:
                self._armorProvidedMostInGame = js["armorProvidedMostInGame"]
            except KeyError:
                self._armorProvidedMostInGame = 0
            try:
                self._damageBlocked = js["damageBlocked"]
            except KeyError:
                self._damageBlocked = 0
            try:
                self._damageBlockedAvgPer10Min = js["damageBlockedAvgPer10Min"]
            except KeyError:
                self._damageBlockedAvgPer10Min = 0
            try:
                self._damageBlockedMostInGame = js["damageBlockedMostInGame"]
            except KeyError:
                self._damageBlockedMostInGame = 0
            try:
                self._inspireUptimePercentage = js["inspireUptimePercentage"]
            except KeyError:
                self._inspireUptimePercentage = 0
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
        elif hero == "dVa":
            try:
                self._damageBlocked = js["damageBlocked"]
            except KeyError:
                self._damageBlocked = 0
            try:
                self._damageBlockedAvgPer10Min = js["damageBlockedAvgPer10Min"]
            except KeyError:
                self._damageBlockedAvgPer10Min = 0
            try:
                self._damageBlockedMostInGame = js["damageBlockedMostInGame"]
            except KeyError:
                self._damageBlockedMostInGame = 0
            try:
                self._mechDeaths = js["mechDeaths"]
            except KeyError:
                self._mechDeaths = 0
            try:
                self._mechsCalled = js["mechsCalled"]
            except KeyError:
                self._mechsCalled = 0
            try:
                self._mechsCalledAvgPer10Min = js["mechsCalledAvgPer10Min"]
            except KeyError:
                self._mechsCalledAvgPer10Min = 0
            try:
                self._mechsCalledMostInGame = js["mechsCalledMostInGame"]
            except KeyError:
                self._mechsCalledMostInGame = 0
            try:
                self._selfDestructKills = js["selfDestructKills"]
            except KeyError:
                self._selfDestructKills = 0
            try:
                self._selfDestructKillsAvgPer10Min = js["selfDestructKillsAvgPer10Min"]
            except KeyError:
                self._selfDestructKillsAvgPer10Min = 0
            try:
                self._selfDestructKillsMostInGame = js["selfDestructKillsMostInGame"]
            except KeyError:
                self._selfDestructKillsMostInGame = 0
        elif hero == "doomfist":
            try:
                self._abilityDamageDone = js["abilityDamageDone"]
            except KeyError:
                self._abilityDamageDone = 0
            try:
                self._abilityDamageDoneAvgPer10Min = js["abilityDamageDoneAvgPer10Min"]
            except KeyError:
                self._abilityDamageDoneAvgPer10Min = 0
            try:
                self._abilityDamageDoneMostInGame = js["abilityDamageDoneMostInGame"]
            except KeyError:
                self._abilityDamageDoneMostInGame = 0
            try:
                self._shieldsCreated = js["shieldsCreated"]
            except KeyError:
                self._shieldsCreated = 0
            try:
                self._shieldsCreatedAvgPer10Min = js["shieldsCreatedAvgPer10Min"]
            except KeyError:
                self._shieldsCreatedAvgPer10Min = 0
            try:
                self._shieldsCreatedMostInGame = js["shieldsCreatedMostInGame"]
            except KeyError:
                self._shieldsCreatedMostInGame = 0
        elif hero == "echo":
            try:
                self._duplicateKills = js["duplicateKills"]
            except KeyError:
                self._duplicateKills = 0
            try:
                self._duplicateKillsAvgPer10Min = js["duplicateKillsAvgPer10Min"]
            except KeyError:
                self._duplicateKillsAvgPer10Min = 0
            try:
                self._duplicateKillsMostInGame = js["duplicateKillsMostInGame"]
            except KeyError:
                self._duplicateKillsMostInGame = 0
            try:
                self._focusingBeamAccuracy = js["focusingBeamAccuracy"]
            except KeyError:
                self._focusingBeamAccuracy = 0
            try:
                self._focusingBeamKills = js["focusingBeamKills"]
            except KeyError:
                self._focusingBeamKills = 0
            try:
                self._focusingBeamKillsAvgPer10Min = js["focusingBeamKillsAvgPer10Min"]
            except KeyError:
                self._focusingBeamKillsAvgPer10Min = 0
            try:
                self._focusingBeamKillsMostInGame = js["focusingBeamKillsMostInGame"]
            except KeyError:
                self._focusingBeamKillsMostInGame = 0
            try:
                self._stickyBombsDirectHitsAccuracy = js["stickyBombsDirectHitsAccuracy"]
            except KeyError:
                self._stickyBombsDirectHitsAccuracy = 0
            try:
                self._stickyBombsDirectHitsAvgPer10Min = js["stickyBombsDirectHitsAvgPer10Min"]
            except KeyError:
                self._stickyBombsDirectHitsAvgPer10Min = 0
            try:
                self._stickyBombsDirectHitsMostInGame = js["stickyBombsDirectHitsMostInGame"]
            except KeyError:
                self._stickyBombsDirectHitsMostInGame = 0
            try:
                self._stickyBombsKills = js["stickyBombsKills"]
            except KeyError:
                self._stickyBombsKills = 0
            try:
                self._stickyBombsKillsAvgPer10Min = js["stickyBombsKillsAvgPer10Min"]
            except KeyError:
                self._stickyBombsKillsAvgPer10Min = 0
            try:
                self._stickyBombsKillsMostInGame = js["stickyBombsKillsMostInGame"]
            except KeyError:
                self._stickyBombsKillsMostInGame = 0
        elif hero == "genji":
            try:
                self._damageReflected = js["damageReflected"]
            except KeyError:
                self._damageReflected = 0
            try:
                self._damageReflectedAvgPer10Min = js["damageReflectedAvgPer10Min"]
            except KeyError:
                self._damageReflectedAvgPer10Min = 0
            try:
                self._damageReflectedMostInGame = js["damageReflectedMostInGame"]
            except KeyError:
                self._damageReflectedMostInGame = 0
            try:
                self._dragonbladesKills = js["dragonbladesKills"]
            except KeyError:
                self._dragonbladesKills = 0
            try:
                self._dragonbladesKillsAvgPer10Min = js["dragonbladesKillsAvgPer10Min"]
            except KeyError:
                self._dragonbladesKillsAvgPer10Min = 0
            try:
                self._dragonbladesKillsMostInGame = js["dragonbladesKillsMostInGame"]
            except KeyError:
                self._dragonbladesKillsMostInGame = 0
        elif hero == "hanzo":
            try:
                self._dragonstrikeKills = js["dragonstrikeKills"]
            except KeyError:
                self._dragonstrikeKills = 0
            try:
                self._dragonstrikeKillsAvgPer10Min = js["dragonstrikeKillsAvgPer10Min"]
            except KeyError:
                self._dragonstrikeKillsAvgPer10Min = 0
            try:
                self._dragonstrikeKillsMostInGame = js["dragonstrikeKillsMostInGame"]
            except KeyError:
                self._dragonstrikeKillsMostInGame = 0
            try:
                self._scatterArrowKills = js["scatterArrowKills"]
            except KeyError:
                self._scatterArrowKills = 0
            try:
                self._scatterArrowKillsAvgPer10Min = js["scatterArrowKillsAvgPer10Min"]
            except KeyError:
                self._scatterArrowKillsAvgPer10Min = 0
            try:
                self._scatterArrowKillsMostInGame = js["scatterArrowKillsMostInGame"]
            except KeyError:
                self._scatterArrowKillsMostInGame = 0
            try:
                self._stormArrowKills = js["stormArrowKills"]
            except KeyError:
                self._stormArrowKills = 0
            try:
                self._stormArrowKillsAvgPer10Min = js["stormArrowKillsAvgPer10Min"]
            except KeyError:
                self._stormArrowKillsAvgPer10Min = 0
            try:
                self._stormArrowKillsMostInGame = js["stormArrowKillsMostInGame"]
            except KeyError:
                self._stormArrowKillsMostInGame = 0
        elif hero == "junkrat":
            try:
                self._concussionMineKills = js["concussionMineKills"]
            except KeyError:
                self._concussionMineKills = 0
            try:
                self._concussionMineKillsAvgPer10Min = js["concussionMineKillsAvgPer10Min"]
            except KeyError:
                self._concussionMineKillsAvgPer10Min = 0
            try:
                self._concussionMineKillsMostInGame = js["concussionMineKillsMostInGame"]
            except KeyError:
                self._concussionMineKillsMostInGame = 0
            try:
                self._enemiesTrapped = js["enemiesTrapped"]
            except KeyError:
                self._enemiesTrapped = 0
            try:
                self._enemiesTrappedAvgPer10Min = js["enemiesTrappedAvgPer10Min"]
            except KeyError:
                self._enemiesTrappedAvgPer10Min = 0
            try:
                self._enemiesTrappedMostInGame = js["enemiesTrappedMostInGame"]
            except KeyError:
                self._enemiesTrappedMostInGame = 0
            try:
                self._ripTireKills = js["ripTireKills"]
            except KeyError:
                self._ripTireKills = 0
            try:
                self._ripTireKillsAvgPer10Min = js["ripTireKillsAvgPer10Min"]
            except KeyError:
                self._ripTireKillsAvgPer10Min = 0
            try:
                self._ripTireKillsMostInGame = js["ripTireKillsMostInGame"]
            except KeyError:
                self._ripTireKillsMostInGame = 0
        elif hero == "lucio":
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
            try:
                self._soundBarriersProvided = js["soundBarriersProvided"]
            except KeyError:
                self._soundBarriersProvided = 0
            try:
                self._soundBarriersProvidedAvgPer10Min = js["soundBarriersProvidedAvgPer10Min"]
            except KeyError:
                self._soundBarriersProvidedAvgPer10Min = 0
            try:
                self._soundBarriersProvidedMostInGame = js["soundBarriersProvidedMostInGame"]
            except KeyError:
                self._soundBarriersProvidedMostInGame = 0
        elif hero == "mccree":
            try:
                self._deadeyeKills = js["deadeyeKills"]
            except KeyError:
                self._deadeyeKills = 0
            try:
                self._deadeyeKillsAvgPer10Min = js["deadeyeKillsAvgPer10Min"]
            except KeyError:
                self._deadeyeKillsAvgPer10Min = 0
            try:
                self._deadeyeKillsMostInGame = js["deadeyeKillsMostInGame"]
            except KeyError:
                self._deadeyeKillsMostInGame = 0
            try:
                self._fanTheHammerKills = js["fanTheHammerKills"]
            except KeyError:
                self._fanTheHammerKills = 0
            try:
                self._fanTheHammerKillsAvgPer10Min = js["fanTheHammerKillsAvgPer10Min"]
            except KeyError:
                self._fanTheHammerKillsAvgPer10Min = 0
            try:
                self._fanTheHammerKillsMostInGame = js["fanTheHammerKillsMostInGame"]
            except KeyError:
                self._fanTheHammerKillsMostInGame = 0
        elif hero == "mei":
            try:
                self._blizzardKills = js["blizzardKills"]
            except KeyError:
                self._blizzardKills = 0
            try:
                self._blizzardKillsAvgPer10Min = js["blizzardKillsAvgPer10Min"]
            except KeyError:
                self._blizzardKillsAvgPer10Min = 0
            try:
                self._blizzardKillsMostInGame = js["blizzardKillsMostInGame"]
            except KeyError:
                self._blizzardKillsMostInGame = 0
            try:
                self._damageBlocked = js["damageBlocked"]
            except KeyError:
                self._damageBlocked = 0
            try:
                self._damageBlockedAvgPer10Min = js["damageBlockedAvgPer10Min"]
            except KeyError:
                self._damageBlockedAvgPer10Min = 0
            try:
                self._damageBlockedMostInGame = js["damageBlockedMostInGame"]
            except KeyError:
                self._damageBlockedMostInGame = 0
            try:
                self._enemiesFrozen = js["enemiesFrozen"]
            except KeyError:
                self._enemiesFrozen = 0
            try:
                self._enemiesFrozenAvgPer10Min = js["enemiesFrozenAvgPer10Min"]
            except KeyError:
                self._enemiesFrozenAvgPer10Min = 0
            try:
                self._enemiesFrozenMostInGame = js["enemiesFrozenMostInGame"]
            except KeyError:
                self._enemiesFrozenMostInGame = 0
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
        elif hero == "mercy":
            try:
                self._blasterKills = js["blasterKills"]
            except KeyError:
                self._blasterKills = 0
            try:
                self._blasterKillsAvgPer10Min = js["blasterKillsAvgPer10Min"]
            except KeyError:
                self._blasterKillsAvgPer10Min = 0
            try:
                self._blasterKillsMostInGame = js["blasterKillsMostInGame"]
            except KeyError:
                self._blasterKillsMostInGame = 0
            try:
                self._damageAmplified = js["damageAmplified"]
            except KeyError:
                self._damageAmplified = 0
            try:
                self._damageAmplifiedAvgPer10Min = js["damageAmplifiedAvgPer10Min"]
            except KeyError:
                self._damageAmplifiedAvgPer10Min = 0
            try:
                self._damageAmplifiedMostInGame = js["damageAmplifiedMostInGame"]
            except KeyError:
                self._damageAmplifiedMostInGame = 0
            try:
                self._playersResurrected = js["playersResurrected"]
            except KeyError:
                self._playersResurrected = 0
            try:
                self._playersResurrectedAvgPer10Min = js["playersResurrectedAvgPer10Min"]
            except KeyError:
                self._playersResurrectedAvgPer10Min = 0
            try:
                self._playersResurrectedMostInGame = js["playersResurrectedMostInGame"]
            except KeyError:
                self._playersResurrectedMostInGame = 0
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
        elif hero == "moira":
            try:
                self._coalescenceHealing = js["coalescenceHealing"]
            except KeyError:
                self._coalescenceHealing = 0
            try:
                self._coalescenceHealingAvgPer10Min = js["coalescenceHealingAvgPer10Min"]
            except KeyError:
                self._coalescenceHealingAvgPer10Min = 0
            try:
                self._coalescenceHealingMostInGame = js["coalescenceHealingMostInGame"]
            except KeyError:
                self._coalescenceHealingMostInGame = 0
            try:
                self._coalescenceKills = js["coalescenceKills"]
            except KeyError:
                self._coalescenceKills = 0
            try:
                self._coalescenceKillsAvgPer10Min = js["coalescenceKillsAvgPer10Min"]
            except KeyError:
                self._coalescenceKillsAvgPer10Min = 0
            try:
                self._coalescenceKillsMostInGame = js["coalescenceKillsMostInGame"]
            except KeyError:
                self._coalescenceKillsMostInGame = 0
            try:
                self._secondaryFireAccuracy = js["secondaryFireAccuracy"]
            except KeyError:
                self._secondaryFireAccuracy = 0
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
        elif hero == "orisa":
            try:
                self._damageAmplified = js["damageAmplified"]
            except KeyError:
                self._damageAmplified = 0
            try:
                self._damageAmplifiedAvgPer10Min = js["damageAmplifiedAvgPer10Min"]
            except KeyError:
                self._damageAmplifiedAvgPer10Min = 0
            try:
                self._damageAmplifiedMostInGame = js["damageAmplifiedMostInGame"]
            except KeyError:
                self._damageAmplifiedMostInGame = 0
            try:
                self._damageBlocked = js["damageBlocked"]
            except KeyError:
                self._damageBlocked = 0
            try:
                self._damageBlockedAvgPer10Min = js["damageBlockedAvgPer10Min"]
            except KeyError:
                self._damageBlockedAvgPer10Min = 0
            try:
                self._damageBlockedMostInGame = js["damageBlockedMostInGame"]
            except KeyError:
                self._damageBlockedMostInGame = 0
            try:
                self._superchargerAssists = js["superchargerAssists"]
            except KeyError:
                self._superchargerAssists = 0
            try:
                self._superchargerAssistsAvgPer10Min = js["superchargerAssistsAvgPer10Min"]
            except KeyError:
                self._superchargerAssistsAvgPer10Min = 0
            try:
                self._superchargerAssistsMostInGame = js["superchargerAssistsMostInGame"]
            except KeyError:
                self._superchargerAssistsMostInGame = 0
        elif hero == "pharah":
            try:
                self._barrageKills = js["barrageKills"]
            except KeyError:
                self._barrageKills = 0
            try:
                self._barrageKillsAvgPer10Min = js["barrageKillsAvgPer10Min"]
            except KeyError:
                self._barrageKillsAvgPer10Min = 0
            try:
                self._barrageKillsMostInGame = js["barrageKillsMostInGame"]
            except KeyError:
                self._barrageKillsMostInGame = 0
            try:
                self._directHitsAccuracy = js["directHitsAccuracy"]
            except KeyError:
                self._directHitsAccuracy = 0
            try:
                self._rocketDirectHits = js["rocketDirectHits"]
            except KeyError:
                self._rocketDirectHits = 0
            try:
                self._rocketDirectHitsAvgPer10Min = js["rocketDirectHitsAvgPer10Min"]
            except KeyError:
                self._rocketDirectHitsAvgPer10Min = 0
            try:
                self._rocketDirectHitsMostInGame = js["rocketDirectHitsMostInGame"]
            except KeyError:
                self._rocketDirectHitsMostInGame = 0
        elif hero == "reaper":
            try:
                self._deathsBlossomKills = js["deathsBlossomKills"]
            except KeyError:
                self._deathsBlossomKills = 0
            try:
                self._deathsBlossomKillsAvgPer10Min = js["deathsBlossomKillsAvgPer10Min"]
            except KeyError:
                self._deathsBlossomKillsAvgPer10Min = 0
            try:
                self._deathsBlossomKillsMostInGame = js["deathsBlossomKillsMostInGame"]
            except KeyError:
                self._deathsBlossomKillsMostInGame = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
        elif hero == "reinhardt":
            try:
                self._chargeKills = js["chargeKills"]
            except KeyError:
                self._chargeKills = 0
            try:
                self._chargeKillsAvgPer10Min = js["chargeKillsAvgPer10Min"]
            except KeyError:
                self._chargeKillsAvgPer10Min = 0
            try:
                self._chargeKillsMostInGame = js["chargeKillsMostInGame"]
            except KeyError:
                self._chargeKillsMostInGame = 0
            try:
                self._damageBlocked = js["damageBlocked"]
            except KeyError:
                self._damageBlocked = 0
            try:
                self._damageBlockedAvgPer10Min = js["damageBlockedAvgPer10Min"]
            except KeyError:
                self._damageBlockedAvgPer10Min = 0
            try:
                self._damageBlockedMostInGame = js["damageBlockedMostInGame"]
            except KeyError:
                self._damageBlockedMostInGame = 0
            try:
                self._earthshatterKills = js["earthshatterKills"]
            except KeyError:
                self._earthshatterKills = 0
            try:
                self._earthshatterKillsAvgPer10Min = js["earthshatterKillsAvgPer10Min"]
            except KeyError:
                self._earthshatterKillsAvgPer10Min = 0
            try:
                self._earthshatterKillsMostInGame = js["earthshatterKillsMostInGame"]
            except KeyError:
                self._earthshatterKillsMostInGame = 0
            try:
                self._fireStrikeKills = js["fireStrikeKills"]
            except KeyError:
                self._fireStrikeKills = 0
            try:
                self._fireStrikeKillsAvgPer10Min = js["fireStrikeKillsAvgPer10Min"]
            except KeyError:
                self._fireStrikeKillsAvgPer10Min = 0
            try:
                self._fireStrikeKillsMostInGame = js["fireStrikeKillsMostInGame"]
            except KeyError:
                self._fireStrikeKillsMostInGame = 0
            try:
                self._rocketHammerMeleeAccuracy = js["rocketHammerMeleeAccuracy"]
            except KeyError:
                self._rocketHammerMeleeAccuracy = 0
        elif hero == "roadhog":
            try:
                self._enemiesHooked = js["enemiesHooked"]
            except KeyError:
                self._enemiesHooked = 0
            try:
                self._enemiesHookedAvgPer10Min = js["enemiesHookedAvgPer10Min"]
            except KeyError:
                self._enemiesHookedAvgPer10Min = 0
            try:
                self._enemiesHookedMostInGame = js["enemiesHookedMostInGame"]
            except KeyError:
                self._enemiesHookedMostInGame = 0
            try:
                self._hookAccuracy = js["hookAccuracy"]
            except KeyError:
                self._hookAccuracy = 0
            try:
                self._hookAccuracyBestInGame = js["hookAccuracyBestInGame"]
            except KeyError:
                self._hookAccuracyBestInGame = 0
            try:
                self._hooksAttempted = js["hooksAttempted"]
            except KeyError:
                self._hooksAttempted = 0
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
            try:
                self._wholeHogKills = js["wholeHogKills"]
            except KeyError:
                self._wholeHogKills = 0
            try:
                self._wholeHogKillsAvgPer10Min = js["wholeHogKillsAvgPer10Min"]
            except KeyError:
                self._wholeHogKillsAvgPer10Min = 0
            try:
                self._wholeHogKillsMostInGame = js["wholeHogKillsMostInGame"]
            except KeyError:
                self._wholeHogKillsMostInGame = 0
        elif hero == "sigma":
            try:
                self._accretionKills = js["accretionKills"]
            except KeyError:
                self._accretionKills = 0
            try:
                self._accretionKillsAvgPer10Min = js["accretionKillsAvgPer10Min"]
            except KeyError:
                self._accretionKillsAvgPer10Min = 0
            try:
                self._accretionKillsMostInGame = js["accretionKillsMostInGame"]
            except KeyError:
                self._accretionKillsMostInGame = 0
            try:
                self._damageAbsorbed = js["damageAbsorbed"]
            except KeyError:
                self._damageAbsorbed = 0
            try:
                self._damageAbsorbedAvgPer10Min = js["damageAbsorbedAvgPer10Min"]
            except KeyError:
                self._damageAbsorbedAvgPer10Min = 0
            try:
                self._damageAbsorbedMostInGame = js["damageAbsorbedMostInGame"]
            except KeyError:
                self._damageAbsorbedMostInGame = 0
            try:
                self._damageBlocked = js["damageBlocked"]
            except KeyError:
                self._damageBlocked = 0
            try:
                self._damageBlockedAvgPer10Min = js["damageBlockedAvgPer10Min"]
            except KeyError:
                self._damageBlockedAvgPer10Min = 0
            try:
                self._damageBlockedMostInGame = js["damageBlockedMostInGame"]
            except KeyError:
                self._damageBlockedMostInGame = 0
            try:
                self._graviticFluxKills = js["graviticFluxKills"]
            except KeyError:
                self._graviticFluxKills = 0
            try:
                self._graviticFluxKillsAvgPer10Min = js["graviticFluxKillsAvgPer10Min"]
            except KeyError:
                self._graviticFluxKillsAvgPer10Min = 0
            try:
                self._graviticFluxKillsMostInGame = js["graviticFluxKillsMostInGame"]
            except KeyError:
                self._graviticFluxKillsMostInGame = 0
        elif hero == "soldier76":
            try:
                self._bioticFieldHealingDone = js["bioticFieldHealingDone"]
            except KeyError:
                self._bioticFieldHealingDone = 0
            try:
                self._bioticFieldsDeployed = js["bioticFieldsDeployed"]
            except KeyError:
                self._bioticFieldsDeployed = 0
            try:
                self._helixRocketKills = js["helixRocketKills"]
            except KeyError:
                self._helixRocketKills = 0
            try:
                self._helixRocketKillsAvgPer10Min = js["helixRocketKillsAvgPer10Min"]
            except KeyError:
                self._helixRocketKillsAvgPer10Min = 0
            try:
                self._helixRocketKillsMostInGame = js["helixRocketKillsMostInGame"]
            except KeyError:
                self._helixRocketKillsMostInGame = 0
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
            try:
                self._tacticalVisorKills = js["tacticalVisorKills"]
            except KeyError:
                self._tacticalVisorKills = 0
            try:
                self._tacticalVisorKillsAvgPer10Min = js["tacticalVisorKillsAvgPer10Min"]
            except KeyError:
                self._tacticalVisorKillsAvgPer10Min = 0
            try:
                self._tacticalVisorKillsMostInGame = js["tacticalVisorKillsMostInGame"]
            except KeyError:
                self._tacticalVisorKillsMostInGame = 0
        elif hero == "sombra":
            try:
                self._enemiesEmpd = js["enemiesEmpd"]
            except KeyError:
                self._enemiesEmpd = 0
            try:
                self._enemiesEmpdAvgPer10Min = js["enemiesEmpdAvgPer10Min"]
            except KeyError:
                self._enemiesEmpdAvgPer10Min = 0
            try:
                self._enemiesEmpdMostInGame = js["enemiesEmpdMostInGame"]
            except KeyError:
                self._enemiesEmpdMostInGame = 0
            try:
                self._enemiesHacked = js["enemiesHacked"]
            except KeyError:
                self._enemiesHacked = 0
            try:
                self._enemiesHackedAvgPer10Min = js["enemiesHackedAvgPer10Min"]
            except KeyError:
                self._enemiesHackedAvgPer10Min = 0
            try:
                self._enemiesHackedMostInGame = js["enemiesHackedMostInGame"]
            except KeyError:
                self._enemiesHackedMostInGame = 0
        elif hero == "symmetra":
            try:
                self._damageBlocked = js["damageBlocked"]
            except KeyError:
                self._damageBlocked = 0
            try:
                self._damageBlockedAvgPer10Min = js["damageBlockedAvgPer10Min"]
            except KeyError:
                self._damageBlockedAvgPer10Min = 0
            try:
                self._damageBlockedMostInGame = js["damageBlockedMostInGame"]
            except KeyError:
                self._damageBlockedMostInGame = 0
            try:
                self._playersTeleported = js["playersTeleported"]
            except KeyError:
                self._playersTeleported = 0
            try:
                self._playersTeleportedAvgPer10Min = js["playersTeleportedAvgPer10Min"]
            except KeyError:
                self._playersTeleportedAvgPer10Min = 0
            try:
                self._playersTeleportedMostInGame = js["playersTeleportedMostInGame"]
            except KeyError:
                self._playersTeleportedMostInGame = 0
            try:
                self._primaryFireAccuracy = js["primaryFireAccuracy"]
            except KeyError:
                self._primaryFireAccuracy = 0
            try:
                self._secondaryDirectHitsAvgPer10Min = js["secondaryDirectHitsAvgPer10Min"]
            except KeyError:
                self._secondaryDirectHitsAvgPer10Min = 0
            try:
                self._sentryTurretsKills = js["sentryTurretsKills"]
            except KeyError:
                self._sentryTurretsKills = 0
            try:
                self._sentryTurretsKillsAvgPer10Min = js["sentryTurretsKillsAvgPer10Min"]
            except KeyError:
                self._sentryTurretsKillsAvgPer10Min = 0
            try:
                self._sentryTurretsKillsMostInGame = js["sentryTurretsKillsMostInGame"]
            except KeyError:
                self._sentryTurretsKillsMostInGame = 0
        elif hero == "torbjorn":
            try:
                self._armorPacksCreated = js["armorPacksCreated"]
            except KeyError:
                self._armorPacksCreated = 0
            try:
                self._armorPacksCreatedAvgPer10Min = js["armorPacksCreatedAvgPer10Min"]
            except KeyError:
                self._armorPacksCreatedAvgPer10Min = 0
            try:
                self._armorPacksCreatedMostInGame = js["armorPacksCreatedMostInGame"]
            except KeyError:
                self._armorPacksCreatedMostInGame = 0
            try:
                self._moltenCoreKills = js["moltenCoreKills"]
            except KeyError:
                self._moltenCoreKills = 0
            try:
                self._moltenCoreKillsAvgPer10Min = js["moltenCoreKillsAvgPer10Min"]
            except KeyError:
                self._moltenCoreKillsAvgPer10Min = 0
            try:
                self._moltenCoreKillsMostInGame = js["moltenCoreKillsMostInGame"]
            except KeyError:
                self._moltenCoreKillsMostInGame = 0
            try:
                self._torbjornKills = js["torbjornKills"]
            except KeyError:
                self._torbjornKills = 0
            try:
                self._torbjornKillsAvgPer10Min = js["torbjornKillsAvgPer10Min"]
            except KeyError:
                self._torbjornKillsAvgPer10Min = 0
            try:
                self._torbjornKillsMostInGame = js["torbjornKillsMostInGame"]
            except KeyError:
                self._torbjornKillsMostInGame = 0
            try:
                self._turretsDamageAvgPer10Min = js["turretsDamageAvgPer10Min"]
            except KeyError:
                self._turretsDamageAvgPer10Min = 0
            try:
                self._turretsKills = js["turretsKills"]
            except KeyError:
                self._turretsKills = 0
            try:
                self._turretsKillsAvgPer10Min = js["turretsKillsAvgPer10Min"]
            except KeyError:
                self._turretsKillsAvgPer10Min = 0
            try:
                self._turretsKillsMostInGame = js["turretsKillsMostInGame"]
            except KeyError:
                self._turretsKillsMostInGame = 0
        elif hero == "tracer":
            try:
                self._healthRecovered = js["healthRecovered"]
            except KeyError:
                self._healthRecovered = 0
            try:
                self._healthRecoveredAvgPer10Min = js["healthRecoveredAvgPer10Min"]
            except KeyError:
                self._healthRecoveredAvgPer10Min = 0
            try:
                self._healthRecoveredMostInGame = js["healthRecoveredMostInGame"]
            except KeyError:
                self._healthRecoveredMostInGame = 0
            try:
                self._pulseBombsAttached = js["pulseBombsAttached"]
            except KeyError:
                self._pulseBombsAttached = 0
            try:
                self._pulseBombsAttachedAvgPer10Min = js["pulseBombsAttachedAvgPer10Min"]
            except KeyError:
                self._pulseBombsAttachedAvgPer10Min = 0
            try:
                self._pulseBombsAttachedMostInGame = js["pulseBombsAttachedMostInGame"]
            except KeyError:
                self._pulseBombsAttachedMostInGame = 0
            try:
                self._pulseBombsKills = js["pulseBombsKills"]
            except KeyError:
                self._pulseBombsKills = 0
            try:
                self._pulseBombsKillsAvgPer10Min = js["pulseBombsKillsAvgPer10Min"]
            except KeyError:
                self._pulseBombsKillsAvgPer10Min = 0
            try:
                self._pulseBombsKillsMostInGame = js["pulseBombsKillsMostInGame"]
            except KeyError:
                self._pulseBombsKillsMostInGame = 0
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
        elif hero == "widowmaker":
            try:
                self._scopedAccuracy = js["scopedAccuracy"]
            except KeyError:
                self._scopedAccuracy = 0
            try:
                self._scopedAccuracyBestInGame = js["scopedAccuracyBestInGame"]
            except KeyError:
                self._scopedAccuracyBestInGame = 0
            try:
                self._scopedCriticalHits = js["scopedCriticalHits"]
            except KeyError:
                self._scopedCriticalHits = 0
            try:
                self._scopedCriticalHitsAccuracy = js["scopedCriticalHitsAccuracy"]
            except KeyError:
                self._scopedCriticalHitsAccuracy = 0
            try:
                self._scopedCriticalHitsAvgPer10Min = js["scopedCriticalHitsAvgPer10Min"]
            except KeyError:
                self._scopedCriticalHitsAvgPer10Min = 0
            try:
                self._scopedCriticalHitsKills = js["scopedCriticalHitsKills"]
            except KeyError:
                self._scopedCriticalHitsKills = 0
            try:
                self._scopedCriticalHitsKillsAvgPer10Min = js["scopedCriticalHitsKillsAvgPer10Min"]
            except KeyError:
                self._scopedCriticalHitsKillsAvgPer10Min = 0
            try:
                self._scopedCriticalHitsMostInGame = js["scopedCriticalHitsMostInGame"]
            except KeyError:
                self._scopedCriticalHitsMostInGame = 0
            try:
                self._venomMineKills = js["venomMineKills"]
            except KeyError:
                self._venomMineKills = 0
            try:
                self._venomMineKillsAvgPer10Mi = js["venomMineKillsAvgPer10Min"]
            except KeyError:
                self._venomMineKillsAvgPer10Mi = 0
            try:
                self._venomMineKillsMostInGame = js["venomMineKillsMostInGame"]
            except KeyError:
                self._venomMineKillsMostInGame = 0
        elif hero == "winston":
            try:
                self._damageBlocked = js["damageBlocked"]
            except KeyError:
                self._damageBlocked = 0
            try:
                self._damageBlockedAvgPer10Min = js["damageBlockedAvgPer10Min"]
            except KeyError:
                self._damageBlockedAvgPer10Min = 0
            try:
                self._damageBlockedMostInGame = js['damageBlockedMostInGame']
            except KeyError:
                self._damageBlockedMostInGame = 0
            try:
                self._playersKnockedBack = js["playersKnockedBack"]
            except KeyError:
                self._playersKnockedBack = 0
            try:
                self._playersKnockedBackAvgPer10Min = js["playersKnockedBackAvgPer10Min"]
            except KeyError:
                self._playersKnockedBackAvgPer10Min = 0
            try:
                self._playersKnockedBackMostInGame = js["playersKnockedBackMostInGame"]
            except KeyError:
                self._playersKnockedBackMostInGame = 0
            try:
                self._primalRageMeleeAccuracy = js["primalRageMeleeAccuracy"]
            except KeyError:
                self._primalRageMeleeAccuracy = 0
            try:
                self._teslaCannonAccuracy = js["teslaCannonAccuracy"]
            except KeyError:
                self._teslaCannonAccuracy = 0
            try:
                self._weaponKills = js["weaponKills"]
            except KeyError:
                self._weaponKills = 0
        elif hero == "wreckingBall":
            try:
                self._grapplingClawKills = js["grapplingClawKills"]
            except KeyError:
                self._grapplingClawKills = 0
            try:
                self._grapplingClawKillsAvgPer10Min = js["grapplingClawKillsAvgPer10Min"]
            except KeyError:
                self._grapplingClawKillsAvgPer10Min = 0
            try:
                self._grapplingClawKillsMostInGame = js["grapplingClawKillsMostInGame"]
            except KeyError:
                self._grapplingClawKillsMostInGame = 0
            try:
                self._minefieldKills = js["minefieldKills"]
            except KeyError:
                self._minefieldKills = 0
            try:
                self._minefieldKillsAvgPer10Min = js["minefieldKillsAvgPer10Min"]
            except KeyError:
                self._minefieldKillsAvgPer10Min = 0
            try:
                self._minefieldKillsMostInGame = js["minefieldKillsMostInGame"]
            except KeyError:
                self._minefieldKillsMostInGame = 0
            try:
                self._piledriverKills = js["piledriverKills"]
            except KeyError:
                self._piledriverKills = 0
            try:
                self._piledriverKillsAvgPer10Min = js["piledriverKillsAvgPer10Min"]
            except KeyError:
                self._piledriverKillsAvgPer10Min = 0
            try:
                self._piledriverKillsMostInGame = js["piledriverKillsMostInGame"]
            except KeyError:
                self._piledriverKillsMostInGame = 0
            try:
                self._playersKnockedBack = js["playersKnockedBack"]
            except KeyError:
                self._playersKnockedBack = 0
            try:
                self._playersKnockedBackAvgPer10Min = js["playersKnockedBackAvgPer10Min"]
            except KeyError:
                self._playersKnockedBackAvgPer10Min = 0
            try:
                self._playersKnockedBackMostInGame = js["playersKnockedBackMostInGame"]
            except KeyError:
                self._playersKnockedBackMostInGame = 0
        elif hero == "zarya":
            try:
                self._averageEnergy = js["averageEnergy"]
            except KeyError:
                self._averageEnergy = 0
            try:
                self._averageEnergyBestInGame = js["averageEnergyBestInGame"]
            except KeyError:
                self._averageEnergyBestInGame = 0
            try:
                self._damageBlocked = js["damageBlocked"]
            except KeyError:
                self._damageBlocked = 0
            try:
                self._damageBlockedAvgPer10Min = js["damageBlockedAvgPer10Min"]
            except KeyError:
                self._damageBlockedAvgPer10Min = 0
            try:
                self._damageBlockedMostInGame = js["damageBlockedMostInGame"]
            except KeyError:
                self._damageBlockedMostInGame = 0
            try:
                self._gravitonSurgeKills = js["gravitonSurgeKills"]
            except KeyError:
                self._gravitonSurgeKills = 0
            try:
                self._gravitonSurgeKillsAvgPer10Min = js["gravitonSurgeKillsAvgPer10Min"]
            except KeyError:
                self._gravitonSurgeKillsAvgPer10Min = 0
            try:
                self._gravitonSurgeKillsMostInGame = js["gravitonSurgeKillsMostInGame"]
            except KeyError:
                self._gravitonSurgeKillsMostInGame = 0
            try:
                self._highEnergyKills = js["highEnergyKills"]
            except KeyError:
                self._highEnergyKills = 0
            try:
                self._highEnergyKillsAvgPer10Min = js["highEnergyKillsAvgPer10Min"]
            except KeyError:
                self._highEnergyKillsAvgPer10Min = 0
            try:
                self._highEnergyKillsMostInGame = js["highEnergyKillsMostInGame"]
            except KeyError:
                self._highEnergyKillsMostInGame = 0
            try:
                self._primaryFireAccuracy = js["primaryFireAccuracy"]
            except KeyError:
                self._primaryFireAccuracy = 0
            try:
                self._projectedBarriersApplied = js["projectedBarriersApplied"]
            except KeyError:
                self._projectedBarriersApplied = 0
            try:
                self._projectedBarriersAppliedAvgPer10Min = js["projectedBarriersAppliedAvgPer10Min"]
            except KeyError:
                self._projectedBarriersAppliedAvgPer10Min = 0
            try:
                self._projectedBarriersAppliedMostInGame = js["projectedBarriersAppliedMostInGame"]
            except KeyError:
                self._projectedBarriersAppliedMostInGame = 0
        elif hero == "zenyatta":
            try:
                self._selfHealing = js["selfHealing"]
            except KeyError:
                self._selfHealing = 0
            try:
                self._selfHealingAvgPer10Min = js["selfHealingAvgPer10Min"]
            except KeyError:
                self._selfHealingAvgPer10Min = 0
            try:
                self._selfHealingMostInGame = js["selfHealingMostInGame"]
            except KeyError:
                self._selfHealingMostInGame = 0
            try:
                self._transcendenceHealing = js["transcendenceHealing"]
            except KeyError:
                self._transcendenceHealing = 0
            try:
                self._transcendenceHealingBest = js["transcendenceHealingBest"]
            except KeyError:
                self._transcendenceHealingBest = 0

    @property
    def bioticGrenadeKills(self):
        return self._bioticGrenadeKills

    @property
    def enemiesSlept(self):
        return self._enemiesSlept

    @property
    def enemiesSleptAvgPer10Min(self):
        return self._enemiesSleptAvgPer10Min

    @property
    def enemiesSleptMostInGame(self):
        return self._enemiesSleptMostInGame

    @property
    def healingAmplified(self):
        return self._healingAmplified

    @property
    def healingAmplifiedAvgPer10Min(self):
        return self._healingAmplifiedAvgPer10Min

    @property
    def healingAmplifiedMostInGame(self):
        return self._healingAmplifiedMostInGame

    @property
    def nanoBoostAssists(self):
        return self._nanoBoostAssists

    @property
    def nanoBoostAssistsAvgPer10Min(self):
        return self._nanoBoostAssistsAvgPer10Min

    @property
    def nanoBoostAssistsMostInGame(self):
        return self._nanoBoostAssistsMostInGame

    @property
    def nanoBoostsApplied(self):
        return self._nanoBoostsApplied

    @property
    def nanoBoostsAppliedAvgPer10Min(self):
        return self._nanoBoostsAppliedAvgPer10Min

    @property
    def nanoBoostsAppliedMostInGame(self):
        return self._nanoBoostsAppliedMostInGame

    @property
    def scopedAccuracy(self):
        return self._scopedAccuracy

    @property
    def scopedAccuracyBestInGame(self):
        return self._scopedAccuracyBestInGame

    @property
    def selfHealing(self):
        return self._selfHealing

    @property
    def selfHealingAvgPer10Min(self):
        return self._selfHealingAvgPer10Min

    @property
    def selfHealingMostInGame(self):
        return self._selfHealingMostInGame

    @property
    def unscopedAccuracy(self):
        return self._unscopedAccuracy

    @property
    def unscopedAccuracyBestInGame(self):
        return self._unscopedAccuracyBestInGame

    @property
    def dynamiteKills(self):
        return self._dynamiteKills

    @property
    def dynamiteKillsAvgPer10Min(self):
        return self._dynamiteKillsAvgPer10Min

    @property
    def dynamiteKillsMostInGame(self):
        return self._dynamiteKillsMostInGame

    @property
    def scopedCriticalHits(self):
        return self._scopedCriticalHits

    @property
    def scopedCriticalHitsAccuracy(self):
        return self._scopedCriticalHitsAccuracy

    @property
    def scopedCriticalHitsAvgPer10Min(self):
        return self._scopedCriticalHitsAvgPer10Min

    @property
    def scopedCriticalHitsMostInGame(self):
        return self._scopedCriticalHitsMostInGame

    @property
    def amplificationMatrixAssists(self):
        return self._amplificationMatrixAssists

    @property
    def amplificationMatrixAssistsAvgPer10Min(self):
        return self._amplificationMatrixAssistsAvgPer10Min

    @property
    def amplificationMatrixAssistsBestInGame(self):
        return self._amplificationMatrixAssistsBestInGame

    @property
    def amplificationMatrixCastsMostInGame(self):
        return self._amplificationMatrixCastsMostInGame

    @property
    def damageAmplified(self):
        return self._damageAmplified

    @property
    def damageAmplifiedAvgPer10Min(self):
        return self._damageAmplifiedAvgPer10Min

    @property
    def damageAmplifiedMostInGame(self):
        return self._damageAmplifiedMostInGame

    @property
    def healingAccuracy(self):
        return self._healingAccuracy

    @property
    def healingAccuracyBestInGame(self):
        return self._healingAccuracyBestInGame

    @property
    def immortalityFieldDeathsPrevented(self):
        return self._immortalityFieldDeathsPrevented

    @property
    def immortalityFieldDeathsPreventedAvgPer10Min(self):
        return self._immortalityFieldDeathsPreventedAvgPer10Min

    @property
    def immortalityFieldDeathsPreventedMostInGame(self):
        return self._immortalityFieldDeathsPreventedMostInGame

    @property
    def reconKills(self):
        return self._reconKills

    @property
    def reconKillsAvgPer10Min(self):
        return self._reconKillsAvgPer10Min

    @property
    def reconKillsMostInGame(self):
        return self._reconKillsMostInGame

    @property
    def sentryKills(self):
        return self._sentryKills

    @property
    def sentryKillsAvgPer10Min(self):
        return self._sentryKillsAvgPer10Min

    @property
    @property
    def sentryKillsMostInGame(self):
        return self._sentryKillsMostInGame

    @property
    def tankKills(self):
        return self._tankKills

    @property
    def tankKillsAvgPer10Min(self):
        return self._tankKillsAvgPer10Min

    @property
    def tankKillsMostInGame(self):
        return self._tankKillsMostInGame

    @property
    def armorProvided(self):
        return self._armorProvided

    @property
    def armorProvidedAvgPer10Min(self):
        return self._armorProvidedAvgPer10Min

    @property
    def armorProvidedMostInGame(self):
        return self._armorProvidedMostInGame

    @property
    def damageBlocked(self):
        return self._damageBlocked

    @property
    def damageBlockedAvgPer10Min(self):
        return self._damageBlockedAvgPer10Min

    @property
    def damageBlockedMostInGame(self):
        return self._damageBlockedMostInGame

    @property
    def inspireUptimePercentage(self):
        return self._inspireUptimePercentage

    @property
    def mechDeaths(self):
        return self._mechDeaths

    @property
    def mechsCalled(self):
        return self._mechsCalled

    @property
    def mechsCalledAvgPer10Min(self):
        return self._mechsCalledAvgPer10Min

    @property
    def mechsCalledMostInGame(self):
        return self._mechsCalledMostInGame

    @property
    def selfDestructKills(self):
        return self._selfDestructKills

    @property
    def selfDestructKillsAvgPer10Min(self):
        return self._selfDestructKillsAvgPer10Min

    @property
    def selfDestructKillsMostInGame(self):
        return self._selfDestructKillsMostInGame

    @property
    def abilityDamageDone(self):
        return self._abilityDamageDone

    @property
    def abilityDamageDoneAvgPer10Min(self):
        return self._abilityDamageDoneAvgPer10Min

    @property
    def abilityDamageDoneMostInGame(self):
        return self._abilityDamageDoneMostInGame

    @property
    def shieldsCreated(self):
        return self._shieldsCreated

    @property
    def shieldsCreatedAvgPer10Min(self):
        return self._shieldsCreatedAvgPer10Min

    @property
    def shieldsCreatedMostInGame(self):
        return self._shieldsCreatedMostInGame

    @property
    def duplicateKills(self):
        return self._duplicateKills

    @property
    def duplicateKillsAvgPer10Min(self):
        return self._duplicateKillsAvgPer10Min

    @property
    def duplicateKillsMostInGame(self):
        return self._duplicateKillsMostInGame

    @property
    def focusingBeamAccuracy(self):
        return self._focusingBeamAccuracy

    @property
    def focusingBeamKills(self):
        return self._focusingBeamKills

    @property
    def focusingBeamKillsAvgPer10Min(self):
        return self._focusingBeamKillsAvgPer10Min

    @property
    def focusingBeamKillsMostInGame(self):
        return self._focusingBeamKillsMostInGame

    @property
    def stickyBombsDirectHitsAccuracy(self):
        return self._stickyBombsDirectHitsAccuracy

    @property
    def stickyBombsDirectHitsAvgPer10Min(self):
        return self._stickyBombsDirectHitsAvgPer10Min

    @property
    def stickyBombsDirectHitsMostInGame(self):
        return self._stickyBombsDirectHitsMostInGame

    @property
    def stickyBombsKills(self):
        return self._stickyBombsKills

    @property
    def stickyBombsKillsAvgPer10Min(self):
        return self._stickyBombsKillsAvgPer10Min

    @property
    def stickyBombsKillsMostInGame(self):
        return self._stickyBombsKillsMostInGame

    @property
    def damageReflected(self):
        return self._damageReflected

    @property
    def damageReflectedAvgPer10Min(self):
        return self._damageReflectedAvgPer10Min

    @property
    def damageReflectedMostInGame(self):
        return self._damageReflectedMostInGame

    @property
    def dragonbladesKills(self):
        return self._dragonbladesKills

    @property
    def dragonbladesKillsAvgPer10Min(self):
        return self._dragonbladesKillsAvgPer10Min

    @property
    def dragonbladesKillsMostInGame(self):
        return self._dragonbladesKillsMostInGame

    @property
    def dragonstrikeKills(self):
        return self._dragonstrikeKills

    @property
    def dragonstrikeKillsAvgPer10Min(self):
        return self._dragonstrikeKillsAvgPer10Min

    @property
    def dragonstrikeKillsMostInGame(self):
        return self._dragonstrikeKillsMostInGame

    @property
    def scatterArrowKills(self):
        return self._scatterArrowKills

    @property
    def scatterArrowKillsAvgPer10Min(self):
        return self._scatterArrowKillsAvgPer10Min

    @property
    def scatterArrowKillsMostInGame(self):
        return self._scatterArrowKillsMostInGame

    @property
    def stormArrowKills(self):
        return self._stormArrowKills

    @property
    def stormArrowKillsAvgPer10Min(self):
        return self._stormArrowKillsAvgPer10Min

    @property
    def stormArrowKillsMostInGame(self):
        return self._stormArrowKillsMostInGame

    @property
    def concussionMineKills(self):
        return self._concussionMineKills

    @property
    def concussionMineKillsAvgPer10Min(self):
        return self._concussionMineKillsAvgPer10Min

    @property
    def concussionMineKillsMostInGame(self):
        return self._concussionMineKillsMostInGame

    @property
    def enemiesTrapped(self):
        return self._enemiesTrapped

    @property
    def enemiesTrappedAvgPer10Min(self):
        return self._enemiesTrappedAvgPer10Min

    @property
    def enemiesTrappedMostInGame(self):
        return self._enemiesTrappedMostInGame

    @property
    def ripTireKills(self):
        return self._ripTireKills

    @property
    def ripTireKillsAvgPer10Min(self):
        return self._ripTireKillsAvgPer10Min

    @property
    def ripTireKillsMostInGame(self):
        return self._ripTireKillsMostInGame

    @property
    def soundBarriersProvided(self):
        return self._soundBarriersProvided

    @property
    def soundBarriersProvidedAvgPer10Min(self):
        return self._soundBarriersProvidedAvgPer10Min

    @property
    def soundBarriersProvidedMostInGame(self):
        return self._soundBarriersProvidedMostInGame

    @property
    def deadeyeKills(self):
        return self._deadeyeKills

    @property
    def deadeyeKillsAvgPer10Min(self):
        return self._deadeyeKillsAvgPer10Min

    @property
    def deadeyeKillsMostInGame(self):
        return self._deadeyeKillsMostInGame

    @property
    def fanTheHammerKills(self):
        return self._fanTheHammerKills

    @property
    def fanTheHammerKillsAvgPer10Min(self):
        return self._fanTheHammerKillsAvgPer10Min

    @property
    def fanTheHammerKillsMostInGame(self):
        return self._fanTheHammerKillsMostInGame

    @property
    def blizzardKills(self):
        return self._blizzardKills

    @property
    def blizzardKillsAvgPer10Min(self):
        return self._blizzardKillsAvgPer10Min

    @property
    def blizzardKillsMostInGame(self):
        return self._blizzardKillsMostInGame

    @property
    def enemiesFrozen(self):
        return self._enemiesFrozen

    @property
    def enemiesFrozenAvgPer10Min(self):
        return self._enemiesFrozenAvgPer10Min

    @property
    def enemiesFrozenMostInGame(self):
        return self._enemiesFrozenMostInGame

    @property
    def blasterKills(self):
        return self._blasterKills

    @property
    def blasterKillsAvgPer10Min(self):
        return self._blasterKillsAvgPer10Min

    @property
    def blasterKillsMostInGame(self):
        return self._blasterKillsMostInGame

    @property
    def playersResurrected(self):
        return self._playersResurrected

    @property
    def playersResurrectedAvgPer10Min(self):
        return self._playersResurrectedAvgPer10Min

    @property
    def playersResurrectedMostInGame(self):
        return self._playersResurrectedMostInGame

    @property
    def coalescenceHealing(self):
        return self._coalescenceHealing

    @property
    def coalescenceHealingAvgPer10Min(self):
        return self._coalescenceHealingAvgPer10Min

    @property
    def coalescenceHealingMostInGame(self):
        return self._coalescenceHealingMostInGame

    @property
    def coalescenceKills(self):
        return self._coalescenceKills

    @property
    def coalescenceKillsAvgPer10Min(self):
        return self._coalescenceKillsAvgPer10Min

    @property
    def coalescenceKillsMostInGame(self):
        return self._coalescenceKillsMostInGame

    @property
    def secondaryFireAccuracy(self):
        return self._secondaryFireAccuracy

    @property
    def superchargerAssists(self):
        return self._superchargerAssists

    @property
    def superchargerAssistsAvgPer10Min(self):
        return self._superchargerAssistsAvgPer10Min

    @property
    def superchargerAssistsMostInGame(self):
        return self._superchargerAssistsMostInGame

    @property
    def barrageKills(self):
        return self._barrageKills

    @property
    def barrageKillsAvgPer10Min(self):
        return self._barrageKillsAvgPer10Min

    @property
    def barrageKillsMostInGame(self):
        return self._barrageKillsMostInGame

    @property
    def directHitsAccuracy(self):
        return self._directHitsAccuracy

    @property
    def rocketDirectHits(self):
        return self._rocketDirectHits

    @property
    def rocketDirectHitsAvgPer10Min(self):
        return self._rocketDirectHitsAvgPer10Min

    @property
    def rocketDirectHitsMostInGame(self):
        return self._rocketDirectHitsMostInGame

    @property
    def deathsBlossomKills(self):
        return self._deathsBlossomKills

    @property
    def deathsBlossomKillsAvgPer10Min(self):
        return self._deathsBlossomKillsAvgPer10Min

    @property
    def deathsBlossomKillsMostInGame(self):
        return self._deathsBlossomKillsMostInGame

    @property
    def chargeKills(self):
        return self._chargeKills

    @property
    def chargeKillsAvgPer10Min(self):
        return self._chargeKillsAvgPer10Min

    @property
    def chargeKillsMostInGame(self):
        return self._chargeKillsMostInGame

    @property
    def earthshatterKills(self):
        return self._earthshatterKills

    @property
    def earthshatterKillsAvgPer10Min(self):
        return self._earthshatterKillsAvgPer10Min

    @property
    def earthshatterKillsMostInGame(self):
        return self._earthshatterKillsMostInGame

    @property
    def fireStrikeKills(self):
        return self._fireStrikeKills

    @property
    def fireStrikeKillsAvgPer10Min(self):
        return self._fireStrikeKillsAvgPer10Min

    @property
    def fireStrikeKillsMostInGame(self):
        return self._fireStrikeKillsMostInGame

    @property
    def rocketHammerMeleeAccuracy(self):
        return self._rocketHammerMeleeAccuracy

    @property
    def enemiesHooked(self):
        return self._enemiesHooked

    @property
    def enemiesHookedAvgPer10Min(self):
        return self._enemiesHookedAvgPer10Min

    @property
    def enemiesHookedMostInGame(self):
        return self._enemiesHookedMostInGame

    @property
    def hookAccuracy(self):
        return self._hookAccuracy

    @property
    def hookAccuracyBestInGame(self):
        return self._hookAccuracyBestInGame

    @property
    def hooksAttempted(self):
        return self._hooksAttempted

    @property
    def wholeHogKillsAvgPer10Min(self):
        return self._wholeHogKillsAvgPer10Min

    @property
    def wholeHogKillsMostInGame(self):
        return self._wholeHogKillsMostInGame

    @property
    def accretionKills(self):
        return self._accretionKills

    @property
    def accretionKillsAvgPer10Min(self):
        return self._accretionKillsAvgPer10Min

    @property
    def accretionKillsMostInGame(self):
        return self._accretionKillsMostInGame

    @property
    def damageAbsorbed(self):
        return self._damageAbsorbed

    @property
    def damageAbsorbedAvgPer10Min(self):
        return self._damageAbsorbedAvgPer10Min

    @property
    def damageAbsorbedMostInGame(self):
        return self._damageAbsorbedMostInGame

    @property
    def graviticFluxKills(self):
        return self._graviticFluxKills

    @property
    def graviticFluxKillsAvgPer10Min(self):
        return self._graviticFluxKillsAvgPer10Min

    @property
    def graviticFluxKillsMostInGame(self):
        return self._graviticFluxKillsMostInGame

    @property
    def bioticFieldHealingDone(self):
        return self._bioticFieldHealingDone

    @property
    def bioticFieldsDeployed(self):
        return self._bioticFieldsDeployed

    @property
    def helixRocketKills(self):
        return self._helixRocketKills

    @property
    def helixRocketKillsAvgPer10Min(self):
        return self._helixRocketKillsAvgPer10Min

    @property
    def helixRocketKillsMostInGame(self):
        return self._helixRocketKillsMostInGame

    @property
    def tacticalVisorKills(self):
        return self._tacticalVisorKills

    @property
    def tacticalVisorKillsAvgPer10Min(self):
        return self._tacticalVisorKillsAvgPer10Min

    @property
    def tacticalVisorKillsMostInGame(self):
        return self._tacticalVisorKillsMostInGame

    @property
    def enemiesEmpd(self):
        return self._enemiesEmpd

    @property
    def enemiesEmpdAvgPer10Min(self):
        return self._enemiesEmpdAvgPer10Min

    @property
    def enemiesEmpdMostInGame(self):
        return self._enemiesEmpdMostInGame

    @property
    def enemiesHacked(self):
        return self._enemiesHacked

    @property
    def enemiesHackedAvgPer10Min(self):
        return self._enemiesHackedAvgPer10Min

    @property
    def enemiesHackedMostInGame(self):
        return self._enemiesHackedMostInGame

    @property
    def playersTeleported(self):
        return self._playersTeleported

    @property
    def playersTeleportedAvgPer10Min(self):
        return self._playersTeleportedAvgPer10Min

    @property
    def playersTeleportedMostInGame(self):
        return self._playersTeleportedMostInGame

    @property
    def primaryFireAccuracy(self):
        return self._primaryFireAccuracy

    @property
    def secondaryDirectHitsAvgPer10Min(self):
        return self._secondaryDirectHitsAvgPer10Min

    @property
    def sentryTurretsKills(self):
        return self._sentryTurretsKills

    @property
    def sentryTurretsKillsAvgPer10Min(self):
        return self._sentryTurretsKillsAvgPer10Min

    @property
    def sentryTurretsKillsMostInGame(self):
        return self._sentryTurretsKillsMostInGame

    @property
    def armorPacksCreated(self):
        return self._armorPacksCreated

    @property
    def armorPacksCreatedAvgPer10Min(self):
        return self._armorPacksCreatedAvgPer10Min

    @property
    def armorPacksCreatedMostInGame(self):
        return self._armorPacksCreatedMostInGame

    @property
    def moltenCoreKills(self):
        return self._moltenCoreKills

    @property
    def moltenCoreKillsAvgPer10Min(self):
        return self._moltenCoreKillsAvgPer10Min

    @property
    def moltenCoreKillsMostInGame(self):
        return self._moltenCoreKillsMostInGame

    @property
    def torbjornKills(self):
        return self._torbjornKills

    @property
    def torbjornKillsAvgPer10Min(self):
        return self._torbjornKillsAvgPer10Min

    @property
    def torbjornKillsMostInGame(self):
        return self._torbjornKillsMostInGame

    @property
    def turretsDamageAvgPer10Min(self):
        return self._turretsDamageAvgPer10Min

    @property
    def turretsKills(self):
        return self._turretsKills

    @property
    def turretsKillsAvgPer10Min(self):
        return self._turretsKillsAvgPer10Min

    @property
    def turretsKillsMostInGame(self):
        return self._turretsKillsMostInGame

    @property
    def healthRecovered(self):
        return self._healthRecovered

    @property
    def healthRecoveredAvgPer10Min(self):
        return self._healthRecoveredAvgPer10Min

    @property
    def healthRecoveredMostInGame(self):
        return self._healthRecoveredMostInGame

    @property
    def pulseBombsAttached(self):
        return self._pulseBombsAttached

    @property
    def pulseBombsAttachedAvgPer10Min(self):
        return self._pulseBombsAttachedAvgPer10Min

    @property
    def pulseBombsAttachedMostInGame(self):
        return self._pulseBombsAttachedMostInGame

    @property
    def pulseBombsKills(self):
        return self._pulseBombsKills

    @property
    def pulseBombsKillsAvgPer10Min(self):
        return self._pulseBombsKillsAvgPer10Min

    @property
    def pulseBombsKillsMostInGame(self):
        return self._pulseBombsKillsMostInGame

    @property
    def scopedCriticalHitsKills(self):
        return self._scopedCriticalHitsKills

    @property
    def scopedCriticalHitsKillsAvgPer10Min(self):
        return self._scopedCriticalHitsKillsAvgPer10Min

    @property
    def venomMineKills(self):
        return self._venomMineKills

    @property
    def venomMineKillsAvgPer10Mi(self):
        return self._venomMineKillsAvgPer10Mi

    @property
    def venomMineKillsMostInGame(self):
        return self._venomMineKillsMostInGame

    @property
    def playersKnockedBack(self):
        return self._playersKnockedBack

    @property
    def playersKnockedBackAvgPer10Min(self):
        return self._playersKnockedBackAvgPer10Min

    @property
    def playersKnockedBackMostInGame(self):
        return self._playersKnockedBackMostInGame

    @property
    def primalRageMeleeAccuracy(self):
        return self._primalRageMeleeAccuracy

    @property
    def teslaCannonAccuracy(self):
        return self._teslaCannonAccuracy

    @property
    def weaponKills(self):
        return self._weaponKills

    @property
    def grapplingClawKills(self):
        return self._grapplingClawKills

    @property
    def grapplingClawKillsAvgPer10Min(self):
        return self._grapplingClawKillsAvgPer10Min

    @property
    def grapplingClawKillsMostInGame(self):
        return self._grapplingClawKillsMostInGame

    @property
    def minefieldKills(self):
        return self._minefieldKills

    @property
    def minefieldKillsAvgPer10Min(self):
        return self._minefieldKillsAvgPer10Min

    @property
    def minefieldKillsMostInGame(self):
        return self._minefieldKillsMostInGame

    @property
    def piledriverKills(self):
        return self._piledriverKills

    @property
    def piledriverKillsAvgPer10Min(self):
        return self._piledriverKillsAvgPer10Min

    @property
    def piledriverKillsMostInGame(self):
        return self._piledriverKillsMostInGame

    @property
    def averageEnergy(self):
        return self._averageEnergy

    @property
    def averageEnergyBestInGame(self):
        return self._averageEnergyBestInGame

    @property
    def gravitonSurgeKills(self):
        return self._gravitonSurgeKills

    @property
    def gravitonSurgeKillsAvgPer10Min(self):
        return self._gravitonSurgeKillsAvgPer10Min

    @property
    def gravitonSurgeKillsMostInGame(self):
        return self._gravitonSurgeKillsMostInGame

    @property
    def highEnergyKills(self):
        return self._highEnergyKills

    @property
    def highEnergyKillsAvgPer10Min(self):
        return self._highEnergyKillsAvgPer10Min

    @property
    def highEnergyKillsMostInGame(self):
        return self._highEnergyKillsMostInGame

    @property
    def projectedBarriersApplied(self):
        return self._projectedBarriersApplied

    @property
    def projectedBarriersAppliedAvgPer10Min(self):
        return self._projectedBarriersAppliedAvgPer10Min

    @property
    def projectedBarriersAppliedMostInGame(self):
        return self._projectedBarriersAppliedMostInGame

    @property
    def transcendenceHealing(self):
        return self._transcendenceHealing

    @property
    def transcendenceHealingBest(self):
        return self._transcendenceHealingBest
