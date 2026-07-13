# 🌌 AI Multiverse Chatbot

An interactive AI chatbot built with Streamlit and Google Gemini AI that allows users to chat with multiple AI personalities while maintaining conversation memory using Streamlit Session State.

## 🚀 Features

### 🤖 Multiple AI Personalities

- Teacher
- Programmer
- Motivator
- Comedian
- AI Engineer

### 💬 Chat Features

- Interactive Chat Interface
- Streamlit Native Chat UI (`st.chat_input`)
- Conversation Memory Vault (`st.session_state`)
- Persistent Chat History During Session
- Save Chat Feature
- Load Previously Saved Chats
- New Chat Option
- Clear Current Chat

### 🧠 AI Powered

- Powered by Google Gemini AI
- Context-Aware Conversations
- Real-Time AI Responses

### 🎨 User Experience

- Clean Streamlit Interface
- Sidebar Controls
- Chat History Viewer
- Personality Switching Without Losing History

### 🔒 Security

- Secure API Key Management using `.env`

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- python-dotenv

---

## 📂 Project Structure

```text
AI_Multiverse_Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/saro0923/AI-Multiverse-Chatbot.git
cd AI-Multiverse-Chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API Key

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your API key from:

https://aistudio.google.com/

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 🧠 Memory Vault (Assignment 3)

This project uses Streamlit Session State to maintain conversation history.

```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

Features:

- Stores User Messages
- Stores AI Responses
- Maintains Chat History Across Reruns
- Preserves History While Changing Personalities
- Displays Previous Messages Automatically

---

## 📸 Application Features

### Sidebar

- Personality Selector
- New Chat
- Save Chat
- Saved Chats
- Memory Vault Viewer
- Clear Current Chat

### Chat Area

- User Messages
- AI Responses
- Conversation History

---

## 🎯 Use Cases

- Learning and Education
- Programming Assistance
- AI & Machine Learning Guidance
- Career Guidance
- Motivation and Productivity
- Entertainment and Fun Conversations

---

## 🔮 Future Enhancements

- Voice Input Support
- Chat Export to PDF
- Database Storage for Chats
- Dark Mode
- Multi-language Support
- User Authentication

---

## 👨‍💻 Author

**Saravanan S**

LinkedIn:
https://www.linkedin.com/in/saravanan2311/

---

## 📄 License

This project was developed as part of the MirAI School of Technology – Virtual Summer Internship 2026 and is intended for educational and learning purposes.