# Cheat_Clipper

This script monitors the clipboard for new content and sends it to the GPT-4o-mini model for processing. The response is then copied back to the clipboard when `Ctrl+x` Pressed. Additionally, the script can be terminated using a hotkey (`Ctrl+B`).

## Prerequisites

- Python 3.6+
- OpenAI API Key
- Required Python packages: `openai`, `pyperclip`, `python-dotenv`, `keyboard`

## Installation

1. **Clone the repository**:

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your OpenAI API key**:
    - Create a `.env` file in the root directory of the project.
    - Add your OpenAI API key to the `.env` file:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage

You can run the application in two ways:

### Standard Mode
1. **Run the script directly**:
    ```sh
    python main.py
    ```

### Hidden Mode (Recommended)
You have two options to run the application in hidden mode:

1. Using VBScript (Recommended):
   - **Double-click** `run_hidden.vbs` to start the application
   - This method ensures the application runs completely hidden

2. Using Command Script:
   - **Double-click** `run_hidden.cmd` to start the application
   - This is an alternative method if VBScript doesn't work on your system

### Operation
- Copy any text you want to get an answer for
- Press `Ctrl+X` to get the AI response (it will automatically replace your clipboard content)
- Paste anywhere to see the answer
- Press `Ctrl+B` to terminate the application
