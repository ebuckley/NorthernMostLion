import sc2reader, os, shutil, sys
import stats
from stats import *
from sc2reader.utils import Length
replay_path = "C:\\Users\\Ersin\\Documents\\StarCraft II\\Accounts\\64589640\\1-S2-1-1526382\\Replays\\Multiplayer"

gameTimes = list()
gameTimesWins = list()
for replay in sc2reader.load_replays(replay_path, load_level = 1):
    if replay.category == "Ladder" and replay.type == "1v1":
        # load extra resources from the replay file
        replay.load_details()
        replay.load_players()

        gameTimes.append(replay.length.total_seconds())

        #print help(replay)
        #print help(replay.length)
        print replay.length
        print replay.date

        for x in replay.teams:
            for y in x:
                print y
                # if we win this game then add it to the list of victory games
                if y.name == "Mania" and y.result == "Win":
                    gameTimesWins.append(replay.length.total_seconds())





print "===="
print "results for all manias games"
print "Average length of all games: " + str(Length(0, mean(gameTimes)))
print "Standard deviations of all games: " +  str(Length(sd(gameTimes)))
print "==="
print "results for manias wins"
print "Average length of  games: " +str(Length(0, mean(gameTimesWins)))
print "Standard deviations of  games: " +  str(Length(sd(gameTimesWins)))



