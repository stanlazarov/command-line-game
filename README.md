# Command line dungeon crawler game

The game is written with python3.6.7 for a job application.

## To start the game:

```
python run.py
```

## Description

You make a character and start in the first room of a dungeon. You can pick up items and fight monsters and your goal is to reach the end of the maze.

Items are either equipment or food. Equipment items give you attack or defense that is used in combat. Food restores health. Each item has weight and your character has a maximum weight weight capacity. You can pick up items from rooms and you can drop them if u need space.

Each room has a number as it's name. Some rooms are locked and you need to find the key elsewhere in the dungeon. You can move to another adjacent room if it isn't locked and there isn't a monster in your current room guarding the exit. When you move to another room u lose half a health point so don't forget to eat some food to regenerate health from time to time.

When you encounter a monster in the room you cant exit before you defeat it. The fighting consist of your character attacking the monster and then the monster attacking you until either one dies. Attack from items increases your attack damage and defense reduces the damage you take from monster attacks.

## Commands

- help - prints the list of commands.
- location - prints the room the character is currently in, items and monsters in the room and a list of the available exits.
- go to room <room_id> - the character will move to the room with <room_id> and execute the location command.
- items - prints the list of the items in the character's backpack.
- pick up <item_name> - the character will pick up the item and execute the items command.
- drop <item_name> - the character will drop the item and execute the items command.
- eat <item_name> - the character eats a food item and restores 3 health points.
- fight - the character engages in combat with the monster in the current room.
- quit = exits the game
