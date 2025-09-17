What is Needed
Before you start, make sure you have prepared:
  1. Python 3.7 or later (can be checked with python --version)
  2. Access to Telegram
  3. Library python-telegram-bot

To install the library, use the following command :
  pip install python-telegram-bot --upgrade
  
Creating a Bot on Telegram :
  1. Open the Telegram app and search for the account @BotFather.
  2. Send the command /newbotand then follow the instructions.
  3. You will be asked to provide a name and username for the bot.
  4. Once completed, @BotFatherit will provide an API token . Keep this token safe as it will be used in your Python code.

Writing Telegram Bot Code
Create a new Python file named bot.py

Replace it YOUR_API_TOKEN_HEREwith the token from BotFather.

Running a Boat
Run the bot with the command:
  python3 bot.py
  
If successful, open the Telegram app, search for your bot's name, and send it a message /start. The bot will reply with a welcome message.

