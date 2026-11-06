import streamlit as st
from ai_processor import generate_fsm
from diagram_generator import create_diagram
from validator import validate_fsm

st.title("AI-Based FSM State Diagram Generator")

st.write("Enter a system description to generate its FSM diagram.")

description = st.text_area(
    "Enter your system description:"
)

if st.button("Generate FSM"):

    if description.strip() == "":
        st.warning("Please enter a system description.")

    else:
        try:
            with st.spinner("Generating FSM..."):

                fsm_data = generate_fsm(description)

                errors = validate_fsm(fsm_data)

            if errors:
                st.error("FSM validation failed.")

                for error in errors:
                    st.error(error)

            else:
                diagram = create_diagram(fsm_data)

                st.success("FSM generated successfully!")

                st.subheader("Generated FSM Diagram")

                st.graphviz_chart(diagram)

                # Convert diagram into PNG
                png_data = diagram.pipe(format="png")

                # Download button
                st.download_button(
                    label="Download FSM Diagram",
                    data=png_data,
                    file_name="fsm_diagram.png",
                    mime="image/png"
                )

                st.subheader("FSM Details")
                st.json(fsm_data)

        except Exception as e:
            st.error(f"Error: {e}")