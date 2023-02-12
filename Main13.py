
# Comments Менеджер <<With ... as>> для работы с файлами

# Example 1

try:
    with open("text.txt", "r", encoding="utf - 8") as file:      # encoding="utf - 8" - означает что мы можем считывать или же записывать символы на кирнилице или латинице
        print(file.read())                                       # with ...as - означет что файл чуть позже будет закрыт, то есть открыт и закрыт
except FileNotFoundError:                                        # open - открытие файла
    print("File not found")

# text.txt - файл необходимо создать перед работой с данными.







































