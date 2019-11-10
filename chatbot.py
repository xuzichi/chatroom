from chatterbot import ChatBot

bot = ChatBot(
    'my-chat',
    database_uri='sqlite:///db.sqlite3'
)

print('Type something to begin...')

while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
