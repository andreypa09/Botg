import os
PATH = 'files'
# print(os.path.exists("main.py")) # проверка папки, файла
os.makedirs(PATH, exist_ok=True) # создание директории
# if not os.path.exists(PATH):
#     os.makedirs(PATH)
# file_name = "test.txt"
# print(os.path.join(PATH, file_name)) # создание пути в директории