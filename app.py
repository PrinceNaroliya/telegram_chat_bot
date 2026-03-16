import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

chat_memory = [
    ("system", "You are a helpful assistant. You have to make good conversation with the user and reply the user in good way.")
]

async def handle_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_reply = update.message.text

    user_id = update.effective_chat.id
    file_path = f"chat_{user_id}.txt"

    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

    try:
        history = ""
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                history = file.read()

        full_prompt = f"{history}\nUser: {user_reply}\nAI:"

        result = model.invoke(full_prompt)
        ai_text = result.content

        with open(file_path, "a") as file:
            file.write(f"User: {user_reply}\n")
            file.write(f"AI: {ai_text}\n")

        await update.message.reply_text(ai_text)

    except Exception as e:
        print(f"Bhai error aa gaya: {e}")
        await update.message.reply_text("Kuch toh gadbad hai!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(os.getenv("token")).build()
    
    msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_msg)
    app.add_handler(msg_handler)
    
    print("Bot is working... AI Brain Connected!")
    app.run_polling()