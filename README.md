# ✂️ Cheat_Clipper

**Cheat_Clipper** is a lightweight Python utility that enhances your clipboard workflow by integrating with OpenAI's GPT-3.5-turbo model. It monitors clipboard activity, processes the content via GPT, and allows quick response retrieval with custom hotkeys. Ideal for research, note-taking, and fast knowledge lookup.

> 😉 **Educational Tool Disclaimer**: While this Cheat tool can assist with learning and research, please use it responsibly and in accordance with your institution's academic integrity policies!

---

## 🔧 Features

- Monitors clipboard content in real-time
- Sends copied text to OpenAI's GPT-3.5-turbo for processing
- Replaces clipboard content with AI response on `Ctrl+X`
- Terminates safely with `Ctrl+B`
- Optional hidden mode execution for seamless background operation

---

## 📦 Prerequisites

- Python 3.6 or later
- OpenAI API Key
- Python packages:
  - `openai`
  - `pyperclip`
  - `python-dotenv`
  - `keyboard`

---

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/K-B-R-S-W/Cheat_Clipper.git
   cd Cheat_Clipper
   ```

2. **(Optional) Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   # source venv/bin/activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your OpenAI API key**:
   - Create a `.env` file in the root directory
   - Add your API key:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

---

## ⚙️ Usage

You can launch the tool in either standard or hidden mode.

### ▶️ Standard Mode

Run the script directly:
```bash
python main.py
```

### 🕵️ Hidden Mode (Recommended)

**Option 1: VBScript (Fully Hidden)**
- Double-click `run_hidden.vbs` — the script runs silently in the background

**Option 2: CMD Script (Minimized Window)**
- Double-click `run_hidden.cmd` — useful if VBScript is unsupported

---

## ⌨️ Controls

- **Ctrl+X** → Sends current clipboard content to GPT and replaces it with the AI's response
- **Ctrl+B** → Safely terminates the program

---

## 🧠 Use Cases

- Cheat in exams😉
- Quick research assistance
- Draft generation for reports or assignments
- Real-time content summarization
- Code explanation or snippet improvement

---

## 📮 Support

**📧 Email:** [k.b.ravindusankalpaac@gmail.com](mailto:k.b.ravindusankalpaac@gmail.com)  
**🐞 Bug Reports:** [GitHub Issues](https://github.com/K-B-R-S-W/Cheat_Clipper_V1/issues)  
**📚 Documentation:** See the project [Wiki](https://github.com/K-B-R-S-W/Cheat_Clipper_V1/wiki)  
**💭 Discussions:** Join the [GitHub Discussions](https://github.com/K-B-R-S-W/Cheat_Clipper_V1/discussions)

---

## ⭐ Support This Project

If you find this project helpful, please consider giving it a **⭐ star** on GitHub!

---

## ⚠️ Disclaimer

This tool requires an active OpenAI API key and will consume API credits based on usage. Please monitor your API usage to avoid unexpected charges.
