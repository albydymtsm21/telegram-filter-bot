from telethon import TelegramClient, events
import asyncio

# بيانات الدخول
API_ID = 22661243
API_HASH = 'd3944bacb412c21cc38eb937e1783102'
BOT_TOKEN = '7327084107:AAFgUyYg1x2DhPQWhiQIm12oTZ_wqW-9Tls'
OWNER_ID = 7964982474  # رقم المستخدم (مثلاً حساب منال)

# الكلمات اللي تبي تراقبها
KEYWORDS = [
    'أحد يساعدني', 'تعرفون احد', 'في احد يقدر', 'مين يعرف', 'مين يسوي',
    'ابغى شرح', 'ابغى احد يشرح', 'ابي احد يسوي', 'يبغى احد', 'يحل واجب',
    'يسوي مشروع', 'يسوي سيفي', 'يسوي cv', 'يساعدني بحل', 'محتاج شرح',
    'ممكن شرح', 'احتاج مساعده', 'في احد هنا يشرح', 'في احد يسوي',
    'تسويلي واجب', 'تشرحون لي', 'احد فاهم', 'ممكن احد يحل', 'حد يعرف يسوي',
    'احد يعرف يساعد', 'احد ينفذ لي', 'ممكن تسويلي', 'مين يقدر يشرح',
    'ممكن احد يسوي', 'تقدر تسوي لي', 'مين يقدر يساعدني', 'مين يحل',
    'مين يسوي بحث', 'مين يشرح مادة', 'محتاج مساعدة', 'ابي مساعدة',
    'ابي احد فاهم', 'ابي حلول', 'ابغى حلول واجب', 'ممكن حل', 'حل ذا',
    'مين عنده خبره', 'من يساعدني', 'حلوا لي', 'ممكن خدمة', 'ممكن تسوون لي',
    'تكفون شرح', 'في احد ينفذ', 'احد يشرح', 'ابغى احد يسوي', 'يشرحون',
    'تعرفون احد يسوي'
]

# تشغيل البوت
bot = TelegramClient('filterbot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage())
async def filter_messages(event):
    try:
        text = event.raw_text
        if any(keyword in text for keyword in KEYWORDS):
            sender = await event.get_sender()
            chat = await event.get_chat()
            msg_link = None

            if hasattr(chat, 'username') and chat.username:
                msg_link = f"https://t.me/{chat.username}/{event.id}"

            alert = "📌 **تم رصد رسالة تحتوي على كلمة مهمة!**\n"
            alert += f"👤 **المرسل:** {getattr(sender, 'first_name', 'غير معروف')}"
            if getattr(sender, 'username', None):
                alert += f" (@{sender.username})"
            alert += f"\n🗨 **المحتوى:**\n{text[:1000]}"
            if msg_link:
                alert += f"\n\n🔗 [رابط الرسالة]({msg_link})"

            await bot.send_message(OWNER_ID, alert, link_preview=False)

    except Exception as e:
        print("❌ خطأ:", e)

if __name__ == '__main__':
    print("🤖 البوت الآن يعمل ويراقب الرسائل...")
    bot.run_until_disconnected()
