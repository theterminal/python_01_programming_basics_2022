# 20220218 - Python Code - Best Player

flag_h3 = num_goals = num_goals_best_player = 0
best_player_name = ''

while True:
    player_name = input()
    if player_name == 'END':
        break

    num_goals = int(input())
    if num_goals > num_goals_best_player:
        num_goals_best_player = num_goals
        best_player_name = player_name
        if num_goals > 2:
            flag_h3 = 1
            if num_goals > 9:
                break

print(f'{best_player_name} is the best player!')

if flag_h3:
    print(f'He has scored {num_goals_best_player} goals and made a hat-trick !!!')
else:
    print(f'He has scored {num_goals_best_player} goals.')
