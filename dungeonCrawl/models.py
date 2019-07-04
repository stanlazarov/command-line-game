class Player(object):
    def __init__(self, name, starting_room):
        self.name = name
        self.inventory = Inventory()
        self.weight_capacity = 10
        self.current_weight = 0
        self.current_room = starting_room


class Inventory(object):  # TODO
    def __init__(self):
        items = []


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
