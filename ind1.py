from pathlib import Path

PATH = "log_sample.txt"


def get_log(level: str, path: str, encoding: str = "utf-8") -> list:
    result = []
    try:
        with open(path, "r", encoding=encoding) as f:
            data = f.read().strip()
    except OSError, UnicodeDecodeError:
        return result
    data = [i for i in data.split("\n") if f"[{level}]" in i]

    return data


if __name__ == "__main__":
    flag = True
    print("Получение записей определённого уровня")
    level = input("Введите уровень: ").upper().strip()

    while level not in ("INFO", "ERROR", "WARNING", "DEBUG", "CRITICAL"):
        print("Некорректный ввод")
        level = input("Введите уровень: ").upper()

    result = get_log(level, PATH)
    if result:
        if Path("result.txt").exists():
            print("\nВНИМАНИЕ! Файл result.txt уже существует")
            ans = input("Перезаписать данные? (y/n): ").lower().strip()
            while ans not in ("y", "n"):
                print("Некорректный ввод")
                ans = input("Перезаписать данные? (y/n): ").lower()
            if ans == "n":
                flag = False
            print()

        if flag:
            try:
                with open("result.txt", "w", encoding="utf-8") as f:
                    f.write("\n".join(result))
                print("Результат успешно записан в файл result.txt")
            except OSError, UnicodeError:
                print("Не удалось записать данные в файл. Вывод на экран:")
                for i in result:
                    print(i)
        else:
            print("Вывод на экран:")
            for i in result:
                print(i)
    else:
        print("Записей нет или файл не удалось прочитать")
