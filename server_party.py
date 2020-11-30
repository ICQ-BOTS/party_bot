# -*- coding: utf8 -*-

import content
import database
import json
import random


def init_user(func):
    def wrapper(*args, **kwargs):
        if kwargs['event'].data["chat"]["type"] == "private":
            user_info = database.check_user(kwargs['event'].data["from"]["userId"])
            if user_info["not_exist"]:
                database.add_user(kwargs['event'].data["from"]["userId"])

        if kwargs['event'].data["chat"]["type"] == "private":
            database.set_stat("personal")
        else:
            database.set_stat(kwargs['event'].data["chat"]["chatId"])
        func(*args, **kwargs)				
    return wrapper


def but_ok(func):
    def wrapper(*args, **kwargs): 
        kwargs['bot'].answer_callback_query(kwargs['event'].data['queryId'], text=None)
        func(*args, **kwargs)
    return wrapper


@init_user
def truth_cm(bot, event):
    game = database.get_game(event.data["chat"]["chatId"])
    if game:
        if game[0][-1] == "truth":
            send_true(bot, event.data)
            database.set_stat_command("Бот правда")
        else:
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.no_game)
    else:
        send_true(bot, event.data)
        database.set_stat_command("Бот правда")


@init_user
def go_cm(bot, event):
    game = database.get_game(event.data["chat"]["chatId"])
    if game:
        if game[0][-1] == "go":
            send_action(bot, event.data)
            database.set_stat_command("Бот действие")
        else:
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.no_game)
    else:
        send_action(bot, event.data)
        database.set_stat_command("Бот действие")


