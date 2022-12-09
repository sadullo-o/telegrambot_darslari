# pip install python-telegram-bot
from lesson26 import get_info
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, Filters

BTN_TODAY = 'Boshqa viloyatni tanlash'
BTN_ERTAGA = "Og'iz ochish duosi"
BTN_WEEK = "Og'iz yopish duosi"
BTN_MONTH = "Ramazon oyi haqida"
ENG = 'ingliz tili'

main_buttons = ReplyKeyboardMarkup([
    [ENG], [BTN_ERTAGA, BTN_WEEK], [BTN_MONTH]
], resize_keyboard=True)

STATE_ONE = 1
STATE_TWO = 2
STATE_THREE = 3

viloyatlar = [ 'Andijon', 'Buxoro', 'Fargona', 'Jizzax', 'Namangan', 'Navoiy', 'Qashqadaryo',
               'Xorazm', 'Samarqand', 'Sirdaryo', 'Surxondaryo', 'Toshkent', 'Qoraqalpogiston']


buttons = []
v_detail = []

for j in range(0, 12,2):
    v_detail = []
    for i in range(j, j+2):
        v_detail.append(InlineKeyboardButton(f'{viloyatlar[i]}', callback_data=f'{viloyatlar[i].lower()}'))
    buttons.append(v_detail)

v_detail = []

v_detail.append(InlineKeyboardButton(f'{viloyatlar[12]}', callback_data=f'region12'))
buttons.append(v_detail)



def start(update, context):
    user = update.message.from_user
    update.message.reply_html('<b>Salom</b> {} <i>botimizga</i> xush kelibsiz'
                              .format(user.first_name), reply_markup=InlineKeyboardMarkup(buttons))
    return 1


def xayr(update, context):
    update.message.reply_text('Xayr!')


def inline_callback(update, context):
    malumot = update.callback_query
    viloyat = malumot.data
    infos = get_info(viloyat)
    print(infos)
    print(viloyat)
    malumotlar = ''
    for i in infos:
        malumotlar += i + '\n'
    malumot.message.delete()
    malumot.message.reply_html(f'{malumotlar}', reply_markup=main_buttons)
    return 2


def today(update, context):
    update.message.reply_text('Boshqa viloyatni tanlang', reply_markup=InlineKeyboardMarkup(buttons))
    return 1


def ertaga(update, context):
    malumot = 'Ro‘za tutish (saharlik, og‘iz yopish) duosi\n\
<b>Navaytu an asuvma sovma shahro ramazona minal fajri ilal mag‘ribi, xolisan lillahi ta’aalaa, Allohu akbar.</b>\n\
Ma’nosi: Ramazon oyining ro‘zasini subhdan to kun botguncha tutmoqni niyat qildim.Xolis Alloh uchun Alloh buyukdir.'
    update.message.reply_html(malumot)
    return 1

def haftalik(update, context):
    malumot = ''
    update.message.reply_text(malumot)
    return 3


def oylik(update, context):
    malumot = ''
    update.message.reply_text(malumot)
    return 3

def main():
    updater = Updater('5537275802:AAGaVLbzpIGljkYlTEGB7NQTliIwATJLPYM', use_context=True)

    dispetcher = updater.dispatcher

    # dispetcher.add_handler(CommandHandler('start', start))
    # dispetcher.add_handler(CommandHandler('xayr', xayr))

    # dispetcher.add_handler(CallbackQueryHandler(inline_callback))
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            STATE_ONE: [CallbackQueryHandler(inline_callback)],
            STATE_TWO: [
                MessageHandler(Filters.regex('^(' + BTN_TODAY + ')$'), today),
                MessageHandler(Filters.regex('^(' + BTN_ERTAGA + ')$'), ertaga),
                MessageHandler(Filters.regex('^(' + BTN_WEEK + ')$'), haftalik),
                MessageHandler(Filters.regex('^(' + BTN_MONTH + ')$'), oylik)
            ],
            STATE_THREE: [CommandHandler('xayr', xayr)]
        },
        fallbacks=[CommandHandler('start', start)]
    )

    dispetcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
