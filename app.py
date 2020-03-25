from chatterbot import ChatBot
import sys

bot = ChatBot(
    '小思',
    database_uri='sqlite:///db.sqlite3'
 )
 
#从请求中获取参数信息
user_input = sys.argv[1]

bot_response = bot.get_response(user_input)
print(bot_response)

