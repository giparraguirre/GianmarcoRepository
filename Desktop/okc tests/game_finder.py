"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

from collections import defaultdict

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int] :
    # Going to return a list of unique gameID's of players who meet the true shooting percentage cutoff.
    qualified_games = [] 
    
	# Calculating the True Shooting Percentage using the formula
    def calculating_true_shooting_percentage(player_stats) :
       # PTS = Total Points Scored
        pts = (2 * player_stats['fieldGoal2Made'] + 3 * player_stats['fieldGoal3Made'] + player_stats['freeThrowMade'])
        
        # FGA = Field Goals Attempted (2PT and 3PT)
        fga = player_stats['fieldGoal2Attempted'] + player_stats['fieldGoal3Attempted']
        
        # FTA = Free Throws Attempted
        fta = player_stats['freeThrowAttempted']
        
        # Denominator
        denominator = 2 * (fga + (0.44 * fta))
        
        # Edge Test in order to avoid division by zero
        if denominator == 0:
            return 0
        
        # TS% Formula
        true_shooting_percentage = (pts / denominator) * 100
        
        return true_shooting_percentage
    
    # Counting the number of players who meet the True Shooting Cutoff
    counting_num_players = defaultdict(int)
    # Since ordered from most to least recent games
    dates_of_the_games = {}

    for game in game_data :
        tsp = calculating_true_shooting_percentage(game)

        if tsp >= true_shooting_cutoff :
            counting_num_players[game['gameID']] += 1

        dates_of_the_games[game['gameID']] = game['gameDate']
    
    qualified_games = [game_id for game_id, count in counting_num_players.items() if count >= player_count]

    qualified_games.sort(key=lambda game_id: dates_of_the_games[game_id], reverse=True)

    return qualified_games