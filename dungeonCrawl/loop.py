from dungeonCrawl.maze import MazeUtility


class Commands(object):
    @staticmethod
    def help():
        print('- help = prints the list of commands.')
        print('- location = prints the room the player is currently in and a list of the available exits.')
        print('- go to <room_name> = the player will move to <room_name> and execute the location command.')
        print('- items = prints the list of the items the player\'s backpack.')
        print('- pick up <item_name> = the player will pick up the item and execute the items command.')
        print('- drop <item_name> = the player will drop the item and execute the items command.')
        print('- quit = exits the game')

    @staticmethod
    def location(curr_room):  # TODO: show available items and monsters
        exits = MazeUtility.get_adjacent_rooms(curr_room)
        print('You are currently in room' + curr_room)
        print('The available exits are to:')
        for exit in exits:
            print('room' + exit)

    @staticmethod
    def go_to(cur_room, room):
        pass  # TODO

    @staticmethod
    def items():
        pass  # TODO

    @staticmethod
    def pick_up(item):
        pass  # TODO

    @staticmethod
    def drop(item):
        pass  # TODO


def game_loop():
    print('Type help to get the list of commands.')
    curr_room = '1'
    while True:
        cmd = input('>')
        split_cmd = cmd.split()

        if cmd == 'quit':
            break
        elif cmd == 'help':
            Commands.help()
        elif cmd == 'location':
            Commands.location(curr_room)
        elif split_cmd[0] == 'go' and split_cmd[1] == 'to':
            Commands.go_to(split_cmd[2])
        elif cmd == 'items':
            Commands.items()
        elif split_cmd[0] == 'pick' and split_cmd[1] == 'up':
            Commands.pick_up(split_cmd[2])
        elif split_cmd[0] == 'drop':
            Commands.drop(split_cmd[1])
        else:
            print('invalid command. (type help to get the list of commands)')
