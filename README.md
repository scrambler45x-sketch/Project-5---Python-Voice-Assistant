# 🎤 Python Voice Assistant

A simple Python-based Voice Assistant built using Flask, Speech Recognition, and Text-to-Speech. The assistant can recognize voice commands and perform everyday tasks like opening websites, telling the time, searching Google, taking screenshots, creating notes, and more.

## Features

- Voice Recognition
- Text-to-Speech
- Tell Current Time
- Tell Current Date
- Weather Search (Google - No API Required)
- Basic Calculator
- Create Notes
- Search Google
- Open Desktop, Downloads, Documents & Pictures
- Open Notepad, Calculator & Chrome
- Play Music
- Take Screenshot
- Tell Jokes
- Exit Assistant

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- SpeechRecognition
- pyttsx3
- PyAutoGUI
- PyJokes

---

## Project Structure

VoiceAssistant/
│
├── app.py
├── weather.py
├── config.py
├── requirements.txt
├── notes.txt
│
├── templates/
│ └── index.html
│
├── static/
│ ├── style.css
│ └── script.js
│
└── screenshots/

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/voice-assistant.git
```

Go to the project directory

```bash
cd voice-assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Voice Commands

| Command | Action |
|----------|--------|
| Time | Tell current time |
| Date | Tell today's date |
| Weather in Mumbai | Opens Google Weather |
| Calculate 10 plus 5 | Calculator |
| Search Google for Python | Google Search |
| Open Google | Opens Google |
| Open YouTube | Opens YouTube |
| Open GitHub | Opens GitHub |
| Open Gmail | Opens Gmail |
| Open Notepad | Launch Notepad |
| Open Calculator | Launch Calculator |
| Open Chrome | Launch Chrome |
| Open Downloads | Open Downloads Folder |
| Open Desktop | Open Desktop Folder |
| Play Music | Play Random Music |
| Screenshot | Save Screenshot |
| Tell me a Joke | Tell a Joke |
| Bye | Exit Assistant |

---

## Future Improvements

- AI Chatbot Integration
- OpenAI API Support
- Wake Word Detection
- Weather API
- Email Support
- WhatsApp Automation
- Voice Authentication

---

