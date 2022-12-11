from telegram.ext import Updater,CommandHandler,CallbackQueryHandler,ConversationHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from googletrans import Translator


first = ''
second = ''
buttons_1=[
    [
        InlineKeyboardButton("O'zbek",callback_data="uz"),
        InlineKeyboardButton("Ingliz",callback_data="en"),
        InlineKeyboardButton("Rus",callback_data="ru")
    ]
]
buttons_2=[
    [
        InlineKeyboardButton("O'zbek",callback_data="uz"),
        InlineKeyboardButton("Ingliz",callback_data="en"),
        InlineKeyboardButton("Rus",callback_data="ru")
    ]
]

def tarjima(update,context):
    t = update.message.text
    if t == 'exit':
        update.message.reply_html("<b>1-tilni tanlang</b>",reply_markup=InlineKeyboardMarkup(buttons_1))
        return 1
    else:
        translator = Translator()
        b = translator.translate(t, src=first, dest=second)
        update.message.reply_text(b.text)
        return 3

def inline_callback(update,context):
    global first
    malumot = update.callback_query
    first = malumot.data
    malumot.message.delete()
    malumot.message.reply_html("<b>birinchi til {} ikkinchi tilni tanlang</b>".format(first), reply_markup=InlineKeyboardMarkup(buttons_2))
    return 2


def inline_callback2(update, context):
    global second
    malumot = update.callback_query
    second = malumot.data
    malumot.message.delete()
    malumot.message.reply_html("<b>birinchi til {} ikkinchi til {}</b> Matnni kiriting".format(first, second))
    return 3


def start(update,context):
    update.message.reply_html("<b>1-tilni tanlang</b>",reply_markup=InlineKeyboardMarkup(buttons_1))
    return 1

def main():
    updater = Updater("5401979701:AAGkqiXBi7K8L71LmqTEGNm0zf1yWsVwmXg",use_context=True)
    dispetcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [
                CallbackQueryHandler(inline_callback)
            ],
            2: [CallbackQueryHandler(inline_callback2)],
            3: [MessageHandler(Filters.text, tarjima)]
        },
        fallbacks=[CommandHandler('start', start)]
    )
    dispetcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__=="__main__":
    main()