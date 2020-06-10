import OverwatchUserDirectory
user = OverwatchUserDirectory.User("milkyman#21932")
print(user.competitiveStats.career_stats.hero_dict["ana"].assists.__dict__)