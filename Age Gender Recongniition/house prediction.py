from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot named "MyBot"
chatbot = ChatBot(name="MyBot", read_only=True, logic_adapters=["chatterbot.logic.BestMatch"])

# Train the chatbot using the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Get a response from the chatbot
response = chatbot.get_response("What is your name?")
print("MyBot: ", response)