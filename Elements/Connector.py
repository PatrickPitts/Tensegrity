from Elements.Node import Node
from vpython import *


class Connector:

    def __init__(self, node_a, node_b):
        self.radius = 0.005
        self.color = color.white
        self.node_a = node_a
        self.node_b = node_b

    def add_node(self, node):
        if type(node) is list and len(node) == 2 and all(isinstance(e, Node) for e in node):
            self.set_nodes(node)
        elif self.node_a is None:
            self.node_a = node
        elif self.node_b is None:
            self.node_b = node

    def set_nodes(self, node):
        if type(node) is list and len(node) == 2 and all(isinstance(e, Node) for e in node):
            [self.node_a, self.node_b] = node
            return True
        return False

    def get_vpython_element(self):
        if self.node_a is None or self.node_b is None:
            raise Exception("Missing endpoint nodes.")
        return cylinder(pos=vector(*self.node_a.pos),
                        axis=vector(*(self.node_b - self.node_a).pos),
                        radius=self.radius,
                        color=self.color)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.node_b == other.node_a and self.node_a == other.node_b:
            return True
        elif self.node_a == other.node_a and self.node_b == other.node_b:
            return True
        return False


class Tendon(Connector):
    def __init__(self, node_a, node_b):
        super().__init__(node_a, node_b)
        self.radius = 0.02
        self.color = color.green


class Strut(Connector):
    def __init__(self, node_a, node_b):
        super().__init__(node_a, node_b)
        self.radius = 0.1
