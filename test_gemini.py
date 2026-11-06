
from ai_processor import generate_fsm
from diagram_generator import create_diagram

description = """
A traffic light starts with Red.
After 30 seconds, it changes to Green.
After 25 seconds, it changes to Yellow.
After 5 seconds, it returns to Red.
"""

# Step 1: Get FSM data from Gemini
fsm_data = generate_fsm(description)

# Step 2: Generate the diagram
diagram = create_diagram(fsm_data)

# Step 3: Save the diagram as an image
diagram.render("traffic_light_fsm", format="png", cleanup=True)

print("FSM diagram generated successfully!")
