from dungeonCrawl.mazes import maze_1
from dungeonCrawl.models import Player, Maze


class Commands(object):
    @staticmethod
    def help():
        print('- help = prints the list of commands.')
        print('- location = prints the room the player is currently in and a list of the available exits.')
        print('- go to room <room_id> = the player will move to the room with <room_id> and execute the location command.')
        print('- items = prints the list of the items in the player\'s backpack.')
        print('- pick up <item_name> = the player will pick up the item and execute the items command.')
        print('- drop <item_name> = the player will drop the item and execute the items command.')
        print(
            '- eat <item_name> = the player eats a food item and restores 3 health points.')
        print('- fight = you engage in combat with the monster in the current room.')
        print('- quit = exits the game')
        print('Every time you move to another room you lose 0.5 health points so try to eat food from time to time.')

    @staticmethod
    def location(player, maze):
        if player.current_room == 17:
            print('Congratulations, you have reached the end of the maze! You can go back and explore more or type "quit" to exit the game.')
        if player.is_dead():
            print('You have reached 0 health points and died.')
            return

        print('{} ({}/{} HP|{} attack|{} defense) is currently in room {}'.format(
            player.name, player.current_health, player.max_health, player.attack, player.defense, player.current_room))

        if maze.has_monster(player.current_room):
            print('This room has a monster: {}. You need to defeat it to exit the room or pick up items.'.format(
                maze.monsters[player.current_room].name))

        if maze.has_item(player.current_room):
            print('This room has an item: {}'.format(
                maze.items[player.current_room].name))

        exits = maze.get_adjacent_rooms(player.current_room)
        print('The available exits are to:')
        for exit in exits:
            print('- room {}'.format(exit))

    @staticmethod
    def go_to(player, maze, room):
        if not room in maze.get_adjacent_rooms(player.current_room):
            print('There isn\'t an exit to that room')
            Commands.location(player, maze)
            return
        else:
            if maze.has_monster(player.current_room):
                print(
                    'A monster is blocking the exit. You need to defeat it to leave the room.')
            elif maze.is_locked(room):
                print('This room is locked and needs a {} key to be unlocked'.format(
                    maze.locked[room]))
                if player.has_item(maze.locked[room]):
                    while True:
                        unlock = input(
                            'Do you want to unlock the door with your {}? (yes/no): '.format(maze.locked[room]))
                        if unlock == 'yes':
                            print('You unlocked the door')
                            player.drop_item(maze.locked[room])
                            maze.locked[room] = False
                            player.current_health -= 0.5
                            player.current_room = room
                            Commands.location(player, maze)
                            break
                        elif unlock == 'no':
                            break
                        else:
                            print('Type yes or no')
            else:
                player.current_health -= 0.5
                player.current_room = room
                Commands.location(player, maze)

    @staticmethod
    def items(player):
        if len(player.inventory) == 0:
            print('You have no items')
        else:
            print('Weight: {}/{}'.format(player.current_weight, player.weight_capacity))
            print('items:')
            for item in player.inventory:
                print('- {} (weight: {}) '.format(
                    item.name, item.weight), end='')
                if not item.is_food:
                    if item.attack:
                        print('gives {} attack'.format(item.attack))
                    elif item.defense:
                        print('gives {} defense'.format(item.defense))
                else:
                    print('food: can be eaten to restore 3 health points')

    @staticmethod
    def pick_up(player, maze, item_name):
        if not maze.items[player.current_room]:
            print('This room does not have items')
        elif not maze.items[player.current_room].name == item_name:
            print('Wrong item name')
        elif maze.has_monster(player.current_room):
            print(
                'There is a monster in this room. You need to defeat it to pick up the item.')
        elif player.add_item(maze.items[player.current_room]):
            maze.items[player.current_room] = False
            Commands.items(player)

    @staticmethod
    def drop(player, item_name):
        player.drop_item(item_name)
        Commands.items(player)

    @staticmethod
    def fight(player, maze):
        if maze.has_monster(player.current_room):
            monster = maze.monsters[player.current_room]
            print('{} ({}/{}HP) attack: {} | defense: {}'.format(
                player.name, player.current_health, player.max_health, player.attack, player.defense))
            print('{} ({}/{}HP) attack: {} | defense: {}\n'.format(
                monster.name, monster.current_health, monster.max_health, monster.attack, monster.defense))
            while True:
                cmd = input('Type "attack" to attack the monster: ')
                if cmd == 'attack':
                    outcome = player.fight(monster)
                    if outcome == 'monster dead':
                        print('{} has died.\n'.format(monster.name))
                        maze.monsters[player.current_room] = False
                        Commands.location(player, maze)
                        break
                    elif outcome == 'player dead':
                        Commands.location(player, maze)
                        break
                    print('\n{} ({}/{}HP) attack: {} | defense: {}'.format(
                        player.name, player.current_health, player.max_health, player.attack, player.defense))
                    print('{} ({}/{}HP) attack: {} | defense: {}\n'.format(
                        monster.name, monster.current_health, monster.max_health, monster.attack, monster.defense))
        else:
            print('There isn\'t a monster in this room.')

    @staticmethod
    def eat(player, item_name):
        player.eat(item_name)


def game_loop():
    # Create player
    name = input('Enter your character\'s name: ')
    player = Player(name=name, starting_room=0)

    # Create maze (can make another maze in mazes.py and use it)
    maze = Maze(*maze_1())

    Commands.location(player, maze)
    print('Type help to get the list of commands.')
    # Main game loop
    while True:
        if player.is_dead():
            break
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
            Commands.items(player)
        elif split_cmd[0] == 'pick' and split_cmd[1] == 'up':
            Commands.pick_up(player, maze, split_cmd[2])
        elif split_cmd[0] == 'drop':
            Commands.drop(player, split_cmd[1])
        elif split_cmd[0] == 'eat':
            Commands.eat(player, split_cmd[1])
        elif cmd == 'fight':
            Commands.fight(player, maze)
        else:
            print('invalid command. (type "help" to get the list of commands)')
