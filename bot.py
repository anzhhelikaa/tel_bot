import telebot
from telebot import types
from bot_logic import flip_coin  # Импортируем функции из bot_logic
from config import token

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['feedback'])
def feedback(message):
    print("Команда /feedback получена")  # Логирование, чтобы понять, срабатывает ли команда
    bot.send_message(message.chat.id, "Что бы ты хотел предложить для улучшения экологии в нашем сообществе? Напиши свою идею.")
    bot.register_next_step_handler(message, handle_feedback)

# Обработка фидбека
def handle_feedback(message):
    print(f"Получен фидбек: {message.text}")  # Логируем полученный фидбек
    user_feedback = message.text
    bot.send_message(message.chat.id, f"Спасибо за предложение: '{user_feedback}'! Мы обязательно его рассмотрим.")

@bot.message_handler(commands=['checklist'])
def send_checklist(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Чек-лист для дома")
    btn2 = types.KeyboardButton("Чек-лист для бизнеса")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Выбери, для чего тебе нужен чек-лист:", reply_markup=markup)

# Чек-лист для дома
@bot.message_handler(func=lambda message: message.text == "Чек-лист для дома")
def checklist_for_home(message):
    checklist = """
    Вот несколько простых шагов для улучшения энергоэффективности дома:
    1. Замените лампочки на энергосберегающие (LED).
    2. Установите термостат для контроля температуры.
    3. Утеплите окна и двери, чтобы избежать потерь тепла.
    4. Используйте энергосберегающие бытовые приборы.
    5. Регулярно чистите фильтры в кондиционерах и обогревателях.
    6. Отключайте электроприборы от сети, когда они не используются.
    7. Используйте солнечные панели или другие источники возобновляемой энергии.
    8. Соблюдайте режим отопления и охлаждения в зависимости от сезона (не перегревайте или не переохлаждайте помещение).
    9. Начните сортировать отходы и перерабатывать материалы.
    """
    bot.send_message(message.chat.id, text=checklist)

# Чек-лист для бизнеса
@bot.message_handler(func=lambda message: message.text == "Чек-лист для бизнеса")
def checklist_for_business(message):
    checklist = """
    Вот несколько шагов для улучшения энергоэффективности бизнеса:
    1. Замените старые осветительные системы на энергосберегающие (LED).
    2. Установите системы управления энергопотреблением (например, умные термостаты).
    3. Внедрите программы для сотрудников по энергосбережению (например, отключение оборудования, когда оно не используется).
    4. Используйте возобновляемые источники энергии (солнечные панели, ветровые генераторы и т.д.).
    5. Пересмотрите корпоративные транспортные политики: поощряйте использование общественного транспорта, электромобилей или велосипедов.
    6. Сократите бумажные материалы и используйте цифровые документы.
    7. Установите системы для переработки отходов и раздельного сбора мусора.
    8. Инвестируйте в экологически чистые технологии для производства.
    9. Снижайте углеродные выбросы, оптимизируя логистику и цепочку поставок.
    """
    bot.send_message(message.chat.id, text=checklist)

# Хендлер для команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Для получения помощи напишите /start. Для чек-листов по экологии используйте команду /checklist.")
    
faq = [
    {
        'question': "Что такое углеродный след?",
        'answer': """Углеродный след — это общий объем парниковых газов, который производится в процессе жизнедеятельности человека или производства товаров и услуг. Эти газы включают углекислый газ (CO2), метан (CH4), закись азота (N2O) и другие, которые способствуют глобальному потеплению и изменению климата."""
    },
    {
        'question': "Как я могу уменьшить свой углеродный след?",
        'answer': """Для снижения углеродного следа можно:
1. Использовать общественный транспорт или переходить на электромобили.
2. Снижать потребление энергии: выключать свет и технику, использовать энергоэффективные устройства.
3. Переходить на возобновляемые источники энергии (солнечные панели, ветрогенераторы).
4. Уменьшать потребление мяса и других продуктов животного происхождения, так как животноводство имеет высокий углеродный след."""
    },
    {
        'question': "Что такое глобальное потепление?",
        'answer': """Глобальное потепление — это процесс увеличения средней температуры на планете, вызванный накоплением парниковых газов в атмосфере. Основной причиной является человеческая деятельность, включая сжигание ископаемых видов топлива, вырубку лесов и сельское хозяйство."""
    },
    {
        'question': "Почему важны возобновляемые источники энергии?",
        'answer': """Возобновляемые источники энергии, такие как солнечная, ветровая и гидроэнергия, не истощаются и не загрязняют окружающую среду. Использование этих источников помогает сократить выбросы углекислого газа и других парниковых газов, что в свою очередь замедляет процесс глобального потепления."""
    },
    {
        'question': "Что такое пластиковый загрязнение?",
        'answer': """Пластиковое загрязнение — это накопление пластиковых отходов в окружающей среде, включая океаны, реки и землю. Пластик разлагается очень медленно и часто угрожает дикой природе, особенно морским животным, которые могут проглотить или запутаться в пластиковых предметах."""
    },
    {
        'question': "Что я могу сделать, чтобы сократить использование пластика?",
        'answer': """Для уменьшения использования пластика можно:
1. Использовать многоразовые сумки и контейнеры.
2. Избегать покупки одноразовой пластиковой упаковки.
3. Выбирать товары с минимальной упаковкой.
4. Сортировать мусор и сдавать пластик на переработку."""
    }
]

# Хендлер для команды /faq
@bot.message_handler(commands=['faq'])
def send_faq(message):
    faq_text = "Вот несколько часто задаваемых вопросов по экологии:\n\n"
    for index, item in enumerate(faq):
        faq_text += f"{index + 1}. {item['question']}\n"
    
    faq_text += "\nЧтобы получить более подробный ответ, отправь номер вопроса, например: '1' или '2'."
    bot.send_message(message.chat.id, faq_text)

# Хендлер для получения ответа на конкретный вопрос
@bot.message_handler(func=lambda message: message.text.isdigit() and 1 <= int(message.text) <= len(faq))
def send_faq_answer(message):
    question_index = int(message.text) - 1
    answer = faq[question_index]['answer']
    bot.send_message(message.chat.id, answer)

questions = [
    {
        'question': "Какой газ является основным виновником глобального потепления?",
        'options': ["CO2", "O2", "N2", "He"],
        'correct_answer': "CO2"
    },
    {
        'question': "Какая деятельность человека считается основным источником выбросов углекислого газа в атмосферу?",
        'options': ["Лесозаготовка", "Сельское хозяйство", "Автомобильный транспорт", "Индустриальное производство"],
        'correct_answer': "Автомобильный транспорт"
    },
    {
        'question': "Какой из этих источников энергии считается возобновляемым?",
        'options': ["Уголь", "Газ", "Солнечная энергия", "Нефть"],
        'correct_answer': "Солнечная энергия"
    },
    {
        'question': "Какая из следующих мер поможет уменьшить углеродный след?",
        'options': ["Использование одноразовых пластиковых бутылок", "Применение возобновляемых источников энергии", "Сжигание угля для производства энергии", "Переход на углеводородные автомобили"],
        'correct_answer': "Применение возобновляемых источников энергии"
    },
    {
        'question': "Как называется процесс, при котором леса и растения поглощают углекислый газ?",
        'options': ["Деградация", "Силосирование", "Фотосинтез", "Вулканизм"],
        'correct_answer': "Фотосинтез"
    },
    {
        'question': "Что из этого является основным источником загрязнения океанов пластиком?",
        'options': ["Рыболовные сети", "Пластиковые бутылки", "Космический мусор", "Курортный мусор"],
        'correct_answer': "Пластиковые бутылки"
    },
    {
        'question': "Какой процент углеродных выбросов в мире приходится на транспорт?",
        'options': ["10%", "25%", "40%", "15%"],
        'correct_answer': "25%"
    },
    {
        'question': "Какая из этих практик помогает уменьшить углеродные выбросы?",
        'options': ["Использование угольных электростанций", "Рециркуляция и переработка отходов", "Повышение потребления мяса", "Сжигание мусора"],
        'correct_answer': "Рециркуляция и переработка отходов"
    },
    {
        'question': "Какое из этих растений поглощает углекислый газ, создавая кислород?",
        'options': ["Кактус", "Водоросли", "Лавр", "Хлопок"],
        'correct_answer': "Водоросли"
    },
    {
        'question': "Что можно сделать для предотвращения глобального потепления в повседневной жизни?",
        'options': ["Сократить потребление мяса", "Покупать одноразовые пластиковые товары", "Использовать уголь для отопления", "Игнорировать энергосбережение"],
        'correct_answer': "Сократить потребление мяса"
    }
]

# Хендлер для начала квиза
@bot.message_handler(commands=['quiz'])
def start_quiz(message):
    question = questions[0]['question']
    options = questions[0]['options']
    
    # Создаем кнопки с вариантами ответа
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for option in options:
        markup.add(types.KeyboardButton(option))
    
    bot.send_message(message.chat.id, text=question, reply_markup=markup)
    # Сохраняем состояние квиза
    bot.register_next_step_handler(message, check_answer, 0)

# Хендлер для обработки ответов
def check_answer(message, question_index):
    correct_answer = questions[question_index]['correct_answer']
    
    if message.text == correct_answer:
        bot.send_message(message.chat.id, "Правильный ответ!")
    else:
        bot.send_message(message.chat.id, "Неправильный ответ. Попробуйте снова.")
        bot.register_next_step_handler(message, check_answer, question_index)
        return
    
    # Переходим к следующему вопросу, если он есть
    question_index += 1
    if question_index < len(questions):
        question = questions[question_index]['question']
        options = questions[question_index]['options']
        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        for option in options:
            markup.add(types.KeyboardButton(option))
        
        bot.send_message(message.chat.id, text=question, reply_markup=markup)
        bot.register_next_step_handler(message, check_answer, question_index)
    else:
        bot.send_message(message.chat.id, "Спасибо за участие! Напишите /quiz, чтобы начать заново.")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Мы боремся с глобальным потеплением, поможешь нам с этим?")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Приветствую! Хочешь узнать что-то? Я смогу помочь! Смотри в команды")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Тебе выпала: {coin}")

