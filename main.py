from openai import OpenAI
import pyperclip
import time
import os
import keyboard
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging to discard messages
logging.basicConfig(filename=os.devnull, level=logging.ERROR)

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    base_url="https://api.openai.com/v1",
)

def get_gpt4o_mini_answer(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant who gives concise and accurate answers. If presented with multiple-choice questions, simply provide the correct answer. For any type of question, including math, just give the best short answer based on the context, without unnecessary explanation. Just give text, don't style the text. Please do not use any formatting elements like **, ###, or bullet points. Instead, use plain text. Provide the answer in a simple and straightforward manner, without any styled text. If you are working on a math question, provide the steps and the final answer without any explanation. No additional commentary is needed, just the steps and the answer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=500,
            temperature=0.2
        )
        return response.choices[0].message.content.strip() if response.choices else "No response generated."
    except Exception as e:
        error_message = f"Error in generating response: {str(e)}"
        logging.error(f"Detailed error: {repr(e)}")
        if 'Connection' in str(e):
            return "Error: Unable to connect to the API. Please check your internet connection and proxy settings."
        return error_message

def process_clipboard():
    global latest_clipboard
    if not latest_clipboard:  # Use the globally tracked clipboard content
        return
    try:
        answer = get_gpt4o_mini_answer(latest_clipboard)
        pyperclip.copy(answer)
        latest_clipboard = answer  # Update the latest clipboard with the answer
    except Exception as e:
        logging.error(f"Error in process_clipboard: {e}")

def handle_cut():
    # Get selected text and copy it
    keyboard.send('ctrl+c')
    time.sleep(0.1)  # Wait for clipboard to update
    # Store the text that was copied
    text_to_process = pyperclip.paste().strip()
    if text_to_process:
        # Delete the selected text (simulate cut)
        keyboard.send('delete')
        # Process the text
        answer = get_gpt4o_mini_answer(text_to_process)
        # Update clipboard with answer
        pyperclip.copy(answer)

def monitor_clipboard():
    global latest_clipboard
    last_clipboard = ""
    latest_clipboard = ""

    # Add global hotkey for cut operation
    keyboard.on_press_key('x', lambda _: handle_cut() if keyboard.is_pressed('ctrl') else None, suppress=True)

    while True:
        time.sleep(0.1)  # Check clipboard frequently
        try:
            current_clipboard = pyperclip.paste().strip()
            if current_clipboard and current_clipboard != last_clipboard:
                last_clipboard = current_clipboard
                latest_clipboard = current_clipboard
        except:
            pass  # Ignore any clipboard access errors

def terminate_script():
    try:
        # Clear clipboard
        pyperclip.copy("")
        # Get current process ID
        current_pid = os.getpid()
        # Kill all Python processes except the current one
        os.system(f'wmic process where "name like \'%python%\' and processid!={current_pid}" call terminate >nul 2>&1')
        # Kill cmd processes that might be running our scripts
        os.system('wmic process where "name=\'cmd.exe\' and commandline like \'%run_hidden%\'" call terminate >nul 2>&1')
        # Kill wscript processes that might be running our VBS
        os.system('wmic process where "name=\'wscript.exe\' and commandline like \'%run_hidden%\'" call terminate >nul 2>&1')
    finally:
        # Force exit the current process
        os._exit(0)

if __name__ == "__main__":
    pyperclip.copy("")
    # Register global hotkeys
    keyboard.on_press_key('b', lambda _: terminate_script() if keyboard.is_pressed('ctrl') else None, suppress=True)
    try:
        monitor_clipboard()
    except Exception as e:
        logging.error(f"Error in main loop: {e}")
        terminate_script()
