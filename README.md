# X-Reports

A powerful desktop application for analyzing CTF (Capture The Flag) writeups using local LLMs (Large Language Models). Built with PySide6.

## ⭐ Features  
### 📁 Writeup Management  
- Automatic indexing of CTF writeups from the Reports/ directory
- Tree view navigation through all report files
- Markdown support with syntax highlighting
- Metadata extraction from report.md files: title, CTF name, challenge, date, tags, etc.
- Multi-format support: .md, .txt, .py, .sh, .c, .cpp, .json, .xml, images, etc.

### 🤖 Local LLM Integration
- Ollama backend support for running models locally
- Multiple model support - you can choose your model for Ollama
- Context-aware analysis using local writeup files
- Conversation history tracking
- Smart prompting optimized for CTF analysis

### 🌐 Web Search Capabilities
- DuckDuckGo integration (no API keys required!)
- Configurable search depth
- Two search modes: before or after local analysis
- Rich search results with titles, snippets, and links

### ⚙️ Customization
- Persistent settings in settings.json
- Dark/Light theme support
- Ollama connection configuration
- Model selection from available Ollama models
- Search engine preferences

## 🖥️ System Requirements
Minimum (without LLM usage)
- OS: Windows 10/11, Linux, or macOS
- RAM: 4 GB
- Storage: 1 GB free space
- Python: 3.11

**Using LLM requires additional resources!**

## 🚀 Installation & Running
Prerequisites
- Python: 3.11
- Ollama: Latest version
- Git: For cloning the repository

Prepare Writeups Structure
```
Reports/
├── R-0001-cool-challenge/
│   ├── report.md           # Required: main writeup file
│   ├── exploit.py          # Optional: exploit scripts
│   └── notes.txt           # Optional: additional files
├── R-0002-web-hack/
│   ├── report.md
│   └── payloads.txt
└── ...
```

Installation:
```shell
# Clone repository
git clone https://github.com/g-vinokurov/X-Reports.git
cd X-Report

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt
```

Run:
```
python main.py
```
