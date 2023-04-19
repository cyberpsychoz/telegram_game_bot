from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "ваш токен от бота здесь"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Создаем клавиатуру с двумя кнопками
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('Дверь 1')
btn2 = types.KeyboardButton('Дверь 2')
keyboard.add(btn1, btn2)

# Создаем переменную для хранения выбора игрока
choice = None

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    global choice # Объявляем переменную глобальной, чтобы изменять ее значение
    choice = None # Сбрасываем выбор игрока при начале игры
    await msg.reply(f'Я бот. Приятно познакомиться, {msg.from_user.first_name}')
    await msg.answer('Вы находитесь в темной комнате с двумя дверями. За какую дверь вы пойдете?', reply_markup=keyboard)

@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    global choice # Объявляем переменную глобальной, чтобы изменять ее значение
    if msg.text == 'Дверь 1':
        choice = 'Дверь 1' # Запоминаем выбор игрока
        await msg.answer('Вы открыли дверь 1 и увидели золото. Вы богаты!')
    elif msg.text == 'Дверь 2':
        choice = 'Дверь 2' # Запоминаем выбор игрока
        await msg.answer('Вы открыли дверь 2 и увидели дракона. Вы мертвы!')
    elif msg.text.lower() == 'конец':
        if choice == 'Дверь 1': # Проверяем выбор игрока
            await msg.answer('Вы счастливо жили со своим золотом.')
        elif choice
