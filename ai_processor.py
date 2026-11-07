
from dotenv import load_dotenv
from google import genai
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_fsm(description):

    prompt = f"""
    You are an FSM (Finite State Machine) expert.

    Read the following system description and identify:

    1. All states
    2. Initial state
    3. Final states, if any
    4. Transitions between states
    5. Input or condition for each transition

    Return the result ONLY as valid JSON in this format:

    {{
        "states": ["State1", "State2"],
        "initial_state": "State1",
        "final_states": ["State2"],
        "transitions": [
            {{
                "from": "State1",
                "to": "State2",
                "input": "Condition"
            }}
        ]
    }}

    If there are no final states, return an empty list.

    System description:
    {description}
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return json.loads(response.text)
