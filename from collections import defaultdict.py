from collections import defaultdict




 # Calculate true shooting percentage for player data with float val returned
def calc_true_shooting(player_data : dict) -> float:
	totalPoints = player_data['freeThrowMade'] + (2 * player_data['fieldGoal2Made']) + (3 * player_data['fieldGoal3Made']) #player's total points scored
	FTA = player_data['freeThrowAttempted'] #Free Throws Attempted
	FGA = player_data['fieldGoal2Attempted'] + player_data['fieldGoal3Attempted'] #Field Goals Attempted
	return (totalPoints / (2 * (FGA + 0.44 * FTA))) * 100 #returns the true shooting percentage as a float val
	


def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
	game_players = defaultdict(int) #track qualified player count
	game_dates = {} #store game dates

	for player_data in game_data: #iterates through each player's game data
		game_id = player_data['gameID'] #sets game ID
		TSP = calc_true_shooting(player_data); #TSP (true shooting percentage) calculation
		
		if game_id not in game_dates: # stores any unstored dates
			game_dates[game_id] = player_data['gameDate']
			
		if TSP >= true_shooting_cutoff: #increments for players who meet the TSP cutoff
			game_players[game_id] += 1

	qualified_games = []
	for game_id, count in game_players.items():
		if count >= player_count:
			qualified_games.append(game_id)
	
	return sorted(
        qualified_games,
        key=lambda game_id: game_dates[game_id][6:] + game_dates[game_id][0:2] + game_dates[game_id][3:5],
        reverse=True
    )
		
		