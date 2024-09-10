from telebot import *

token = 'тг токен'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Стандартные операции")
    item2 = types.KeyboardButton("Степени и корни")
    item3 = types.KeyboardButton("Системы счисления")
    markup.add(item1,item2,item3)	
    bot.send_message(message.chat.id,'Что нада',reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Сложение")
    item2 = types.KeyboardButton("Вычитание")
    item3 = types.KeyboardButton("Умножение")
    item4 = types.KeyboardButton("Деление")
    item7 = types.KeyboardButton("Возведение в степень")
    item8 = types.KeyboardButton("Вычисление корня")
    item9 = types.KeyboardButton("Факториал")
    item10 = types.KeyboardButton("Системы счисления")
    item = types.KeyboardButton("Назад")
    bob1 = types.KeyboardButton("Стандартные операции")
    bob2 = types.KeyboardButton("Степени и корни")
    bob3 = types.KeyboardButton("Другие функции")
    if message.text=="Стандартные операции":
        markup.add(item1,item2,item3,item4,item)
        bot.send_message(message.chat.id,'Выберите операцию',reply_markup=markup)
    elif message.text=="Назад":
            markup.add(bob1,bob2,bob3)
            bot.send_message(message.chat.id,'Что нада',reply_markup=markup)    
    elif message.text=="Степени и корни":
        markup.add(item7,item8, item)
        bot.send_message(message.chat.id,'Выберите операцию',reply_markup=markup)
    elif message.text == "Другие функции":
        markup.add(item9,item10, item)
        bot.send_message(message.chat.id,'Выберите операцию',reply_markup=markup)
    elif message.text == "Системы счисления":
        a = bot.send_message(message.chat.id,'Системы счисления: Введите 2 числа через пробел. Пример: 100 2 (100 - число, 2 - система счисления)',reply_markup=markup)
        bot.register_next_step_handler(a, q_7)
    elif message.text == "Факториал":
        a = bot.send_message(message.chat.id,'Вычисление факториала: Введите число',reply_markup=markup)
        bot.register_next_step_handler(a, q_8)  
    elif message.text=="Сложение":
        a = bot.send_message(message.chat.id,'Сложение: Введите 2 числа через пробел',reply_markup=markup)
        bot.register_next_step_handler(a, q_1)
    elif message.text=="Вычитание":
        a = bot.send_message(message.chat.id,'Вычитание: Введите 2 числа через пробел',reply_markup=markup)
        bot.register_next_step_handler(a, q_2)
    elif message.text=="Умножение":
        a = bot.send_message(message.chat.id,'Умножение: Введите 2 числа через пробел',reply_markup=markup)
        bot.register_next_step_handler(a, q_3)
    elif message.text=="Деление":
        a = bot.send_message(message.chat.id,'Деление: Введите 2 числа через пробел',reply_markup=markup)
        bot.register_next_step_handler(a, q_4)
    elif message.text=="Возведение в степень":
        a = bot.send_message(message.chat.id,'Возведение в степень: Введите 2 числа через пробел. Пример: 2 4. (2 - число, 4 - степень)',reply_markup=markup)
        bot.register_next_step_handler(a, q_5)
    elif message.text=="Вычисление корня":
        a = bot.send_message(message.chat.id,'Вычисление корня: Введите 2 числа через пробел. Пример: 625 4. (625 - число, 4 - степень корня)',reply_markup=markup)
        bot.register_next_step_handler(a, q_6)  
    
def bob(a,b):
    res = ''
    a = int(a)
    b = int(b)
    while a > 0:
        res = str(a%b) + res
        a = a // b
    return res

def fac(n):
    n = int(n)
    if n == 1:
        return 1
    return fac(n-1) * n

def q_1(message):
    res = str(message.text).split()
    try:
        if len(res) > 2:
            bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
        elif float(res[0])+float(res[1]) == 52:
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=YAdL4iobqwE')
        else:
            bot.send_message(message.chat.id, float(res[0])+float(res[1]))
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
def q_2(message):
    res = str(message.text).split()
    try:
        if len(res) > 2:
            bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
        elif float(res[0])-float(res[1]) == 52:
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=YAdL4iobqwE')
        else:
            bot.send_message(message.chat.id, float(res[0])-float(res[1]))
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
def q_3(message):
    res = str(message.text).split()
    try:
        if len(res) > 2:
            bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
        elif float(res[0])*float(res[1]) == 52:
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=YAdL4iobqwE')
        else:
            bot.send_message(message.chat.id, float(res[0])*float(res[1]))
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
def q_4(message):
    res = str(message.text).split()
    try:
        if len(res) > 2:
            bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
        elif float(res[0])/float(res[1]) == 52:
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=YAdL4iobqwE')
        else:
            bot.send_message(message.chat.id, float(res[0])/float(res[1]))
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
    except ZeroDivisionError:
        bot.send_message(message.chat.id, 'выбери заново операцию, я не могу поделить на 0')
def q_5(message):
    res = str(message.text).split()
    try:
        if len(res) > 2:
            bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
        elif float(res[0])**float(res[1]) == 52:
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=YAdL4iobqwE')
        else:
            bot.send_message(message.chat.id, float(res[0])**float(res[1]))
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
def q_6(message):
    res = str(message.text).split()
    try:
        if int(res[0]) < 0 and float(res[1]) % 2 == 0:
            bot.send_message(message.chat.id, 'выбери заново операцию, нельзя вычислить корень четной степени из отрицательного числа')
        elif str(abs(float(res[0]))**(1/(float(res[1])))) == 52:
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=YAdL4iobqwE')
        elif int(res[0]) < 0 and float(res[1]) % 2 != 0:
            bot.send_message(message.chat.id, '-' + str(abs(float(res[0]))**(1/(float(res[1])))))
        elif len(res) > 2:
            bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
        else:
            bot.send_message(message.chat.id, float(res[0])**(1/(float(res[1]))))
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
    except ZeroDivisionError:
        bot.send_message(message.chat.id, 'выбери заново операцию, я не могу посчитать корень 0 степени')
def q_7(message):
    res = str(message.text).split()
    try:
        if float(res[0]) <= 0:
            bot.send_message(message.chat.id, 'выбери заново операцию, введи число больше 0')
        elif bob(res[0],res[1]) == 52:
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=YAdL4iobqwE')
        elif float(res[1]) <= 1:
            bot.send_message(message.chat.id, 'выбери заново операцию, введи систему счисления больше 1')
        if len(res) > 2:
            bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа и только в формате: 20 4 (2 числа через пробел)')
        else:   
            bot.send_message(message.chat.id, bob(res[0],res[1]))
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только целые числа и только в формате: 20 4 (2 числа через пробел)')
    except ZeroDivisionError:
        bot.send_message(message.chat.id, 'выбери заново операцию, я не могу перевести в 0 систему счисления')
def q_8(message):
    res = str(message.text).split()
    try:
        if int(res[0]) < 0:
            bot.send_message(message.chat.id, 'выберите заново операцию, факториал вычисляется только у положительного целого числа')
        elif fac(res[0]) == 52:
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=YAdL4iobqwE')
        elif len(res) > 1:
            bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа, вводить нужно 1 число')
        else:
            bot.send_message(message.chat.id, fac(res[0]))
    except (ValueError, IndexError):
        bot.send_message(message.chat.id, 'выбери заново операцию, ты можешь использовать только числа, вводить нужно 1 число')
    except RecursionError:
        bot.send_message(message.chat.id, '1')

bot.infinity_polling()