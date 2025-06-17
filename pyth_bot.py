from telethon import TelegramClient, events
import asyncio

# بياناتك
API_ID = 22661243
API_HASH = 'd3944bacb412c21cc38eb937e1783102'
BOT_TOKEN = '7327084107:AAFgUyYg1x2DhPQWhiQIm12oTZ_wqW-9Tls'
OWNER_ID = 7964982474  # ID تبعك (رقم ياسمين)

# الكلمات اللي تبي تراقبها
KEYWORDS = ['عاجل', 'مساعدة', 'معتصم', 'حل واجب', 'مشروع', 'صيدلة', 'حاسوب', 'معلوماتية']

# تشغيل البوت
bot = TelegramClient('filterbot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage())
async def filter_messages(event):
    text = event.raw_text.lower()

    if any(keyword in text for keyword in KEYWORDS):
        try:
            sender = await event.get_sender()
            chat = await event.get_chat()
            msg_link = None

            # إذا الجروب فيه يوزر نيم عام، بنقدر نولد رابط
            if hasattr(chat, 'username'):
                msg_link = f"https://t.me/{chat.username}/{event.id}"

            alert = f"📌 تم رصد رسالة تحتوي على كلمة مهمة!\n"
            alert += f"👤 المرسل: {getattr(sender, 'first_name', 'غير معروف')}\n"
            alert += f"🗨 المحتوى:\n{text[:500]}\n"
            if msg_link:
                alert += f"\n🔗 الرابط: {msg_link}"

            await bot.send_message(OWNER_ID, alert)

        except Exception as e:
            print("❌ خطأ:", e)

print("🤖 البوت الآن يعمل ويراقب الرسائل...")
bot.run_until_disconnected()
