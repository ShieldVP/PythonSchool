# Создаём своего бота в Telegram

Для начала зарегистрируем его у [BotFather](https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D1%91%D1%81%D1%82%D0%BD%D1%8B%D0%B9_%D0%BE%D1%82%D0%B5%D1%86_(%D1%84%D0%B8%D0%BB%D1%8C%D0%BC))'a в https://t.me/BotFather.
Токен, который он отправит очень важен -- это ключ для управления ботом.

Создаём проект в PyCharm, там и будет жить код.
Установим библиотеку, с помощью которой будем общаться с Telegram'ом, для этого откройте терминал или командную строку и наберите:


```bash
pip install pytelegrambotapi 
```

Теперь в `main.py` нужно
* импортировать нашу библиотеку `import telebot`
* завести строку, в которой будет храниться токен
* создать объект бота `bot = telebot.TeleBot(TOKEN)`
* определить действия бота в функциях с нужными хэдлерами
* запустить бота `bot.infinity_polling()`

Всё остальное и функции в хэндлерах зависят от того, что вы хотите сделать. Библиотека довольно обширная, поэтому ограничимся парой примеров, а остальное по мере нужды можно искать самому, благо названия говорящее.

Есть [документация](https://pytba.readthedocs.io/ru/latest/index.html) на русском