import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import logging

# Инициализация бота с вашим токеном
bot = Bot(token="")
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Используй команду /dynamic для тестирования динамических кнопок.")


# Обработчик команды /dynamic
@dp.message(Command("dynamic"))
async def dynamic_command(message: Message):
    # Создание инлайн-кнопки "Показать больше"
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
    ])

    await message.answer("Нажми на кнопку ниже:", reply_markup=inline_keyboard)


# Обработчик нажатий на инлайн-кнопки
@dp.callback_query()
async def handle_dynamic_callback(query: CallbackQuery):
    action = query.data

    if action == "show_more":
        # Заменяем кнопку на "Опция 1" и "Опция 2"
        inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Опция 1", callback_data="option_1")],
            [InlineKeyboardButton(text="Опция 2", callback_data="option_2")]
        ])

        # Обновляем сообщение с новыми кнопками
        await query.message.edit_text("Выберите опцию:", reply_markup=inline_keyboard)

    elif action == "option_1":
        # Ответ на выбор "Опция 1"
        await query.message.edit_text("Вы выбрали Опцию 1")

    elif action == "option_2":
        # Ответ на выбор "Опция 2"
        await query.message.edit_text("Вы выбрали Опцию 2")


# Основная функция для запуска бота
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
