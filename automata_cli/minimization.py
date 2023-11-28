import networkx as nx


def convert_graph_to_language(automata_graph, accepting_states, starting_state):
    """
    convert the automata graph (nx graph) to written dfa language
    this version of the function is relatively fast but lengthy
    output
    """
    language = ""
    language += f"-> {starting_state} ; \n"
    graph_dict = nx.get_edge_attributes(automata_graph, "weight")
    for edge, symbols in graph_dict.items():
        language += f"{edge[0]} -> {edge[1]} : {', '.join(symbols)}  ; \n"
    language += f"=> {', '.join(accepting_states)} ;  "
    return language


def convert_graph_to_minimal_language(automata_graph, accepting_states, starting_state):
    """ """
    language = ""
    language += f"-> {starting_state} ; \n"
    same = []
    iss = set()
    edge_list = list(nx.to_edgelist(automata_graph))
    for i in range(len(edge_list)):
        samee = []
        for j in range(i, len(edge_list)):
            if i == j :
                continue
            if (
                edge_list[i][1] == edge_list[j][1]
                and edge_list[i][2]["weight"] == edge_list[j][2]["weight"]
            ):
                samee.append(edge_list[i][0])
                iss.add(i)
                # edge_list.pop(j)
        same.append((samee, [edge_list[i][1], edge_list[i][2]["weight"]]))
        # edge_list.pop(i)
    return same

    # graph_dict = nx.get_edge_attributes(automata_graph, "weight")
    # for edge, symbols in graph_dict.items():
    #     language += f"{edge[0]} -> {edge[1]} : {', '.join(symbols)}  ; \n"
    # language += (
    #     f"=> {', '.join(accepting_states)} ;  "
    # )
    # return language


def is_deterministic_automata(alphabet, automata_graph):
    pass


"""
-> q0 ;
q0 -> q1 : 0  ;
q0 -> q2 : a  ;
q0 -> q3 : -  ;
q1 -> q3 : 0  ;
q1 -> q4 : .  ;
q1 -> q6 : E, e  ;
q2 -> q3 : [1-9]  ;
q2 -> q2 : [0-9]  ;
q2 -> q4 : .  ;
q2 -> q6 : E, e  ;
q3 -> q6 : w  ;
q4 -> q5 : y  ;
q4 -> q6 : yt  ;
q5 -> q5 : [0-9]  ;
q5 -> q6 : E, e  ;
q6 -> q7 : -, +  ;
q6 -> q8 : [0-9]  ;
q7 -> q8 : [0-9]  ;
q8 -> q8 : [0-9]  ;
=> q5, q8, q1, q2 ;

"""
