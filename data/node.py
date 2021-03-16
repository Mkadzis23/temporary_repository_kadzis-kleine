
class Node(object):
    def __init__(self, gameMap):
        self.state = gameMap
        self.children = []
        self.parent = None

    def add_child(self, node):
        self.children.append(node)

    #@parent.setter
    def set_parent(self, node):
        self.parent = node

    def get_parent(self, node):
        return self.parent

    def hasParent(self):
        if self.parent == None:
            return False
        return True