@init_user
def spin_cm(bot, event):
    game = database.get_game(event.data["chat"]["chatId"])
    if game:
        if game[0][-1] == "spin":
            if event.data["chat"]["type"] == "private":
                bot.send_text(
                    chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
                return
            send_bottle(bot, event.data)
            database.set_stat_command("Бот бутылочка")
        else:
           bot.send_text(chat_id=event.data["chat"]
                         ["chatId"], text=content.no_game)
    else:
        if event.data["chat"]["type"] == "private":
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
            return
        send_bottle(bot, event.data)
        database.set_stat_command("Бот бутылочка")


@init_user
def croc_cm(bot, event):
    game = database.get_game(event.data["chat"]["chatId"])
    if game:
        if game[0][-1] == "croc":
            if event.data["chat"]["type"] == "private":
                bot.send_text(
                    chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
                return
            is_ok = check_members(bot, event.data)
            if is_ok:
                return
            send_crocodile(bot, event.data)
            database.set_stat_command("Бот сыграем в крокодила")
        else:
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.no_game)
    else:
        if event.data["chat"]["type"] == "private":
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
            return
        is_ok = check_members(bot, event.data)
        if is_ok:
            return
        send_crocodile(bot, event.data)
        database.set_stat_command("Бот сыграем в крокодила")


@init_user
def film_cm(bot, event):
    game = database.get_game(event.data["chat"]["chatId"])
    if game:
        if game[0][-1] == "film":
            if event.data["chat"]["type"] == "private":
                bot.send_text(
                    chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
                return
            is_ok = check_members(bot, event.data)
            if is_ok:
                return
            send_film(bot, event.data)
            database.set_stat_command("Бот сыграем в угадай фильм")
        else:
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.no_game)
    else:
        if event.data["chat"]["type"] == "private":
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
            return
        is_ok = check_members(bot, event.data)
        if is_ok:
            return
        send_film(bot, event.data)
        database.set_stat_command("Бот сыграем в угадай фильм")


@init_user
def person_cm(bot, event):
    game = database.get_game(event.data["chat"]["chatId"])
    if game:
        if game[0][-1] == "person":
            if event.data["chat"]["type"] == "private":
                bot.send_text(
                    chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
                return
            is_ok = check_members(bot, event.data)
            if is_ok:
                return
            send_who_am_i(bot, event.data)
            database.set_stat_command("Бот сыграем в угадай персонажа")
        else:
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.no_game)
    else:
        if event.data["chat"]["type"] == "private":
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
            return
        is_ok = check_members(bot, event.data)
        if is_ok:
            return
        send_who_am_i(bot, event.data)
        database.set_stat_command("Бот сыграем в угадай персонажа")


@init_user
def who_cm(bot, event):
    game = database.get_game(event.data["chat"]["chatId"])
    if game:
        if game[0][-1] == "who":
            if event.data["chat"]["type"] == "private":
                bot.send_text(
                    chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
                return
            is_ok = check_members(bot, event.data)
            if is_ok:
                return
            send_character(bot, event.data)
            database.set_stat_command("Бот сыграем в кто я")
        else:
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.no_game)
    else:
        if event.data["chat"]["type"] == "private":
            bot.send_text(
                chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
            return
        is_ok = check_members(bot, event.data)
        if is_ok:
            return
        send_character(bot, event.data)
        database.set_stat_command("Бот сыграем в кто я")


@init_user
def send_start(bot, event):
    bot.send_text(chat_id=event.data["chat"]
                  ["chatId"], text=content.command_start)


@init_user
def send_command_info(bot, event):
    bot.send_text(chat_id=event.data["chat"]
                  ["chatId"], text=content.command_info)


@init_user
def level_game(bot, event):
    game = database.get_game(event.data["chat"]["chatId"])
    if not game:
        game = event.text.split("_")[-1]
        get_game_level(bot, event.data, game)


@init_user
def faq(bot, event):
    bot.send_text(chat_id=event.data["chat"]["chatId"], text=content.faq)


@init_user
def change_user(bot, event):
    if event.data["chat"]["type"] == "private":
        bot.send_text(chat_id=event.data["chat"]["chatId"], text=content.command_is_chat)
        return
    game = event.data.get('text', '').split("_")[-1]
    if game in content.games:
        send_level(bot, event.data, game)
    else:
        message = "В этой игре пока нельзя изменить уровень сложности или данной игры не существует. Следи за обновлениями бота:) "
        bot.send_text(chat_id=event.data["chat"]["chatId"], text=message)


def get_game_level(bot, data, game):
    if game in list(content.games.keys()):
        level_info = database.get_level(data["chat"]["chatId"], game)
        if level_info:
            level_dict = {'super': 'Супер Хард', 'hard': 'Сложный', 'middle': 'Средний', 'easy': 'Легкий'}
            level = level_dict[level_info[0][-2]]
        else:
            level = "Средний"
        message = "Уровень сложности для данной игры: " + level
        bot.send_text(chat_id=data["chat"]["chatId"], text=message)
    else:
        message = "Данной игры нет или для нее нельзя запросить уровень"
        bot.send_text(chat_id=data["chat"]["chatId"], text=message)


def send_level(bot, data, game):
    message = content.games[game]["level_message"]
    inline_keyboard_markup = [
        [{"text": "Простой", "callbackData": "level_easy_" + game}],
        [{"text": "Средний", "callbackData": "level_middle_" + game}],
        [{"text": "Сложный", "callbackData": "level_hard_" + game}]
    ]
    if game == "croc":
        inline_keyboard_markup.append(
            [{"text": "Супер Хард", "callbackData": "level_super_"+game}])
    inline_keyboard_markup = json.dumps(inline_keyboard_markup)
    is_admin = check_admin_chat(bot,data)
    if is_admin:
        bot.send_text(chat_id=data["chat"]["chatId"], text=message,
                      inline_keyboard_markup=inline_keyboard_markup)


def check_members(bot, data):
    members = bot.get_chat_members(chat_id=data["chat"]["chatId"]).json()
    if members['ok'] == True:
        if len(members["members"]) > 20:
            message = "Чтобы использовать бота в чате должно быть меньше 20 человек"
            bot.send_text(chat_id=data["chat"]["chatId"], text=message)
            return True
        else:
            return False
    else:
        message = "У бота нет прав администратора в этом чате"
        bot.send_text(chat_id=data["chat"]["chatId"], text=message)
        return True


def send_character(bot, data):
    info = bot.get_chat_members(chat_id=data["chat"]["chatId"]).json()
    if info == {'ok': False, 'description': 'Permission denied'}:
        message = "У бота нет прав администратора в этом чате"
        bot.send_text(chat_id=data["chat"]["chatId"],
                      text=message, reply_msg_id=data["msgId"])
    else:
        info = info["members"]
        person = info[random.randint(0, len(info)-1)]["userId"]
        try:
            is_bot = bot.get_chat_info(chat_id=person).json()['isBot']
        except:
            is_bot = False
        while is_bot == True:
            person = info[random.randint(0, len(info)-1)]["userId"]
            try:
                is_bot = bot.get_chat_info(chat_id=person).json()['isBot']
            except:
                is_bot = False
        level_info = database.get_level(data["chat"]["chatId"], "person")
        if level_info:
            level = level_info[0][-2]
        else:
            level = "middle"
        who_am_i = content.games["person"][level][random.randint(
            0, len(content.games["person"][level])-1)]
        # who_am_i = content.who_am_i[random.randint(0,len(content.who_am_i)-1)]
        message = "Пользователь @["+person+"] угадывает персонажа"
        bot.send_text(chat_id=data["chat"]["chatId"], text=message)
        for member in range(0, len(info)):
            if bot.get_chat_info(chat_id=info[member]['userId']).json().get('isBot') == True:
                info[member] = None
        for member in info:
            if member:
                if member['userId'] == person:
                    message = "Ты угадываешь персонажа"
                    if bot.send_text(chat_id=person, text=message).json()['ok'] == False:
                        bot.send_text(chat_id=data["chat"]["chatId"], text="Я знаком еще не со всеми участниками тусовки. \n @[" +
                                      person+"], перейди в диалог со мной и нажми кнопку «начать»")
                else:
                    inline_keyboard_markup = json.dumps([
                        [{"text": "Угадано", "callbackData": "solved_who_" +
                            data["chat"]["chatId"], "style": "primary"}]
                    ])
                    message = "Участник @["+person + "] угадывает персонажа.\n\nЕго персонаж: " + who_am_i
                    if bot.send_text(chat_id=member['userId'], text=message, inline_keyboard_markup=inline_keyboard_markup).json()['ok'] == False:
                        bot.send_text(chat_id=data["chat"]["chatId"], text="Я знаком еще не со всеми участниками тусовки. \n @[" +
                                      member['userId']+"], перейди в диалог со мной и нажми кнопку «начать»")


def send_film(bot, data):
    info = bot.get_chat_members(chat_id=data["chat"]["chatId"]).json()
    if info == {'ok': False, 'description': 'Permission denied'}:
        message = "У бота нет прав администратора в этом чате"
        bot.send_text(chat_id=data["chat"]["chatId"],
                      text=message, reply_msg_id=data["msgId"])
    else:
        info = info["members"]
        person = info[random.randint(0, len(info)-1)]["userId"]
        try:
            is_bot = bot.get_chat_info(chat_id=person).json()['isBot']
        except:
            is_bot = False
        while is_bot == True:
            person = info[random.randint(0, len(info)-1)]["userId"]
            try:
                is_bot = bot.get_chat_info(chat_id=person).json()['isBot']
            except:
                is_bot = False
        level_info = database.get_level(data["chat"]["chatId"], "film")
        if level_info:
            level = level_info[0][-2]
        else:
            level = "middle"
        film = content.games["film"][level][random.randint(
            0, len(content.games["film"][level])-1)]
        letter = content.letters[random.randint(0, len(content.letters)-1)]
        # film = content.films[random.randint(0,len(content.films)-1)]
        message = "Попробуй объяснить фильм: "+film
        message = message + "\n\nМожно использовать только слова на букву: "+letter
        inline_keyboard_markup = json.dumps([
            [{"text": "Другой фильм", "callbackData": level +
                "_new_film_"+letter+"_"+data["chat"]["chatId"]}],
            [{"text": "Угадано", "callbackData": "solved_film_" +
                data["chat"]["chatId"], "style": "primary"}]
        ])
        if bot.send_text(chat_id=person, text=message, inline_keyboard_markup=inline_keyboard_markup).json()['ok'] == False:
            bot.send_text(chat_id=data["chat"]["chatId"], text="Я знаком еще не со всеми участниками тусовки. \n @[" +
                          person+"], перейди в диалог со мной и нажми кнопку «начать»")
        message = "Пользователь @["+person + \
            "] объясняет фильм используя слова на букву "+letter+"\nКак играть: /faq"
        bot.send_text(chat_id=data["chat"]["chatId"], text=message)


def send_crocodile(bot, data):
    info = bot.get_chat_members(chat_id=data["chat"]["chatId"]).json()
    if info == {'ok': False, 'description': 'Permission denied'}:
        message = "У бота нет прав администратора в этом чате"
        bot.send_text(chat_id=data["chat"]["chatId"],
                      text=message, reply_msg_id=data["msgId"])
    else:
        info = info["members"]
        person = info[random.randint(0, len(info)-1)]["userId"]
        try:
            is_bot = bot.get_chat_info(chat_id=person).json()['isBot']
        except:
            is_bot = False
        while is_bot == True:
            person = info[random.randint(0, len(info)-1)]["userId"]
            try:
                is_bot = bot.get_chat_info(chat_id=person).json()['isBot']
            except:
                is_bot = False
        level_info = database.get_level(data["chat"]["chatId"], "croc")
        if level_info:
            level = level_info[0][-2]
        else:
            level = "middle"
        word = content.games["croc"][level][random.randint(
            0, len(content.games["croc"][level])-1)]
        # word = content.words[random.randint(0,len(content.words)-1)]
        if level == "super":
            message = "Попробуй объяснить поговорку: "+word
        else:
            message = "Попробуй объяснить слово: "+word
            message = message + "\n\nНельзя использовать однокренные слова"
        inline_keyboard_markup = json.dumps([
            [{"text": "Другое слово", "callbackData": level +
                "_new_word_"+data["chat"]["chatId"]}],
            [{"text": "Угадано", "callbackData": "solved_croc_" +
                data["chat"]["chatId"], "style": "primary"}]
        ])
        if bot.send_text(chat_id=person, text=message, inline_keyboard_markup=inline_keyboard_markup).json()['ok'] == False:
            bot.send_text(chat_id=data["chat"]["chatId"], text="Я знаком еще не со всеми участниками тусовки. \n @[" +
                          person+"], перейди в диалог со мной и нажми кнопку «начать»")
        message = "Пользователь @["+person + \
            "] объясняет слово.\nКак играть: /faq"
        bot.send_text(chat_id=data["chat"]["chatId"], text=message)


def send_who_am_i(bot, data):
    info = bot.get_chat_members(chat_id=data["chat"]["chatId"]).json()
    if info == {'ok': False, 'description': 'Permission denied'}:
        message = "У бота нет прав администратора в этом чате"
        bot.send_text(chat_id=data["chat"]["chatId"],
                      text=message, reply_msg_id=data["msgId"])
    else:
        info = info["members"]
        person = info[random.randint(0, len(info)-1)]["userId"]
        try:
            is_bot = bot.get_chat_info(chat_id=person).json()['isBot']
        except:
            is_bot = False
        while is_bot == True:
            person = info[random.randint(0, len(info)-1)]["userId"]
            try:
                is_bot = bot.get_chat_info(chat_id=person).json()['isBot']
            except:
                is_bot = False
        level_info = database.get_level(data["chat"]["chatId"], "who")
        if level_info:
            level = level_info[0][-2]
        else:
            level = "middle"
        inline_keyboard_markup = json.dumps([
            [{"text": "Другой персонаж", "callbackData": level +
                "_new_character_"+data["chat"]["chatId"]}],
            [{"text": "Угадано", "callbackData": "solved_person_" +
                data["chat"]["chatId"], "style": "primary"}]
        ])
        who_am_i = "Твой персонаж — " + \
            content.games["who"][level][random.randint(
                0, len(content.games["who"][level])-1)]
        if bot.send_text(chat_id=person, text=who_am_i, inline_keyboard_markup=inline_keyboard_markup).json()['ok'] == False:
            bot.send_text(chat_id=data["chat"]["chatId"], text="Я знаком еще не со всеми участниками тусовки. \n @[" +
                          person+"], перейди в диалог со мной и нажми кнопку «начать»")
        message = "Пользователь @["+person + \
            "] загадывает персонажа.\nКак играть: /faq"
        bot.send_text(chat_id=data["chat"]["chatId"], text=message)


def send_help(bot, event):
    bot.send_text(
        chat_id=event.data["chat"]["chatId"], 
        text=content.command_help, 
        reply_msg_id=event.data["msgId"]
    )


def send_true(bot, data):
    question = content.questions[random.randint(0, len(content.questions)-1)]
    bot.send_text(chat_id=data["chat"]["chatId"],
                  text=question, reply_msg_id=data["msgId"])


def send_action(bot, data):
    question = content.actions[random.randint(0, len(content.actions)-1)]
    bot.send_text(chat_id=data["chat"]["chatId"],
                  text=question, reply_msg_id=data["msgId"])


def send_bottle(bot, data):
    info = bot.get_chat_members(
        chat_id=data["chat"]["chatId"]).json()["members"]
    person1 = info[random.randint(0, len(info)-1)]["userId"]
    message = """Бутылочка выбрала @["""+str(person1)+"""]
Можете обменяться стикерами 😉
"""
    bot.send_text(
        chat_id=data["chat"]["chatId"],
        text=message, 
        reply_msg_id=data["msgId"]
    )


@but_ok
def but_solved(bot, event):
    chatId = event.data["callbackData"].split("_")[-1]
    if "film" in event.data["callbackData"]:
        message = "Успех! Вы догадались, что за фильм. Еще разок? /film"
        bot.send_text(chat_id=chatId, text=message)
    elif "croc" in event.data["callbackData"]:
        message = "Ура! Слово угадано. Еще разок? /croc"
        bot.send_text(chat_id=chatId, text=message)
    elif "who" in event.data["callbackData"]:
        message = "Поздравляю! Персонаж отгадан. Еще разок? /who "
        bot.send_text(chat_id=chatId, text=message)
    elif "person" in event.data["callbackData"]:
        message = "Поздравляю! Персонаж отгадан. Еще разок? /person"
        bot.send_text(chat_id=chatId, text=message)


@but_ok
def but_new_film(bot, event):
    letter = event.data["callbackData"].split("_")[-2]
    chatId = event.data["callbackData"].split("_")[-1]
    level = event.data["callbackData"].split("_")[0]
    film = content.games["film"][level][random.randint(
        0, len(content.games["film"][level])-1)]
    message = film + " на букву " + letter
    inline_keyboard_markup = json.dumps([
        [{"text": "Другой фильм", "callbackData": level +
            "_new_film_"+letter+"_"+chatId}],
        [{"text": "Угадано", "callbackData": "solved_film_"+chatId, "style": "primary"}]
    ])
    bot.send_text(
        chat_id=event.data["message"]["chat"]["chatId"],
        text=message, 
        inline_keyboard_markup=inline_keyboard_markup
    )


@but_ok
def but_new_character(bot, event):
    level = event.data["callbackData"].split("_")[0]
    chatId = event.data["callbackData"].split("_")[-1]
    inline_keyboard_markup = json.dumps([
        [{"text": "Другой персонаж", "callbackData": level+"_new_character_"+chatId}],
        [{"text": "Угадано", "callbackData": "solved_who_"+chatId, "style": "primary"}]
    ])
    # who_am_i = content.who_am_i[random.randint(0,len(content.who_am_i)-1)]
    who_am_i = "Твой персонаж — " + \
        content.games["who"][level][random.randint(
            0, len(content.games["who"][level])-1)]
    bot.send_text(
        chat_id=event.data["message"]["chat"]["chatId"],
        text=who_am_i, 
        inline_keyboard_markup=inline_keyboard_markup
    )


@but_ok
def but_new_word(bot, event):
    level = event.data["callbackData"].split("_")[0]
    chatId = event.data["callbackData"].split("_")[-1]
    inline_keyboard_markup = json.dumps([
        [{"text": "Другое слово", "callbackData": level+"_new_word_"+chatId}],
        [{"text": "Угадано", "callbackData": "solved_who_"+chatId, "style": "primary"}]
    ])
    word = content.games["croc"][level][random.randint(
        0, len(content.games["croc"][level])-1)]
    if level == "super":
        message = "Попробуй объяснить поговорку — "+word
    else:
        message = "Попробуй объяснить слово — "+word
        message = message + "\n\nНельзя использовать однокренные слова"
    # word = content.words[random.randint(0,len(content.words)-1)]
    message = "Попробуй объяснить слово — "+word
    message = message + "\n\nНельзя использовать однокренные слова"
    bot.send_text(
        chat_id=event.data["message"]["chat"]["chatId"],
        text=message, 
        inline_keyboard_markup=inline_keyboard_markup
    )


@but_ok
def but_level(bot, event):
    game = event.data["callbackData"].split("_")[-1]
    if "easy" in event.data["callbackData"]:
        is_admin = check_admin(bot, event.data)
        if is_admin:
            database.set_level(
                event.data["message"]["chat"]["chatId"], "easy", game)
            message = "Уровень сложности успешно изменен на Легкий"
        else:
            message = "Нужно обладать правами администратора для изменения уровня"
        bot.send_text(
            chat_id=event.data["message"]["chat"]["chatId"], 
            text=message
        )
    elif "middle" in event.data["callbackData"]:
        is_admin = check_admin(bot, event.data)
        if is_admin:
            database.set_level(
                event.data["message"]["chat"]["chatId"], "middle", game)
            message = "Уровень сложности успешно изменен на Средний"
        else:
            message = "Нужно обладать правами администратора для изменения уровня"
        bot.send_text(
            chat_id=event.data["message"]["chat"]["chatId"], 
            text=message
        )
    elif "hard" in event.data["callbackData"]:
        is_admin = check_admin(bot, event.data)
        if is_admin:
            database.set_level(
                event.data["message"]["chat"]["chatId"], "hard", game)
            message = "Уровень сложности успешно изменен на Сложный"
        else:
            message = "Нужно обладать правами администратора для изменения уровня"
        bot.send_text(
            chat_id=event.data["message"]["chat"]["chatId"], 
            text=message
        )
    elif "super" in event.data["callbackData"]:
        is_admin = check_admin(bot, event.data)
        if is_admin:
            database.set_level(
                event.data["message"]["chat"]["chatId"], "super", game)
            message = "Уровень сложности успешно изменен на Супер Хард"
        else:
            message = "Нужно обладать правами администратора для изменения уровня"
        bot.send_text(
            chat_id=event.data["message"]["chat"]["chatId"], 
            text=message
        )


def check_admin(bot, data):
    members = bot.get_chat_members(
        chat_id=data["message"]["chat"]["chatId"]).json()
    if members['ok'] == True:
        for member in members["members"]:
            if data['from']['userId'] == member['userId']:
                if member.get("admin") or member.get("creator"):
                    return True


def check_admin_chat(bot,data):
    members = bot.get_chat_members(chat_id=data["chat"]["chatId"]).json()
    if members['ok'] == True:
        for member in members["members"]:
            if data['from']['userId'] == member['userId']:
                if member.get("admin") or member.get("creator"):
                    return True