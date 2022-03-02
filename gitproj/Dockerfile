#Какой базовый образ взять за основу
FROM python:3.10-alpine

#Какую директорию сделать рабочей
WORKDIR /app

#Какой порт открыть
EXPOSE 8000

#Обновить линукс пакет
#RUN apt-get update && apt-get install -y

#RUN python -m pip install --upgrade pip

#Позволяет скопировать файлы с папки где dockerfile в линукс
ADD . /app

#Отвечает за то, что какая команда будет выполняться при запуске контейнера.
#Точка входа в проект. Выполняет команды на старте контейнера
ENTRYPOINT ["python"]

#Выполнить команду ЕСЛИ НЕТ ENTRYPOINT.
CMD ["some4.py"]