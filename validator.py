def validate_fsm(fsm_data):

    errors = []

    states = fsm_data.get("states", [])
    initial_state = fsm_data.get("initial_state")
    transitions = fsm_data.get("transitions", [])

    # Check whether states exist
    if not states:
        errors.append("No states found.")

    # Check initial state
    if initial_state not in states:
        errors.append("Initial state is not present in the states list.")

    # Check transitions
    for transition in transitions:

        from_state = transition.get("from")
        to_state = transition.get("to")
        condition = transition.get("input")

        if from_state not in states:
            errors.append(f"Unknown source state: {from_state}")

        if to_state not in states:
            errors.append(f"Unknown destination state: {to_state}")

        if not condition:
            errors.append("A transition has no input condition.")

    return errors
