class Node:
    def __init__(self, pos=None):
        if pos is None:
            pos = [0., 0., 0.]
        elif not isinstance(pos, list) or len(pos) != 3 or not all(isinstance(e, float) for e in pos):
            raise TypeError("Bad Input: 'pos' should be an array of 3 floats.")
        self.pos = pos
        self.struts, self.tendons = [], []

    def add_strut(self, node) -> bool:
        if type(node) is Node and node not in self.struts:
            self.struts.append(node)
            node.add_strut(self)
            return True
        return False

    def add_tendon(self, node) -> bool:
        if type(node) is Node and node not in self.tendons:
            self.tendons.append(node)
            node.add_tendon(self)
            return True
        return False

    def remove_strut(self, node) -> bool:
        if type(node) is Node:
            pre = len(self.struts)
            self.struts.remove(node)
            return pre == len(self.struts)
        return False

    def remove_tendon(self, node) -> bool:
        if type(node) is Node:
            pre = len(self.tendons)
            self.tendons.remove(node)
            return pre == len(self.tendons)
        return False

    # TODO: Clean up coordinate equality
    def __eq__(self, other):
        if type(other) is not Node:
            return False
        return self.pos[0] == other.pos[0] and self.pos[1] == other.pos[1] and self.pos[2] == other.pos[2]

    def __sub__(self, other):
        return Node([self.pos[0] - other.pos[0], self.pos[1] - other.pos[1], self.pos[2]-other.pos[2]])

    def __str__(self):
        return "Position: " + str(self.pos)