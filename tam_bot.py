import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.enums import ParseMode
import random

# Замени с твоя Telegram bot token
API_TOKEN = "7

# Примерни Temu продукти с твоите affiliate линкове
PRODUCTS = [
        'https://www.temu.com/bg-en/plus-size-sexy-outfits-set-womens-plus-solid-lantern-sleeve-surplice-neck-crop-top-maxi-skirt-outfits-two-piece-set-g-601099525543534.html'
        'https://www.temu.com/bg-en/c/home-decor-products-o4-751.html'
        'https://www.temu.com/top-sellers-5020065319020-s.html'
        'https://www.temu.com/bg-en/shopping_category.html?r_pid=601099512475112&rps=10032'

  ]
bot = Bot(token=API_TOKEN)
dp = Dispatcher()



@dp.message()
async def reply_with_product(message: Message):
    product = random.choice(PRODUCTS)
    await message.answer(
        f"🛍 <b>{product['title']}</b>\n🔗 Поръчай сега: {product['url']}",
        parse_mode=ParseMode.HTML
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())
