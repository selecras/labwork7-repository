import json


def is_valid_json(text: str) -> bool:
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False


if __name__ == "__main__":
    a = input("Введите JSON-строку: ")
    if is_valid_json(a):
        print("JSON-строка валидна")
    else:
        print("JSON-строка невалидна")
