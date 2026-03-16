# Telegram Chat Bot 🤖

A professional-grade Telegram bot integrated with **Groq AI (Llama 3.3)**. This bot features **persistent per-user memory**, ensuring private and contextual conversations for every user.

## ✨ Key Features
* **AI-Powered:** Uses `llama-3.3-70b-versatile` via Groq for high-speed, intelligent responses.
* **Per-User Memory:** Automatically creates unique `.txt` files for every user to maintain chat history independently.
* **Asynchronous Architecture:** Built with `python-telegram-bot` (AsyncIO) to handle multiple users simultaneously without lag.
* **Secure:** Implementation of `.gitignore` to protect sensitive API keys and local user data.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** `python-telegram-bot`
* **LLM Orchestration:** `LangChain` / `LangChain-Groq`
* **Inference Engine:** Groq Cloud API

## 🚀 Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/PrinceNaroliya/telegram_chat_bot.git](https://github.com/PrinceNaroliya/telegram_chat_bot.git)
   cd telegram_chat_bot

2. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependies**
    ```bash
    pip install -r requirements.txt

4. **Environment Variable:**
    Create a .env file and add your credentials:

    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    GROQ_API_KEY=your_groq_api_key

5. **Run the Bot:**
    ```bash
    python app.py

## 📂 Project Structure
* **app.py:** Main bot logic and message handlers.

* **.env:** Secret keys (not tracked by Git).

* **.gitignore:** Prevents sensitive files and logs from being uploaded.

* **chat_{user_id}.txt:** Auto-generated persistent storage for user conversations.

___