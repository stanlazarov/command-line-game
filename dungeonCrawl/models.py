class BaseUnit(object):
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.current_health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense

    def is_dead(self):
        return self.current_health <= 0


class Player(BaseUnit):
    def __init__(self, name, starting_room, health=10, attack=2, defense=0):
        BaseUnit.__init__(self, name, health, attack, defense)
        self.inventory = []
        self.weight_capacity = 10
        self.current_weight = 0
        self.current_room = starting_room

    def add_item(self, item):
        if self.current_weight + item.weight >= self.weight_capacity:
            print('You don\'t have enough space to pick up {}. You can use the drop command to drop another item or eat some food to make space.'.format(item.name))
            return False
        else:
            self.current_weight += item.weight
            self.attack += item.attack
            self.defense += item.defense
            self.inventory.append(item)
            print('You picked up {}'.format(item.name))
            return True

    def has_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                return True
        return False

    def drop_item(self, item_name):
        if not self.has_item(item_name):
            print('You don\'t  have that item.')
        else:
            for item in self.inventory:
                if item.name == item_name:
                    print('You have dropped {}'.format(item.name))
                    self.attack -= item.attack
                    self.defense -= item.defense
                    self.current_weight -= item.weight
                    self.inventory.remove(item)

    def eat(self, item_name):
        if not self.has_item(item_name):
            print('You don\'t  have an item with that name.')
        else:
            for item in self.inventory:
                if item.name == item_name:
                    if item.is_food:
                        print(
                            'You have eaten {} and restored 3 health points.'.format(item.name))
                        self.current_health += 3
                        if self.current_health > self.max_health:
                            self.current_health = self.max_health
                        self.current_weight -= item.weight
                        self.inventory.remove(item)
                    else:
                        print('You can\'t eat that item because it\' not food.')

    def fight(self, monster):
        monster.current_health -= self.attack - monster.defense
        if monster.is_dead():
            return 'monster dead'
        self.current_health -= monster.attack - self.defense
        if self.is_dead():
            return 'player dead'
        return 'fighting'


class Monster(BaseUnit):
    def __init__(self, name, health=5, attack=1, defense=1):
        BaseUnit.__init__(self, name, health, attack, defense)


class Item(object):
    def __init__(self, name, weight, is_food=False, attack=0, defense=0):
        self.name = name
        self.weight = weight
        self.is_food = is_food
        self.attack = attack
        self.defense = defense


class Maze(object):
    def __init__(self, number_of_rooms, adj_matrix, items, locked, monsters):
        self.number_of_rooms = number_of_rooms
        self.adj_matrix = adj_matrix
        self.items = items
        self.locked = locked
        self.monsters = monsters

    def is_locked(self, room):
        return self.locked[room]

    def has_item(self, room):
        return self.items[room]

    def has_monster(self, room):
        return self.monsters[room]

    def get_adjacent_rooms(self, room):
        res = []
        for i, is_neighbour in enumerate(self.adj_matrix[room]):
            if is_neighbour:
                res.append(i)
        return res
