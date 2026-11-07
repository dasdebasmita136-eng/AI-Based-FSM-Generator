
import streamlit as st
import json

from ai_processor import generate_fsm
from diagram_generator import create_diagram
from validator import validate_fsm


# Page configuration
st.set_page_config(
    page_title="AI-Based FSM Generator",
    page_icon="⚙️",
    layout="wide"
)


# Main heading
st.title("⚙️ AI-Based FSM Generator")

st.markdown(
    "Transform plain-English system descriptions into "
    "Finite State Machine (FSM) diagrams using Artificial Intelligence."
)

st.divider()


# Sample descriptions
examples = {
    "Traffic Light": """
    A traffic light starts with Red.
    After 30 seconds, it changes to Green.
    After 25 seconds, it changes to Yellow.
    After 5 seconds, it returns to Red.
    """,

    "Vending Machine": """
    A vending machine starts in Idle state.
    When a coin is inserted, it moves to Payment Received.
    When a product is selected, it moves to Dispensing.
    After dispensing, it returns to Idle.
    """,

    "Automatic Door": """
    An automatic door starts in Closed state.
    When a person is detected, it moves to Open.
    After the person passes, it returns to Closed.
    """,

    "Login System": """
    A login system starts in Logged Out state.
    When the user enters correct credentials, it moves to Logged In.
    When the user clicks logout, it returns to Logged Out.
    If incorrect credentials are entered, it moves to Login Failed.
    """,

    "Custom Input": ""
}


# Input section
st.subheader("📝 System Description")

st.caption(
    "Choose a sample scenario or enter your own system description."
)

selected_example = st.selectbox(
    "Choose a sample system:",
    list(examples.keys())
)

description = st.text_area(
    "Enter your system description:",
    value=examples[selected_example],
    height=180,
    key=f"description_{selected_example}"
)


# Generate button
st.divider()

generate_button = st.button(
    "✨ Generate FSM",
    type="primary",
    use_container_width=True
)


# Generate FSM
if generate_button:

    st.session_state.pop("fsm_data", None)

    if not description.strip():

        st.warning("Please enter a system description.")

    else:

        try:

            with st.spinner(
                "AI is analysing your description and generating the FSM..."
            ):

                # Generate FSM using Gemini
                fsm_data = generate_fsm(description)

                # Validate generated FSM
                errors = validate_fsm(fsm_data)

            if errors:

                st.error(
                    "Unable to generate a valid FSM. "
                    "Please enter a meaningful system description "
                    "containing identifiable states and transitions."
                )

                # Technical details available when needed
                with st.expander("View validation details"):

                    for error in errors:
                        st.write(f"• {error}")

            else:

                st.session_state["fsm_data"] = fsm_data

                st.success("FSM generated successfully!")

        except json.JSONDecodeError:

            st.error(
                "The AI returned an invalid response. "
                "Please try again with a clearer description."
            )

        except Exception as e:

            st.error(
                "Something went wrong while generating the FSM. "
                "Please try again."
            )

            with st.expander("View technical error"):
                st.code(str(e))


# Display generated results
if "fsm_data" in st.session_state:

    fsm_data = st.session_state["fsm_data"]

    st.divider()

    st.header("📊 Generated FSM")

    # FSM statistics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total States", len(fsm_data["states"]))

    with col2:
        st.metric("Total Transitions", len(fsm_data["transitions"]))

    with col3:
        st.metric(
            "Final States",
            len(fsm_data.get("final_states", []))
        )

    # Generate diagram
    diagram = create_diagram(fsm_data)

    st.subheader("FSM State Diagram")

    st.graphviz_chart(
        diagram,
        use_container_width=True
    )

    # Download section
    st.divider()

    st.subheader("⬇️ Download Your FSM")

    col1, col2 = st.columns(2)

    with col1:

        png_data = diagram.pipe(format="png")

        st.download_button(
            label="Download Diagram (PNG)",
            data=png_data,
            file_name="fsm_diagram.png",
            mime="image/png",
            use_container_width=True
        )

    with col2:

        json_data = json.dumps(
            fsm_data,
            indent=4,
            ensure_ascii=False
        )

        st.download_button(
            label="Download FSM Data (JSON)",
            data=json_data,
            file_name="fsm_data.json",
            mime="application/json",
            use_container_width=True
        )

    # FSM details
    st.divider()

    with st.expander("🔍 View FSM Details"):

        st.subheader("States")

        for state in fsm_data["states"]:
            st.write(f"• {state}")

        st.subheader("Initial State")

        st.info(fsm_data["initial_state"])

        st.subheader("Final States")

        final_states = fsm_data.get("final_states", [])

        if final_states:

            for state in final_states:
                st.write(f"• {state}")

        else:
            st.write("No final states specified.")

        st.subheader("Transitions")

        for transition in fsm_data["transitions"]:

            st.write(
                f"**{transition['from']}** → "
                f"**{transition['to']}** "
                f"({transition['input']})"
            )

        st.subheader("Complete FSM JSON")

        st.json(fsm_data)


# Footer
st.divider()

st.caption(
    "AI-Based FSM Generator | Natural Language Processing "
    "and Finite State Machine Visualization"
)
