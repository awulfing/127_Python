# --------------------------------------
# CSCI 127, Lab 4
# May 29, 2020
# Adam Wulfing
# --------------------------------------

def process_season(season, games_played, points_earned):
    print("Season: " + str(season) + ", Games Played: " + str(games_played) +
          ", Points earned: " + str(points_earned))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")

    win = 0
    tie = 0

    for win in range(0, (games_played+1), 1):
        for tie in range(0, games_played+1, 1):
            calc_pts = win*3+tie
            #print(calc_pts)
            if calc_pts == points_earned:
                loss = games_played-(win+tie)
                if loss >= 0:
                    #print(calc_pts)
                    print(str(win) + "-" + str(tie) + "-" +str(loss))
    
    print()

# --------------------------------------

def process_seasons(seasons):
    season_count = 1
    for season in seasons:
        #print(season)
        process_season(season_count, season[0], season[1])
        season_count = season_count + 1

# --------------------------------------

def main():
    # format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]
    process_seasons(soccer_seasons)

# --------------------------------------

main()