@bot.message_handler(commands=['news'])
def send_site(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сайт с новостями №1", url='https://www.climatechangenews.com/')
    button2 = types.InlineKeyboardButton("Сайт с новостями №2", url='https://insideclimatenews.org/')
    button3 = types.InlineKeyboardButton("Сайт с новостями №3", url='https://climate.nasa.gov/')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Жми на одну из кнопок и переходи на сайт с новостями!".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['recommendations'])
def send_recomend(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Снижение углеродного следа")
    btn2 = types.KeyboardButton("Энергосбережение")
    btn3 = types.KeyboardButton("Ответственное потребление")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Хорошо, советы на счет чего тебе нужны?".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def recomend(message):
    if(message.text == "Снижение углеродного следа"):
        bot.send_message(message.chat.id, text="""1. Используйте общественный транспорт или ходите пешком. Это помогает уменьшить выбросы углекислого газа, связанные с автомобильным транспортом.
2.Переходите на электромобили или гибридные автомобили, если это возможно.
3. Экономьте электроэнергию: выключайте свет и бытовую технику, когда они не используются, используйте энергосберегающие лампочки и устройства.
4.Уменьшайте использование пластика: пластиковые изделия способствуют загрязнению окружающей среды и требуют больших ресурсов для производства.""")
        
    elif(message.text == "Энергосбережение"):
        bot.send_message(message.chat.id, text="""1.Утепление домов. Хорошая теплоизоляция помогает снизить потребление энергии на отопление зимой и охлаждение летом. 
2. Использование возобновляемых источников энергии (солнечные панели, ветрогенераторы и т.д.), если это возможно. 
3. Снижение температуры в помещении зимой на 1-2 градуса или повышение летом помогает сэкономить энергию.""")
    
    elif(message.text == "Ответственное потребление"):
        bot.send_message(message.chat.id, text= """1.Покупайте экологически чистые продукты: выбирайте товары, произведенные с минимальным воздействием на окружающую среду (органическое земледелие, товары без излишней упаковки).
2. Питайтесь растительно: животноводство оказывает сильное воздействие на климат, поэтому сокращение потребления мяса и молочных продуктов может помочь уменьшить углеродные выбросы.
3. Сортировка мусора: переработка материалов помогает уменьшить нагрузку на свалки и снижает количество вредных выбросов в атмосферу.""")    
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

bot.polling(none_stop=True)