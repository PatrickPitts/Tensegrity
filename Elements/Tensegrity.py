from Elements.Node import Node
from Elements.Connector import *
from vpython import *


class Tensegrity:
    def __init__(self, nodes=None):
        self.nodes = []
        if nodes is not None:
            self.add_nodes(nodes)


    def add_nodes(self, nodes):
        if type(nodes) is Node and nodes not in self.nodes:
            self.nodes.append(nodes)
        elif type(nodes) is list and all(isinstance(e, Node) for e in nodes):
            [self.add_nodes(n) for n in nodes]

    def set_connections(self, connections):
        for i in range(len(self.nodes)):
            for j in range(i, len(connections[i])):
                if connections[i][j] == 1:
                    self.nodes[i].add_strut(self.nodes[j])
                elif connections[i][j] == 2:
                    self.nodes[i].add_tendon(self.nodes[j])

    def build_vpython_tensegrity(self):
        elements = []
        for node in self.nodes:
            for other in node.tendons:
                T = Tendon(node, other)
                if T not in elements:
                    elements.append(T)
            for other in node.struts:
                S = Strut(node, other)
                if S not in elements:
                    elements.append(S)
        return [_.get_vpython_element() for _ in elements]
