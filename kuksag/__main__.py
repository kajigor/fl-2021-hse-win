#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import base
import parser


def parse_args():
    parser = argparse.ArgumentParser(description='Parse arguments')
    parser.add_argument('--input', '-i', default=None)
    parser.add_argument('--output', '-o', default=None)
    return parser.parse_args()


def readline(default_input):
    if default_input is None:
        return input('> ')
    return default_input.readline()


def error():
    print('bad input')
    exit(1)



if __name__ == '__main__':
    args = parse_args()
    graph = base.FiniteStateMachine()

    default_input = None
    if args.input is not None:
        default_input = open(args.input, 'r')

    vertex_line = readline(default_input)
    graph.vertices = parser.parse(vertex_line)

    if not isinstance(graph.vertices, int):
        error()

    edges_line = readline(default_input)
    graph.edges = parser.parse(edges_line)

    if not isinstance(graph.edges, int):
        error()

    for i in range(graph.edges):
        edge_line = readline(default_input)
        edge = parser.parse(edge_line)

        if not isinstance(edge, base.Edge):
            error()

        graph.adjacency_list[edge.vertex_from].append(edge)
    root_line = readline(default_input)
    graph.root = parser.parse(root_line)

    if not isinstance(graph.root, int):
        error()

    terminal_line = readline(default_input)
    graph.terminals = parser.parse(terminal_line)

    if not isinstance(graph.terminals, int):
        error()

    if args.output is None:
        print(graph)
    else:
        with open(args.output, 'w+') as output_data:
            output_data.write(str(graph))
