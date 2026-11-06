from graphviz import Digraph

def create_diagram(fsm_data):

    dot = Digraph()

    # Diagram layout
    dot.attr(
        rankdir="LR",
        bgcolor="white",
        splines="true",
        nodesep="0.8",
        ranksep="1.0"
    )

    # General node style
    dot.attr(
        "node",
        fontname="Arial",
        fontsize="12",
        style="filled",
        color="black"
    )

    # General arrow style
    dot.attr(
        "edge",
        fontname="Arial",
        fontsize="10",
        color="#444444",
        arrowsize="0.8"
    )

    # Starting point
    dot.node(
        "start",
        shape="none",
        label=""
    )

    initial = fsm_data["initial_state"]

    # Create states
    for state in fsm_data["states"]:

        if state == initial:
            dot.node(
                state,
                label=state,
                shape="doublecircle",
                fillcolor="#B7E4C7"
            )

        else:
            dot.node(
                state,
                label=state,
                shape="circle",
                fillcolor="#DDEBFF"
            )

    # Arrow to initial state
    dot.edge("start", initial)

    # Create transitions
    for transition in fsm_data["transitions"]:

        dot.edge(
            transition["from"],
            transition["to"],
            label=transition["input"]
        )

    return dot