
def validate_fsm(fsm_data):

    errors = []

    # 1. Check overall FSM format
    if not isinstance(fsm_data, dict):
        return ["Invalid FSM format. Expected a dictionary."]

    states = fsm_data.get("states")
    initial_state = fsm_data.get("initial_state")
    final_states = fsm_data.get("final_states", [])
    transitions = fsm_data.get("transitions")

    # 2. Check states
    if not isinstance(states, list):
        return ["Invalid states format. Expected a list."]

    if not states:
        errors.append("No states found.")

    # Check state names
    for state in states:
        if not isinstance(state, str) or not state.strip():
            errors.append("State names must be non-empty strings.")

    valid_states = [
        state for state in states
        if isinstance(state, str) and state.strip()
    ]

    # Check duplicate states
    normalized_states = [
        state.strip().lower() for state in valid_states
    ]

    if len(normalized_states) != len(set(normalized_states)):
        errors.append("Duplicate state names found.")

    # 3. Check initial state
    if not isinstance(initial_state, str) or not initial_state.strip():

        errors.append("Initial state is missing or invalid.")

    elif initial_state not in states:

        errors.append(
            f"Initial state '{initial_state}' is not present in the states list."
        )

    # 4. Check final states
    if not isinstance(final_states, list):

        errors.append("Final states must be provided as a list.")

    else:

        for state in final_states:

            if state not in states:
                errors.append(
                    f"Final state '{state}' is not present in the states list."
                )

    # 5. Check transitions format
    if not isinstance(transitions, list):

        errors.append("Transitions must be provided as a list.")
        return errors

    # IMPORTANT: An FSM must have at least one transition
    if len(transitions) == 0:

        errors.append(
            "No transitions found. Please provide a meaningful "
            "system description containing states and transitions."
        )

        return errors

    # 6. Check individual transitions
    seen_transitions = set()

    for index, transition in enumerate(transitions):

        if not isinstance(transition, dict):

            errors.append(
                f"Transition {index + 1} has an invalid format."
            )
            continue

        from_state = transition.get("from")
        to_state = transition.get("to")
        condition = transition.get("input")

        # Check source state
        if not isinstance(from_state, str) or not from_state.strip():

            errors.append(
                f"Transition {index + 1} has a missing source state."
            )

        elif from_state not in states:

            errors.append(
                f"Unknown source state: {from_state}"
            )

        # Check destination state
        if not isinstance(to_state, str) or not to_state.strip():

            errors.append(
                f"Transition {index + 1} has a missing destination state."
            )

        elif to_state not in states:

            errors.append(
                f"Unknown destination state: {to_state}"
            )

        # Check transition condition
        if not isinstance(condition, str) or not condition.strip():

            errors.append(
                f"Transition {index + 1} has no valid input condition."
            )

        # Check duplicate transitions
        if (
            isinstance(from_state, str)
            and isinstance(to_state, str)
            and isinstance(condition, str)
        ):

            transition_key = (
                from_state.strip().lower(),
                to_state.strip().lower(),
                condition.strip().lower()
            )

            if transition_key in seen_transitions:

                errors.append(
                    f"Duplicate transition found: "
                    f"{from_state} → {to_state}."
                )

            seen_transitions.add(transition_key)

    return errors
