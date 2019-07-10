from dungeonCrawl.models import Item, Monster


def maze_1():
    N = 20
    adj_matrix = [
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    ]

    items = [False] * N
    locked = [False] * N
    monsters = [False] * N

    items.insert(0, Item(name='sword', weight=2, attack=2))
    items.insert(1, Item(name='pie', weight=0.5, is_food=True))
    items.insert(2, Item(name='apple', weight=0.5, is_food=True))
    items.insert(3, Item(name='pizza', weight=0.5, is_food=True))
    items.insert(4, Item(name='donut', weight=0.5, is_food=True))
    items.insert(5, Item(name='helm', weight=1, defense=1))
    items.insert(6, Item(name='sandwich', weight=0.5, is_food=True))
    items.insert(8, Item(name='boots', weight=1, defense=1))
    items.insert(9, Item(name='banana', weight=0.5, is_food=True))
    items.insert(10, Item(name='red_key', weight=0.2))
    items.insert(11, Item(name='bread', weight=0.5, is_food=True))
    items.insert(12, Item(name='blue_key', weight=0.2))
    items.insert(13, Item(name='steak', weight=0.5, is_food=True))
    items.insert(14, Item(name='axe', weight=2, attack=3))
    items.insert(15, Item(name='potato', weight=0.5, is_food=True))
    items.insert(18, Item(name='dagger', weight=1, attack=1))
    items.insert(19, Item(name='pie', weight=0.5, is_food=True))

    locked.insert(11, 'red_key')
    locked.insert(14, 'blue_key')

    monsters.insert(1, Monster('skeleton'))
    monsters.insert(2, Monster('skeleton'))
    monsters.insert(6, Monster('skeleton'))
    monsters.insert(10, Monster('troll', health=8, attack=2, defense=1))
    monsters.insert(12, Monster('goblin', health=6, attack=3, defense=0))
    monsters.insert(16, Monster('minotaur', health=12, attack=3, defense=2))

    return (N, adj_matrix, items, locked, monsters)
