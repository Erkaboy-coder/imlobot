from connections import *
from checkWord import checkWord
from transliterate import to_cyrillic, to_latin

async def set_default_command(dp):
	await db.bot.set_default_command(
		[
			type.BotCommand("start","Bo'tni ishga tushirish"),
			type.BotCommand("help","Yordam")
		]
	)
async def on_startup(dispatcher):
	await set_default_command(dispatcher)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	await message.reply("Uz imlo botga xush kelibsiz")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
	await message.reply("Bu botdan foydalanish uchun krilchada so'z kiriting.")


@dp.message_handler()
async def checkImlo(message: types.Message):
	word = message.text
	javob = to_latin(word)

	result = checkWord(to_cyrillic(word))

	if result['available']:
		response = f"✅{javob.capitalize()}"
	else:
		response = f"❌{javob.capitalize()}\n"
		for text in result['matches']:
			response += f"✅{to_latin(text).capitalize()}\n"

	await message.answer(response)

if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)