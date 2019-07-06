class Player(object):
    def __init__(self, name, starting_room):
        self.name = name
        self.inventory = []
        self.weight_capacity = 10
        self.current_weight = 0
        self.current_room = starting_room

    def add_item(self, item):
        if self.current_weight + item.weight >= self.weight_capacity:
            print('You don\'t have enough space to pick up {}. You can use the drop command to drop another item to make space.'.format(item.name))
            return False
        else:
            self.current_weight += item.weight
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
                    self.inventory.remove(item)


class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Maze(object):
    def __init__(self, number_of_rooms, adj_matrix, items, locked):
        self.number_of_rooms = number_of_rooms
        self.adj_matrix = adj_matrix
        self.items = items
        self.locked = locked

    def is_locked(self, room):
        return self.locked[room]

    def has_item(self, room):
        return self.items[room]

    def get_adjacent_rooms(self, room):
        res = []
        for i, is_neighbour in enumerate(self.adj_matrix[room]):
            if is_neighbour:
                res.append(i)
        return res
