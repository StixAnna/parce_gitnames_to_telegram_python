# Parcing gitnames-to-telegram

here is a py script that can parce telegram-usernames and compare this to githubContributors-usernames
it can be useful for HR who want to take personal telegram-usernames of many contributors participating in the development of projects on a topic

### Using

Firstly, need to create `.env` file and fill it like `env.example`

- `bsoup_repositories_take.py` taking repositories-names for your querry in `texttofind`
- `api_gittakenames.py` collecting githubContributors-usernames from projects found by `bsoup_repositories_take.py`
- `collect_Tg_Msgs_usernames.py` taking telegram-usernames from telegram-chat `TELEGRAM_CHAT`
- `compare_GitToTelegram.py` comparing results to find matches