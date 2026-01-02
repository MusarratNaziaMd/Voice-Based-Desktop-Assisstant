

# Voice-Based Desktop Assistant

A **voice-enabled desktop assistant** built in Python. It allows users to interact with their computer using **voice commands** and a GUI for typing messages. The assistant can greet the user, tell the time, open websites, play music, and respond to simple queries.

---

## 📝 About

This project is designed to make everyday tasks faster and more convenient using **voice recognition** and **text-to-speech technology**. Users can **ask questions**, **give commands**, or **type messages** in the GUI, and the assistant responds intelligently.

---

## ⚡ Features

* Voice recognition using **speech-to-text**
* Text-to-speech responses using **pyttsx3**
* GUI interface with **Tkinter** and **PIL** for images
* Responds to greetings, queries, and commands
* Open **Google**, **YouTube**, or **Spotify** directly
* Provides **current time**
* Shutdown command support
* Easy-to-use **Ask / Send / Delete** interface

---

## 🖥️ Working / Platform Compatibility

* Works on **Windows 10/11**, **Linux**, and **MacOS**
* Requires a **microphone** for voice commands
* GUI is required (desktop environment)
* Internet connection is needed for opening websites or Spotify

**Example Commands:**

| Voice Command        | Response / Action                |
| -------------------- | -------------------------------- |
| "Hello"              | Assistant responds with greeting |
| "What is your name?" | Assistant introduces itself      |
| "Time now"           | Assistant speaks current time    |
| "Open YouTube"       | Launches YouTube in browser      |
| "Play Music"         | Opens Spotify music link         |
| "Shutdown"           | Exits the application            |

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone <your-repo-link>
cd Voice-Based-Desktop-Assistant
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

**Dependencies (requirements.txt):**

```
Python
SpeechRecognition
Pillow
pyttsx3
PyAudio
```

---

## 🖼️ File Structure

```
Voice-Based-Desktop-Assistant/
│
├─ action.py               # Handles commands and responses
├─ speech_to_text.py       # Voice-to-text conversion
├─ text_to_speech.py       # Text-to-speech conversion
├─ gui.py                  # GUI interface for interaction
├─ assistant.png           # Image displayed in GUI
├─ requirements.txt        # Project dependencies
└─ README.md               # Project documentation
```

---

## 🚀 Usage

1. Run the GUI:

```bash
python gui.py
```

2. Use **voice commands** by clicking **Ask**, or type a message in the input box and click **Send**.
3. Click **Delete** to clear the conversation.
4. To exit, say or type **"shutdown"**.

---

## 💡 How It Works

1. **Voice Input:** Captured via `speech_recognition`
2. **Command Processing:** Handled by `action.py`
3. **Response Generation:** Converted to speech via `pyttsx3`
4. **GUI Display:** Tkinter window shows conversation and response

---

## 🎯 Future Enhancements

* Add **AI-based natural language understanding** for more complex queries
* Integrate **calendar and reminder functionality**
* Add **offline voice command recognition**
* Include **music streaming controls**

---

## ⚠️ Notes

* Ensure **microphone permissions** are enabled
* Internet connection is required for web-based commands
* Tested on Python 3.10+

---

