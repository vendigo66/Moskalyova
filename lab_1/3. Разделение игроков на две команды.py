list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

quantity_half = len(list_players)//2
index = quantity_half
team_one = list_players[:index]
team_two = list_players[index:]
print(team_one)
print(team_two)
