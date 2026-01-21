import telebot
from telebot import types

TOKEN = '8379919670:AAEalyRbbUAMAthKoamVSPhs2K01ALKQHX0'
bot = telebot.TeleBot(TOKEN)
ADMIN_ID = 5476313175 # ID-и ту барои хисобот

# Истинодҳои бозиҳои HTML (инҳо ройгонанд)
GAMES = {
    "snake": "https://poki.com/en/g/blocky-snake",
    "space": "https://poki.com/en/g/space-major-minor",
    "tetris": "https://poki.com/en/g/tetris",
    "racing": "https://poki.com/en/g/extreme-off-road-cars"
}

@bot.message_handler(commands=['start'])
def start(message):
    # Хисобот ба ту
    bot.send_message(ADMIN_ID, f"🔔 {message.from_user.first_name} ботро фаъол кард!")
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("🐍 Кирмак (Snake)")
    btn2 = types.KeyboardButton("🚀 Ҷанги Космосӣ")
    btn3 = types.KeyboardButton("🧩 Тетриси HTML")
    btn4 = types.KeyboardButton("🏎️ Пойга (Racing)")
    btn5 = types.KeyboardButton("🎁 ПРИЗ-И МАХСУС")
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    bot.send_message(message.chat.id, "Салом! Яке аз бозиҳои HTML-ро интихоб кун ё Призро бигир! 🔥", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == "🐍 Кирмак (Snake)":
        bot.send_message(message.chat.id, f"Марҳамат, бозии Кирмак: {GAMES['snake']}")
    
    elif message.text == "🚀 Ҷанги Космосӣ":
        bot.send_message(message.chat.id, f"Ба пеш, ҷанговар! {GAMES['space']}")
        
    elif message.text == "🧩 Тетриси HTML":
        bot.send_message(message.chat.id, f"Тетриси классикӣ: {GAMES['tetris']}")
        
    elif message.text == "🏎️ Пойга (Racing)":
        bot.send_message(message.chat.id, f"Суръатро ҳис кун: {GAMES['racing']}")
        
    elif message.text == "🎁 ПРИЗ-И МАХСУС":
        msg = bot.send_message(message.chat.id, "🔐 Барои гирифтани приз номатро навис:")
        bot.register_next_step_handler(msg, send_prize)

def send_prize(message):
    name = message.text
    bot.send_message(message.chat.id, f"Раҳмат, {name}! Ҳозир призи туро тайёр мекунам...")
    
    # Эффекти Ваууу (Коди HTML бо эффекти неон)
    wow_code = f"""
    <div style="background: black; padding: 20px; border: 5px solid neonblue;">
        <h1 style="color: cyan; text-shadow: 0 0 20px blue;">ВАУУУ! {name}</h1>
        <p style="color: white;">Ту беҳтарин HTML CODER ҳастӣ!</p>
        <video autoplay loop style="width: 100%;">
            <source src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXN4Z3JueXN4Z3JueXN4/3o7TKVUn7iM8FMEU24/giphy.gif">
        </video>
    </div>
    """
    
    bot.send_message(message.chat.id, "🌟 ИНҶОРО БИН! ЭФФЕКТИ ВАУУУ:")
    bot.send_message(message.chat.id, f"```html\n{wow_code}\n```", parse_mode="Markdown")
    bot.send_message(message.chat.id, "Ин кодро дар браузери худ санҷ! 😉")
    
    # Хисобот ба ту
    bot.send_message(ADMIN_ID, f"💰 {name} призи худро гирифт!")

bot.polling(none_stop=True)
