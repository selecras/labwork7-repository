import re


def count_words(text: str) -> int:
    """Подсчитывает количество слов в тексте."""
    return len(text.split())


def count_words_clean(text: str) -> int:
    words = re.findall(r"\b\w+\b", text)
    return len(words)


text = input("Введите текст: ")
print(f"Количество слов: {count_words(text)}")

print(f"Слов (с пунктуацией): {count_words(text)}")
print(f"Слов (без пунктуации): {count_words_clean(text)}")
