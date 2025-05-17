from pyrogram import Client, filters
from pyrogram.types import Message

# >>> O'ZINGIZNING API MA'LUMOTLARINGIZNI QO'YING
API_ID = 13064636     # <-- bu yerga api_id (my.telegram.org)
API_HASH = "42eb9677330d23211ff7397d0a446333"
BOT_TOKEN = "7223441901:AAFFL4-sqarL-JptCoQhTqiqgw8eVRW99Ik"

# >>> FAQAT BIR GURUHDA ISHLASH UCHUN GROUP ID
ALLOWED_GROUP_ID = -1002645346805  # <-- Guruh ID ni shu yerga yozing

app = Client("service_cleaner_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Faqat service xabarlar va faqat bir guruh uchun
@app.on_message(filters.group & filters.service)
def delete_service_messages(client: Client, message: Message):
    if message.chat.id == ALLOWED_GROUP_ID:
        try:
            message.delete()
        except:
            pass  # jim turadi, hatolik bo‘lsa ham

print("ishga tushdi")
app.run()
