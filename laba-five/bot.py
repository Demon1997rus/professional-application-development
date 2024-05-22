import telebot
from peewee import *
import config
import re

bot = telebot.TeleBot(config.apikey)

# Подключение к базе данных
db = SqliteDatabase(config.db_path)


class BaseModel(Model):
    class Meta:
        database = db


class Group(BaseModel):
    name = CharField(unique=True)


class Student(BaseModel):
    full_name = CharField()
    email = CharField(unique=True)
    group = ForeignKeyField(Group, backref='students')
    age = IntegerField()


db.connect()


# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Введите /help для списка доступных команд.")


# Команда /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "/add_group <name> - Добавить новую группу\n"
        "/add_student <ФИО> <email> <группа> <возраст> - Добавить нового студента\n"
        "/list_students - Показать список всех студентов\n"
    )
    bot.reply_to(message, help_text)


# Команда для добавления группы
@bot.message_handler(commands=['add_group'])
def add_group(message):
    try:
        group_name = message.text.split()[1]
        group, created = Group.get_or_create(name=group_name)
        if created:
            bot.reply_to(message, f"Группа '{group_name}' добавлена.")
        else:
            bot.reply_to(message, f"Группа '{group_name}' уже существует.")
    except IndexError:
        bot.reply_to(message, "Пожалуйста, укажите название группы.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")


# Команда для добавления студента
@bot.message_handler(commands=['add_student'])
def add_student(message):
    try:
        command_text = message.text[len('/add_student '):]
        match = re.match(r'^(.+)\s+(\S+@\S+)\s+(.+)\s+(\d+)$', command_text)

        if not match:
            bot.reply_to(message, "Пожалуйста, укажите все данные в формате: ФИО, email, группа, возраст.")
            return

        full_name, email, group_name, age = match.groups()
        age = int(age)

        group = Group.get_or_none(Group.name == group_name)
        if not group:
            bot.reply_to(message, f"Группа '{group_name}' не найдена.")
            return
        student = Student.create(full_name=full_name, email=email, group=group, age=age)
        bot.reply_to(message, f"Студент '{full_name}' добавлен.")
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка: {e}")


# Команда для отображения списка студентов
@bot.message_handler(commands=['list_students'])
def list_students(message):
    students = Student.select()
    if not students:
        bot.reply_to(message, "Студентов нет.")
        return

    response = "Список студентов:\n"
    for student in students:
        response += f"№ {student.id}: {student.full_name}, {student.email}, Группа: {student.group.name}, Возраст: {student.age}\n"

    bot.reply_to(message, response)


# Запуск бота
bot.polling()
