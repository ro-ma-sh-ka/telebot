# <p align="center">@FamilyChatikBot <a>1.0</a>

<p align="center">Band member counter and some entertainment</p>

## Contents

  * [Getting started](#getting-started)
  * [General API Documentation](#general-api-documentation)
  * [Database structure](#database-structure)
  * [List of commands](#list-of-commands)
  * [Questions and suggestions](#questions-and-suggestions)

## Getting started
Download this Api and run
```
main.py
```

## General API Documentation
* DB - PostgreSQL
* ORM - SQLAlchemy
* Bot - Telegram Bot API (https://core.telegram.org/bots/api)

## Database structure
```
Table name: my_family
```
### Columns
* id, type - Integer, primary_key=True, autoincrement=True
* name, type - String(20), nullable=False
* surname, type - String(30), nullable=True
* birthday, type - Date, nullable=False
* created_on, type - DateTime, default=datetime.now

## List of commands
* /help - list of commands
* /hello - new member introduction
* /who_is_there - list of members
* /weather - weather forcast

## Questions and suggestions
Please send it to:
* e-mail: roma.l@mail.ru
* telegram: @Ro_ma_sh_ka
