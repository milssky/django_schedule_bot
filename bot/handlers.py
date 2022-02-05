from aiogram import Bot, Dispatcher, executor, types

from django_bot.settings import BOT_API_TOKEN
from .models import Task, TgUser
from .logic import create_task, get_user_tasks, get_user_from_tg_id

bot_object = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot_object)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """Welcome message"""
    await message.reply("Hello! /register to start usage.")


@dp.message_handler(commands=['register'])
async def register_user(message: types.Message):
    """Register user handler"""
    user = message['from']
    user_id = user['id']
    fetch_user = await get_user_from_tg_id(user_id)
    if fetch_user.username == user['username']:
        await message.answer('You already registered')
    else:
        new_user = TgUser(
            username=user['username'],
            tg_user=user['id'],
            first_name=user['first_name'],
            last_name=user['last_name'],
        )
        await new_user.save()
        await message.answer('Registered')
    await message.answer('To see your day schedule use /day or /add to add day task.')


@dp.message_handler(commands=['day'])
async def day_command(message: types.Message):
    """Returns day schedule for user"""
    user = message['from']
    user_id = user['id']
    fetch_user = await get_user_from_tg_id(user_id)
    if fetch_user.username != user['username']:
        await message.answer('You\'re not registered!' )
        return
    tasks = await get_user_tasks(user_id)
    if len(tasks) == 0:
        await message.answer("No tasks. Just /add it.")
        return
    await message.answer(tasks)


@dp.message_handler(commands=['add'])
async def add_task_command(message: types.Message):
    user = message['from']
    user_id = user['id']
    fetch_user = await get_user_from_tg_id(user_id)
    if fetch_user.username != user['username']:
        await message.answer('You\'re not registered!')
        return
    await create_task(
        message.text[4:].strip(),
        fetch_user
    )
    await message.answer('Task added')
    await message.answer('To see your day schedule use /day or /add to add day task.')



@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Unknown command. Use /help or /start.")


def start():
    executor.start_polling(dp, skip_updates=True)
