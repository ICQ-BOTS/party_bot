from asyncio import events
from bot.bot import Bot
from bot.filter import Filter
from bot.handler import (BotButtonCommandHandler, CommandHandler,
                         MessageHandler, StartCommandHandler)

import config
from server_party import (but_level, but_new_character, but_new_film,
                          but_new_word, but_solved, croc_cm, faq, film_cm,
                          go_cm, level_game, person_cm, send_command_info, 
                          send_help, send_start, spin_cm, truth_cm, who_cm, 
                          change_user)

bot = Bot(token=config.MAIN_TOKEN)

bot.dispatcher.add_handler(MessageHandler(
    callback=truth_cm,
    filters=Filter.regexp(r'(?i)^бот(.*?)правда')
))
bot.dispatcher.add_handler(CommandHandler(
    callback=truth_cm,
    command='truth'
))

bot.dispatcher.add_handler(MessageHandler(
    callback=go_cm,
    filters=Filter.regexp(r'(?i)^бот(.*?)действие')
))
bot.dispatcher.add_handler(CommandHandler(
    callback=go_cm,
    command='go'
))

bot.dispatcher.add_handler(MessageHandler(
    callback=spin_cm,
    filters=Filter.regexp(r'(?i)^бот(.*?)бутылочка')
))
bot.dispatcher.add_handler(CommandHandler(
    callback=spin_cm,
    command='spin'
))

bot.dispatcher.add_handler(MessageHandler(
    callback=croc_cm,
    filters=Filter.regexp(r'(?i)^бот(.*?)сыграем(.*?)в(.*?)крокодила')
))
bot.dispatcher.add_handler(CommandHandler(
    callback=croc_cm,
    command='croc'
))

bot.dispatcher.add_handler(MessageHandler(
    callback=film_cm,
    filters=Filter.regexp(r'(?i)^бот(.*?)сыграем(.*?)в(.*?)угадай(.*?)фильм')
))
bot.dispatcher.add_handler(CommandHandler(
    callback=film_cm,
    command='film'
))

bot.dispatcher.add_handler(MessageHandler(
    callback=person_cm,
    filters=Filter.regexp(r'(?i)^бот(.*?)сыграем(.*?)в(.*?)угадай(.*?)персонажа')
))
bot.dispatcher.add_handler(CommandHandler(
    callback=person_cm,
    command='person'
))

bot.dispatcher.add_handler(MessageHandler(
    callback=who_cm,
    filters=Filter.regexp(r'(?i)^бот(.*?)сыграем(.*?)в(.*?)кто(.*?)я')
))
bot.dispatcher.add_handler(CommandHandler(
    callback=who_cm,
    command='who'
))

bot.dispatcher.add_handler(MessageHandler(
    callback=send_help,
    filters=Filter.regexp(r'(?i)^бот(.*?)помощь')
))
bot.dispatcher.add_handler(CommandHandler(
    callback=send_help,
    command='help'
))

bot.dispatcher.add_handler(CommandHandler(
    callback=send_command_info,
    command='list'
))


bot.dispatcher.add_handler(CommandHandler(
    callback=faq,
    command='faq'
))

bot.dispatcher.add_handler(MessageHandler(
    callback=level_game,
    filters=Filter.regexp(r'(?i)^/level')
))

bot.dispatcher.add_handler(MessageHandler(
    callback=change_user,
    filters=Filter.regexp(r'(?i)^/change')
))

bot.dispatcher.add_handler(BotButtonCommandHandler(
    callback=but_solved,
    filters=Filter.callback_data_regexp(r'^solved')
))
bot.dispatcher.add_handler(BotButtonCommandHandler(
    callback=but_new_film,
    filters=Filter.callback_data_regexp(r'^new_film')
))
bot.dispatcher.add_handler(BotButtonCommandHandler(
    callback=but_new_character,
    filters=Filter.callback_data_regexp(r'^new_character')
))
bot.dispatcher.add_handler(BotButtonCommandHandler(
    callback=but_new_word,
    filters=Filter.callback_data_regexp(r'^new_word')
))
bot.dispatcher.add_handler(BotButtonCommandHandler(
    callback=but_level,
    filters=Filter.callback_data_regexp(r'^level')
))

bot.dispatcher.add_handler(StartCommandHandler(callback=send_start))
bot.start_polling()
bot.idle()
