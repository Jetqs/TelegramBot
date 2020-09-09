import telebot
import datetime
import random
import pickle


def open_predictions_file(filename):
    with open(filename, "rb") as file:
        predictions = pickle.load(file)
    return predictions


def save_predictions_file(data, filename):
    with open("predictions.dat", "wb") as file:
        pickle.dump(data, filename)


def get_prediction(predictions):
    predictionsCount = len(predictions)
    return predictions[random.randint(0, predictionsCount - 1)]


pathToFile = "predictions.dat"
predictions = open_predictions_file(pathToFile)
bot = telebot.TeleBot("966476344:AAFEZf1OFuJW-n8BN-e1gJUaMRLeihf6l6g")

@bot.message_handler(content_types=["text"])
def get_message(message):
    message_content = message.text.lower()

    print(datetime.datetime.now(), "Message:", message_content)
    if message_content == "/попытатьудачу":
        bot.send_message(message.from_user.id, get_prediction(predictions))
    elif message_content == "/help":
        bot.send_message(message.from_user.id, "Для получения предсказания напиши /ПопытатьУдачу")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")


bot.polling(none_stop=True, interval=0)
