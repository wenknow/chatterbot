from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("小思")
trainer = ListTrainer(chatbot)
with open('part.data', encoding='utf-8') as f:
  data = f.read().replace('\t', '\n')
data = data.split("\n")
trainer.train(data)
