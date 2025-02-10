from sqlalchemy import create_engine
import os

# Получаем строку подключения из переменной окружения
connection_string = os.getenv("CONNECTION_STRING")

# Создаем движок SQLAlchemy
engine = create_engine(connection_string)

# Подключаемся к базе данных
try:
    connection = engine.connect()
    print("Успешное подключение к базе данных!")

    # Пример выполнения запроса
    result = connection.execute("SELECT version()")
    db_version = result.fetchone()
    print("Версия базы данных:", db_version)

    # Закрываем соединение
    connection.close()
except Exception as err:
    print(f"Ошибка подключения к базе данных: {err}")