from dungeonCrawl.mazes import maze_1
from dungeonCrawl.models import Player, Maze


class Commands(object):
    @staticmethod
    def help():
        print('- help = prints the list of commands.')
        print('- location = prints the room the player is currently in and a list of the available exits.')
        print('- go to room <room_id> = the player will move to the room with <room_id> and execute the location command.')
        print('- items = prints the list of the items the player\'s backpack.')
        print('- pick up <item_name> = the player will pick up the item and execute the items command.')
        print('- drop <item_name> = the player will drop the item and execute the items command.')
        print('- quit = exits the game')

    @staticmethod
    def location(player, maze):
        print(player.name, 'is currently in room', player.current_room)

        if maze.has_item(player.current_room):
            print("This room has an item:", maze.items[player.current_room])

        exits = maze.get_adjacent_rooms(player.current_room)
        print('The available exits are to:')
        for exit in exits:
            print('room', exit)

    @staticmethod
    def go_to(player, maze, room):
        if not room in maze.get_adjacent_rooms(player.current_room):
            print('There isn\'t an exit to that room')
            Commands.location(player, maze)
            return
        else:
            if maze.is_locked(room):
                print('This room is locked and needs a',
                      maze.locked[room], 'key to be unlocked')
                return
                # Check if the player has that key and whether he wants to unlock it
            player.current_room = room
            Commands.location(player, maze)

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
    name = input('Enter your character\'s name: ')

    player = Player(name=name, starting_room=0)
    maze = Maze(*maze_1())

    Commands.location(player, maze)
    print('Type help to get the list of commands.')
    while True:
        cmd = input('>')
        split_cmd = cmd.split()

        if cmd == 'quit':
            break
        elif cmd == 'help':
            Commands.help()
        elif cmd == 'location':
            Commands.location(player, maze)
        elif split_cmd[0] == 'go' and split_cmd[1] == 'to':
            Commands.go_to(player, maze, int(split_cmd[3]))
        elif cmd == 'items':
            Commands.items()
        elif split_cmd[0] == 'pick' and split_cmd[1] == 'up':
            Commands.pick_up(split_cmd[2])
        elif split_cmd[0] == 'drop':
            Commands.drop(split_cmd[1])
        else:
            print('invalid command. (type help to get the list of commands)')
