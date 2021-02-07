#!/bin/env python3
from vkbottle.bot import Bot, Message
from typing import Optional


bot = Bot("7f12ba6623387c37c610fe178f282436daab6e78445e5152f2cdb16626e286fee8999525ce36fba8fde2d")

alp = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

def encrypt(key, text):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            try:
                mj = alp.index(ch)
                kj = alp.index(key[(index - space) % len(key)])
                cj = (mj + kj) % len(alp)
                result.append(alp[cj])
            except ValueError:
                return "Err"
        else:
            space += 1
            result.append(' ')
    return ''.join(result)

def decrypt(key, text):
    result = []
    space = 0
    for index, ch in enumerate(text):
        if ch != ' ':
            try:
                cj = alp.index(ch)
                kj = alp.index(key[(index - space) % len(key)])
                mj = (cj - kj) % len(alp)
                result.append(alp[mj])
            except ValueError:
                return "Err"
        else:
            space += 1
            result.append(' ')
    return ''.join(result)
    
@bot.on.message(text="шифр <key> <text>")
async def handler(message: Message, key: Optional[str] = None, text: Optional[str] = None) -> str:
        if encrypt(key, text) == "Err":
            return "разрешенно использование только букв"
        else:
            return f"Ваш зашифрованный текcт: {encrypt(key, text)}"
    
@bot.on.message(text="дешифр <key> <text>")
async def handler(message: Message, key: Optional[str] = None, text: Optional[str] = None) -> str:
    if decrypt(key, text) == "Err":
        return "разрешенно использование только букв"
    else:
        return f"Ваш зашифрованный текcт: {decrypt(key, text)}"

@bot.on.message()
async def handler(_) -> str:
    return "Привет! Доступны 2 команды:\n шифр ключ текст\nдешифр ключ текст"

bot.run_forever()