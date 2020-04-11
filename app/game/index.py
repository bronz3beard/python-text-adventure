def get_player_command():
    return input('Action: ')

def play():
    print("Escape!")
    while True:
        action_input = get_player_command()
        if action_input.lower() == 'n':
            print('Go North!')
            break
        if action_input.lower() == 's':
            print('Go South!')
            break
        if action_input.lower() == 'e':
            print('Go East!')
            break
        if action_input.lower() == 'w':
            print('Go West!')
            break
        print('Invalid action!')

play()