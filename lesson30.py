import json

from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup

BUTTON1 = 'Sklad'
BUTTON2 = 'Sotib olish'
BUTTON3 = 'Qarz berish'

mahsulotlar = {
    'non':'2000 so\'m',
    'kola':'11000 so\'m',
    'olma': '15000 so\'m',
    'sut': '10000 so\'m',
    'sabzi': '7000 so\'m',

}

m_buttons = ReplyKeyboardMarkup([[BUTTON1], [BUTTON2], [BUTTON3]], resize_keyboard=True)

def start(update, context):
    username = update.message.from_user.first_name
    update.message.reply_html('Salom <b>{}</b>'.format(username), reply_markup=m_buttons)

    return 1

def sklad(update, context):
    malumotlar = ''
    n = 1
    for k, q in mahsulotlar.items():
        malumotlar += str(n) + '. ' + k.title() + ': ' + q + '\n\n'
        n+=1
    update.message.reply_html(malumotlar)


    return 1

def sotish(update, context):
    update.message.reply_html('Mahsulot nomini kiritib uni sotib oling')

    return 2

def qarz(update, context):
    username = update.message.from_user.first_name

    with open('qarzlara.json') as f:
        qarzdorlar = json.load(f)
        if username in qarzdorlar:
            update.message.reply_html('Qarzingiz bor ekan: {}. Qarzni berish uchun summani kiriting 🔽'.format(qarzdorlar[username]))
            return 3
        else:
            update.message.reply_html('Sizni qarzingiz mavjud emas', reply_markup=m_buttons)
            return 1


def berish(update, context):
    username = update.message.from_user.first_name
    summa = update.message.text
    with open('qarzlara.json') as f:
        qarzdorlar = json.load(f)
        qarz = qarzdorlar[username]
        qolgani = int(qarz) - int(summa)
        if qolgani <= 0:
            del qarzdorlar[username]
            with open('qarzlara.json', 'w') as fa:
                json.dump(qarzdorlar, fa)
        else:
            qarzdorlar[username] = str(qolgani)
            with open('qarzlara.json', 'w') as fa:
                json.dump(qarzdorlar, fa)

        update.message.reply_html('Qarzingiz berildi. Qolgan qarzingiz {} so\'m'.format(qolgani))

    return 1


def add(update, context):
    m = update.message.text
    if m.lower() in mahsulotlar:
        username = update.message.from_user.first_name
        data = {
            'name': username,
            'tovar': m
        }
        with open('items.json', 'a') as f:
            json.dump(data, f)
        update.message.reply_html('Mahsulotni sotib oldingiz, admin siz bilan boglanadi', reply_markup=m_buttons)
        return 1
    else:
        update.message.reply_html('Bu tovar bizda mavjud emas, boshqa mahsulot sotib olishingiz mumkin, skladni koring')
        return 1

def main():
    updater = Updater('5401979701:AAGkqiXBi7K8L71LmqTEGNm0zf1yWsVwmXg', use_context=True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [
                MessageHandler(Filters.regex('^(' + BUTTON1 + ')$'), sklad),
                MessageHandler(Filters.regex('^(' + BUTTON2 + ')$'), sotish),
                MessageHandler(Filters.regex('^(' + BUTTON3 + ')$'), qarz)

            ],
            2: [
                MessageHandler(Filters.text, add)
            ],
            3: [
                MessageHandler(Filters.text, berish)
            ]

        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ =='__main__':
    main()

