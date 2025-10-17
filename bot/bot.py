import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '7565416664:AAHM9XmuYVhwCnS_KiMFKQ3s9P-AiBL6iBM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    welcome_text = "Здравствуйте! Добро пожаловать в бота.\n\nВыберите опцию:"
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="Поиск по ключевым словам", callback_data="option_1"))
    markup.add(InlineKeyboardButton(text="Авторская подборка", callback_data="author_selection"))
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'author_selection')
def show_author_menu(call):
    markup = InlineKeyboardMarkup()
    button_names = [
        '1. Полиция', '2. Росгвардия', '3. Маркировка', '4. Сроки годности',
        '5. Товар', '6. Охрана', '7. Подача заявления', '8. Статьи магазинов',
        '9. Статьи граждан', '10. Видеофиксация', '11. Публикация изображений', '12. Закон о защите прав', '13. Личный досмотр'
    ]
    buttons = [InlineKeyboardButton(text=name, callback_data=f"author_{name}") for name in button_names]
    for i in range(0, len(buttons), 3):
        markup.row(*buttons[i:i+3])
    markup.row(InlineKeyboardButton(text="Назад", callback_data="back_to_main"))
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'back_to_main')
def handle_back_to_main(call):
    bot.answer_callback_query(call.id)
    welcome_text = "Вы вернулись в главное меню.\n\nВыберите опцию:"
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text="Поиск по ключевым словам", callback_data="option_1"))
    markup.add(InlineKeyboardButton(text="Авторская подборка", callback_data="author_selection"))
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('author_'))
def handle_author_menu(call):
    bot.answer_callback_query(call.id)
    item = call.data.split('_', 1)[1]
    if item == 'Полиция':
        markup = InlineKeyboardMarkup()
        police_buttons = [
            ('Полиция1', 'police_1'),
            ('Полиция2', 'police_2'),
            ('Полиция3', 'police_3'),
            ('Полиция4', 'police_4'),
            ('Полиция5', 'police_5'),
            ('Полиция6', 'police_6')
        ]
        for name, callback_data in police_buttons:
            markup.add(InlineKeyboardButton(text=name, callback_data=callback_data))
        markup.row(InlineKeyboardButton(text="Назад", callback_data="back_to_author"))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif item == 'Росгвардия':
        # Создаем 4 новые кнопки для Росгвардии
        markup = InlineKeyboardMarkup()
        rg_buttons = [
            ('Росгвардия1', 'rosgvardiya_1'),
            ('Росгвардия2', 'rosgvardiya_2'),
            ('Росгвардия3', 'rosgvardiya_3'),
            ('Росгвардия4', 'rosgvardiya_4')
        ]
        for name, callback_data in rg_buttons:
            markup.add(InlineKeyboardButton(text=name, callback_data=callback_data))
        markup.row(InlineKeyboardButton(text="Назад", callback_data="back_to_author"))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif item == 'Товар':
        # Новый блок для отображения двух кнопок
        markup = InlineKeyboardMarkup()
        btn1 = InlineKeyboardButton(text="Можно ли попробовать товар до оплаты на кассе?", callback_data="good_1")
        btn2 = InlineKeyboardButton(text="Как сьесть товар и вернуть полную стоимость этого товара? ", callback_data="good_2")
        markup.add(btn1)
        markup.add(btn2)
        markup.add(InlineKeyboardButton(text="Назад", callback_data="back_to_author"))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      reply_markup=markup)

    elif item == 'Охрана':
        markup = InlineKeyboardMarkup()
        security_buttons = [
            ('6.1 Закон о частной детективной и охранной деятельности в РФ', 'sec_1'),
            ('6.2 Что грозит охраннику за отсутствие удостоверения?', 'sec_2'),
            ('6.3 Могут ли охранники досматривать сумки?', 'sec_3')
        ]
        for name, callback_data in security_buttons:
            markup.add(InlineKeyboardButton(text=name, callback_data=callback_data))
        markup.row(InlineKeyboardButton(text="Назад", callback_data="back_to_author"))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif item == 'Видеофиксация':
        markup = InlineKeyboardMarkup()
        video_buttons = [
            ('10.1 Видеофиксация граждан', 'video_1'),
            ('10.2 Видеофиксация сотрудников полиции', 'video_2'),
            ('10.3 Видеофиксация в суде', 'video_3')
        ]
        for name, callback_data in video_buttons:
            markup.add(InlineKeyboardButton(text=name, callback_data=callback_data))
        markup.row(InlineKeyboardButton(text="Назад", callback_data="back_to_author"))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    else:
        # Обработка других пунктов
        bot.send_message(call.message.chat.id, f"Вы выбрали '{item}'.")

@bot.callback_query_handler(func=lambda call: call.data.startswith('police_'))
def handle_police_menu(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Вы выбрали {call.data}")

@bot.callback_query_handler(func=lambda call: call.data.startswith('rosgvardiya_'))
def handle_rosgvardiya_menu(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Вы выбрали {call.data}")

@bot.callback_query_handler(func=lambda call: call.data.startswith('good_'))
def handle_goods(call):
    bot.answer_callback_query(call.id)
    if call.data == 'good_1':
        bot.send_message(call.message.chat.id, "1 Пункт")
    elif call.data == 'good_2':
        bot.send_message(call.message.chat.id, "2 Пункт")

@bot.callback_query_handler(func=lambda call: call.data.startswith('sec_'))
def handle_security_menu(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Вы выбрали {call.data}")

@bot.callback_query_handler(func=lambda call: call.data.startswith('video_'))
def handle_video_menu(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Вы выбрали {call.data}")

@bot.callback_query_handler(func=lambda call: call.data == 'back_to_author')
def handle_back_to_author(call):
    show_author_menu(call)

# Запуск бота
bot.polling()
