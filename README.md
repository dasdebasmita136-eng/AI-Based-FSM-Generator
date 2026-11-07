# AI-Based FSM State Diagram Generator

## Project Overview

The AI-Based FSM State Diagram Generator is a Python-based application that converts plain-English system descriptions into Finite State Machine (FSM) representations and visual state diagrams.

It uses Google's Gemini AI to identify states, initial states, final states and transitions from natural-language descriptions. The generated FSM is then validated and visualized using Graphviz.

## Features

- **Natural Language Input:** Enter system descriptions in plain English.
- **AI-Based FSM Generation:** Uses Gemini AI to identify FSM states and transitions.
- **FSM Validation:** Checks the generated FSM for structural errors.
- **State Diagram Visualization:** Generates diagrams using Graphviz.
- **Sample Scenarios:** Includes Traffic Light, Vending Machine, Automatic Door and Login System examples.
- **Custom Input:** Supports user-defined system descriptions.
- **Download Options:** Download generated diagrams as PNG and FSM data as JSON.
- **Error Handling:** Displays understandable messages for invalid inputs and unexpected responses.

## Technologies Used

- Python
- Google Gemini API
- Streamlit
- Graphviz
- Python Graphviz package
- JSON
- python-dotenv

## Project Architecture

The application consists of the following modules:

1. **app.py:** Provides the Streamlit user interface and coordinates the application.
2. **ai_processor.py:** Sends natural-language descriptions to Gemini and receives structured FSM data.
3. **validator.py:** Checks the structure and validity of generated FSM data.
4. **diagram_generator.py:** Converts FSM data into a visual state diagram using Graphviz.

## Working Methodology

1. The user selects a sample scenario or enters a custom system description.
2. The description is sent to the Gemini AI model.
3. Gemini identifies the states, initial state, final states and transitions.
4. The response is converted into structured JSON data.
5. The validator checks the generated FSM structure.
6. If validation succeeds, Graphviz generates the FSM diagram.
7. The user can view and download the diagram and JSON data.

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/dasdebasmita136-eng/AI-Based-FSM-Generator.git
```

### 2. Open the project folder

```bash
cd AI-Based-FSM-Generator
```

### 3. Install dependencies

```bash
pip install streamlit google-genai graphviz python-dotenv
```

### 4. Configure the Gemini API key

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own Gemini API key.

Do not upload your `.env` file to GitHub.

### 5. Run the application

```bash
python -m streamlit run app.py
```

## Testing

The application has been tested using different scenarios:

| Test Scenario | Expected Result |
|---|---|
| Traffic Light | Three states and cyclic transitions |
| Vending Machine | Three states and corresponding transitions |
| Automatic Door | Closed and Open states |
| Login System | Login success and failure transitions |
| Washing Machine | Five states and sequential transitions |
| Invalid input | Validation error instead of an FSM diagram |
| Custom machine description | Correct FSM generation |
| PNG download | Diagram downloaded successfully |
| JSON download | FSM data downloaded successfully |

## Limitations

- The application uses an existing Gemini generative AI model rather than training a custom sequence-to-sequence model.
- Generated FSM accuracy depends on the clarity and completeness of the input description.
- Structural validation does not guarantee complete semantic correctness.
- Internet connectivity and a working Gemini API key are required for AI generation.

## Future Scope

- Improve semantic validation of generated transitions.
- Support more complex FSM descriptions.
- Add additional diagram customization options.
- Explore custom-trained sequence-to-sequence models.

## Conclusion

The project demonstrates how natural-language processing and AI can simplify the creation of Finite State Machines. It converts plain-English descriptions into structured FSM data and visual diagrams, making FSM design more accessible and efficient.