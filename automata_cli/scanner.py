import re
import networkx as nx
import dataclasses 
from automata_cli.patterns import *

def strip_strings(strings: list[str]) -> set[str]:
    return {string.strip() for string in strings if string.strip()}

def read_automata_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()
    return content


def match_alphabet(content: str) -> list[str]:
    return list(re.findall(alphabet_pattern, content))


def match_transition(content: str) -> list[str]:
    return list(re.findall(transition_pattern, content))


def match_accepting_states(content: str) -> list[str]:
    return list(re.findall(accepting_states_pattern, content))


def match_starting_state(content: str) -> list[str]:
    return list(re.findall(starting_states_pattern, content))


def parse_accepting_states(content: str) -> set[str]:
    accepting_states = set()
    matches = match_accepting_states(content)
    for match_ in matches:
        states = match_.replace("=>", "").replace(";", "").split(",")
        accepting_states = accepting_states.union(strip_strings(states))
    return accepting_states


def parse_starting_state(content):
    matches = match_starting_state(content)
    for match_ in matches:
        match_ = match_.strip().replace("->", "").replace(";", "").split(",")
        return match_[0].strip()


def parse_title(content):
    return list(re.findall(title_pattern, content))


def parse_alphabet(content: str) -> set[str]:
    alphabet = set()
    matches = match_alphabet(content)
    for match_ in matches:
        chars = (
            match_.split(":")[1]
            .replace("{", "")
            .replace("}", "")
            .replace(";", "")
            .split(",")
        )
        alphabet = alphabet.union(strip_strings(chars))
    return alphabet



@dataclasses.dataclass
class Machine:
    graph: nx.Graph
    starting_state: set
    accepting_states: set
    alphabet: set
    title: str

def construct_automata_graph_from_transitions(content: str):
    graph = nx.DiGraph()
    title = parse_title(content)[-1]  # take the last title if there are many
    title = title.replace("@title", "").replace(";", "")
    accepting_states = parse_accepting_states(content)
    alphabet = parse_alphabet(content)
    transitions = match_transition(content)
    starting_state = parse_starting_state(content)
    for transition in transitions:
        delimiter = "->"
        transition = transition.strip().replace(";", "").split(":")
        symbols = strip_strings(transition[1].split(","))
        symbols = "".join(symbols)
        if "=>" in transition[0]:
            delimiter = "=>"
        input_states = strip_strings(transition[0].split(delimiter)[0].split(","))
        output_state = transition[0].split(delimiter)[1].strip()
        if delimiter == "=>":
            accepting_states = accepting_states.union(output_state)

        for state in input_states:
            graph.add_edge(state, output_state, weight=symbols)

        alphabet = alphabet.union(symbols)

    return Machine(
        graph=graph,
        starting_state=starting_state,
        accepting_states=accepting_states,
        alphabet=alphabet,
        title=title,
    )


# if __name__ == "__main__":
#     print(parse_alphabet(read_automata_file("test.dfa")))
#     print(parse_accepting_states(read_automata_file("test.dfa")))
#     print(construct_automata_graph_from_transitions(read_automata_file("test.dfa")))
