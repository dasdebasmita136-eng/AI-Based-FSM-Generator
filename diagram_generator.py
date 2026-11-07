
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

    # Starting point as a small black dot
    dot.node(
        "start",
        shape="point",
        width="0.15",
        height="0.15",
        fillcolor="black"
    )

    initial = fsm_data["initial_state"]
    final_states = fsm_data.get("final_states", [])

    # Traffic light colours
    traffic_colors = {
        "red": "#FF6666",
        "green": "#66CC66",
        "yellow": "#FFD966"
    }

    state_names = [state.lower() for state in fsm_data["states"]]

    is_traffic_light = all(
        color in state_names
        for color in traffic_colors
    )

    # Create FSM states
    for state in fsm_data["states"]:

        # Traffic light states
        if is_traffic_light and state.lower() in traffic_colors:

            dot.node(
                state,
                label=state,
                shape="doublecircle" if state in final_states else "circle",
                fillcolor=traffic_colors[state.lower()]
            )

        # Initial state
        elif state == initial:

            dot.node(
                state,
                label=state,
                shape="doublecircle" if state in final_states else "circle",
                fillcolor="#B7E4C7"
            )

        # Final states
        elif state in final_states:

            dot.node(
                state,
                label=state,
                shape="doublecircle",
                fillcolor="#FFE2B8"
            )

        # Normal states
        else:

            dot.node(
                state,
                label=state,
                shape="circle",
                fillcolor="#CDE7FF"
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
