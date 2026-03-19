# Telegram Chat Bot 🤖

# 🤖 AI Telegram Chatbot (Groq + LangChain)

An **AI-powered Telegram chatbot** that can have natural conversations with users using **Groq LLM (LLaMA 3.3 70B)**.

This bot:
- 💬 Chats like a human  
- 🧠 Remembers conversation history  
- ⚡ Uses ultra-fast Groq inference  
- 📂 Stores chat per user  

---

## 🚀 Features

✔️ Real-time AI conversation  
✔️ Per-user memory (chat history saved in files)  
✔️ Fast responses using Groq API  
✔️ Simple and minimal codebase  
✔️ Easily extendable  

---

## 🧠 How It Works

1. User sends a message on Telegram  
2. Bot retrieves previous chat history (if exists)  
3. Combines history + new message  
4. Sends to Groq LLM  
5. Returns AI response  
6. Saves conversation to file  

---

## 🛠️ Tech Stack

- **Python**
- **python-telegram-bot**
- **LangChain**
- **Groq API (llama-3.3-70b-versatile)**
- **dotenv**

---

## 📂 Project Structure

```
.
├── bot.py
├── .env
├── chat_<user_id>.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/telegram-ai-bot.git
cd telegram-ai-bot
```

---

### 2️⃣ Install Dependencies

```bash
pip install python-telegram-bot langchain langchain-groq python-dotenv
```

---

### 3️⃣ Add Environment Variables

Create `.env` file:

```
GROQ_API_KEY=your_groq_api_key
token=your_telegram_bot_token
```

---

### 4️⃣ Run the Bot

```bash
python bot.py
```

---

## 📸 Example Chat

```
User: Hello bro!
AI: Hey! 😄 Kaise ho? Aaj kya chal raha hai?

User: Tell me something interesting
AI: Did you know your brain processes information faster than any computer? 🤯
```

---

## 🧩 Core Logic

### 📌 Message Handling

- Receives user message  
- Reads chat history from file  
- Sends full prompt to LLM  

---

### 🧠 Memory System

Each user has a separate file:

```
chat_<user_id>.txt
```

Example:

```
User: Hello
AI: Hi there!

User: How are you?
AI: I'm doing great! 😄
```

---

### ⚡ LLM Integration

```python
result = model.invoke(full_prompt)
ai_text = result.content
```

---

## 💡 Why This Project is Useful

- Learn how to build real AI bots  
- Understand LLM memory handling  
- Great beginner-to-intermediate project  
- Can be extended into SaaS  

---

## 🔮 Future Improvements

- 🗄️ Database (MongoDB / Redis) instead of files  
- 🌐 Web dashboard (admin panel)  
- 🎤 Voice support  
- 🌍 Multi-language support  
- 🔒 Authentication system  
- 📊 Analytics (user engagement tracking)  

---

## ⚠️ Limitations

- File-based memory (not scalable)  
- No context limit handling  
- No rate limiting  

---

## 🤝 Contributing

Pull requests are welcome! Feel free to improve this project.

---

## ⭐ Show Some Love

If you like this project, give it a ⭐ on GitHub!

---

## 📢 Keywords (for SEO)

telegram ai bot, groq chatbot, langchain telegram bot, python chatbot, llama 3 chatbot, ai assistant telegram, conversational ai bot

___