import graphviz as vz
import yaml

from automata_cli.scanner import *


def viz_add_accepting_states(rendering_graph, accepting_states):
    for state in accepting_states:
        rendering_graph.node(state, shape="doublecircle")


def initialize_rendering_graph(configs, filename=None, title=None):
    configs["renderer"]["filename"] = filename if filename else "output"
    configs["renderer"]["name"] = configs["renderer"]["filename"]
    configs["graph"]["label"] = title if title else ""

    rendering_graph = vz.Digraph(**configs["renderer"])
    rendering_graph.attr(
        **configs["graph"],
    )
    rendering_graph.attr("node", **configs["node"])
    rendering_graph.attr("edge", **configs["edge"])
    return rendering_graph


def build_automata_graph(
    rendering_graph,
    automata_graph,
    accepting_states,
    starting_state,
):
    viz_add_accepting_states(rendering_graph, accepting_states)
    automata_graph_dict = nx.get_edge_attributes(automata_graph, "weight")
    rendering_graph.attr("node", shape="circle")
    for states, symbols in automata_graph_dict.items():
        rendering_graph.node(states[0])
        rendering_graph.node(states[1])
        rendering_graph.edge(
            states[0],
            states[1],
            label="".join(symbols),
        )
    rendering_graph.node("dummyyyyy", shape="point")
    rendering_graph.edge("dummyyyyy", starting_state)
    return rendering_graph 


def dry_render(filename, output, config, format):

    configs = yaml.safe_load(open(config))
    configs["renderer"]["format"] = format 
    machine = construct_automata_graph_from_transitions(read_automata_file(filename))
    rendering_graph = initialize_rendering_graph(
        configs, filename=output, title=machine.title
    )
    rendering_graph = build_automata_graph(
        rendering_graph,
        machine.graph,
        machine.accepting_states,
        machine.starting_state,
    )
    return rendering_graph 
