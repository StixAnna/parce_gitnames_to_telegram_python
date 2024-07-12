# %%
import os
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')
from telethon import TelegramClient
from datetime import datetime

# %%

# Загрузка переменных окружения из файла .env
load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
telegram_chat_url = os.getenv('TELEGRAM_CHAT')

start_date = datetime(2018, 3, 29) # start_analyse_date
chatname = telegram_chat_url.split('/')[3]

with TelegramClient('session', api_id, api_hash) as client:
    # Получаем все сообщения из чата starts at date 'start_date'
    all_messages = client.iter_messages(telegram_chat_url, reverse=True, offset_date=start_date)
    unique_user_ids = []

    for message in all_messages:
      try:
        if message.sender is not None: 
          if message.sender.username:   # если юзернейм у пользователя есть
            unique_user_ids.append(message.sender.username.lower())
      except Exception as e:            # ошибка если сообщение не от обычного пользователя
        print(f"Произошла ошибка: {e}")
    out_list = list(set(unique_user_ids))

    with open(f"out_users_{chatname}.csv", "w") as txt_file:
        txt_file.write(", ".join(out_list) + "\n")


# %%
