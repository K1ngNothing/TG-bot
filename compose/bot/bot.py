from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

THE_PUNISHMENT="https://rr4---sn-jvhnu5g-c35d.googlevideo.com/videoplayback?expire=1671890673&ei=kbKmY8LHDcWN2LYPv7GQqA4&ip=161.0.31.185&id=o-AJ2oaK4UfGeNITqWiGxgLgk-VUajqzkF0JjmdZAwKrNt&itag=18&source=youtube&requiressl=yes&spc=zIddbKkevB4_7XltRfEevi48ArZMEVg&vprv=1&mime=video%2Fmp4&ns=ZSJ00ezFFWbOEpfIvstmwaEK&cnr=14&ratebypass=yes&dur=212.091&lmt=1665516961425965&fexp=24001373,24007246&c=WEB&txp=4530434&n=DRBxkOZTjgwj8w&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgE1MN6MAoEDMl8elGc5uQtVBIUt3f0KZMFj6fM1lHgR8CIDlxV0YbqZwKFGBz2gtqiwOWsvWu1qrXZPOzdSnzRJs1&redirect_counter=1&rm=sn-ab5eez7s&req_id=afd02a6ff183a3ee&cms_redirect=yes&cmsv=e&ipbypass=yes&mh=7c&mip=79.139.143.91&mm=31&mn=sn-jvhnu5g-c35d&ms=au&mt=1671874410&mv=m&mvi=4&pl=17&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgZwSO8Ebep5SngNoQhIYktRfebfyobehYEe0ZNcAojD0CIQDk6SrtfQGzPFXkFo3SpDlaNxn26lDuxq08UqceR0Kzkg%3D%3D"

COOL_CAT="https://images.unsplash.com/photo-1533738363-b7f9aef128ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8NHx8fGVufDB8fHx8&w=1000&q=80"

CUTE_CAT="https://i.pinimg.com/originals/d3/be/08/d3be083885874b41ff1d50fc946c666a.png"

SLEEPING_CAT="https://media-be.chewy.com/wp-content/uploads/sleeping-kitten-TS_160626325.jpg"


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Hi!\nHow ya doing?")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("/start: starts this bot\n"
                        "/help: prints this message\n"
                        "/hello_world: you will never guess what it does\n"
                        "/cute_cat, /cool_cat, /sleeping_cat: they are soooo cute)\n"
                        "/xxx_videos: just don't do this")


@dp.message_handler(commands=['hello_world'])
async def hello_world_command(message: types.Message):
    await message.reply("Hello World!")


@dp.message_handler(commands=['cute_cat'])
async def process_group_command(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(CUTE_CAT)
    await message.reply_media_group(media=media)


@dp.message_handler(commands=['cool_cat'])
async def process_group_command(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(COOL_CAT)
    await message.reply_media_group(media=media)


@dp.message_handler(commands=['sleeping_cat'])
async def process_group_command(message: types.Message):
    media = types.MediaGroup()
    media.attach_photo(SLEEPING_CAT)
    await message.reply_media_group(media=media)


@dp.message_handler(commands=['xxx_videos'])
async def process_group_command(message: types.Message):
    media = types.MediaGroup()
    media.attach_video(THE_PUNISHMENT)
    await message.reply_media_group(media=media)


if __name__ == '__main__':
    executor.start_polling(dp)
