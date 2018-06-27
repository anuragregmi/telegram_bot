## Telegram Bot
A simple Telegram Bot

### Arrributes:
  `bot`: A telepot bot.

### Methods:
  `handle_message`: Handles a chat message
  
  `handle_private_message`: Handles private messages
  
  `handle_group_message`: Handles group messages

### Usage:

```python

  # First of all create a telepot Bot.
  bot = telepot.Bot("TOKEN")

  # Then create a TelegramBot
  t_bot = TelegramBot(bot)

  # Then run telegram Bot
  t_bot.run_bot()

  Advanced:

  Override `handle_group_message` to handle group message your way and
  `handle_private_message` to handle private message your way
  
```
