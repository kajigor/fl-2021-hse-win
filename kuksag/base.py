import attr
from collections import defaultdict

@attr.s
class Edge:
    vertex_from = attr.ib(default=None)
    vertex_to = attr.ib(default=None)
    edge_value = attr.ib(default=None)


@attr.s
class FiniteStateMachine:
    vertices = attr.ib(default=None)
    edges = attr.ib(default=None)
    root = attr.ib(default=None)
    terminals = attr.ib(default=[])
    adjacency_list = attr.ib(default=defaultdict(list))
