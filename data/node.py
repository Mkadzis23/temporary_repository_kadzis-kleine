
class Node(object):
    def __init__(self, gameMap):
        self.state = gameMap
        self.children = []

    def add_child(self, node):
        self.children.append(node)