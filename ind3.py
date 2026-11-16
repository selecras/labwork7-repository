def check_word(word: str, alphabet: str = "en") -> bool:
    if alphabet not in ("en", "rus"):
        raise ValueError("Non-existent alphabet")

    rus_alp = "".join(sorted("йцукенгшщзёхъфывапролджэячсмитьбю"))
    en_alp = "".join(sorted("qwertyuiopasdfghjklzxcvbnm"))

    alp = rus_alp if alphabet == "rus" else en_alp

    return all(let in alp for let in word if let.isalpha()) and word


def vigenere(word: str, key: str, alphabet: str = "en") -> str:
    word = word.lower()
    key = key.lower()

    if alphabet not in ("en", "rus"):
        raise ValueError("Non-existent alphabet")

    if not (check_word(word, alphabet) and check_word(key, alphabet)):
        raise ValueError("Wrong alphabet")

    if not key or not all(let.isalpha() for let in key):
        raise ValueError("Key must contain letters from the alphabet")

    rus_alp = "".join(sorted("йцукенгшщзёхъфывапролджэячсмитьбю")) * 2
    en_alp = "".join(sorted("qwertyuiopasdfghjklzxcvbnm")) * 2

    result = ""

    key = (key * (len(word) // len(key) + 1))[: len(word)]
    lst = rus_alp if alphabet == "rus" else en_alp
    for let_w, let_k in zip(word, key):
        if let_w not in lst:
            result += let_w
            continue

        ind_w = lst.find(let_w)
        ind_k = lst.find(let_k)
        result += lst[ind_w + ind_k]

    return result


if __name__ == "__main__":
    alphabet = input("Введите желаемый язык (en/rus): ").lower()
    while alphabet not in ("en", "rus"):
        print("Некорректный ввод")
        alphabet = input("Введите желаемый язык (en/rus): ").lower()

    word = input("Введите текст для шифрования: ").strip().lower()
    key = input("Введите ключевое слово: ").strip().lower()

    while not (word and key) or not (
        check_word(word, alphabet) and check_word(key, alphabet)
    ):
        print("\nНекорректный ввод")
        word = input("Введите текст для шифрования: ").strip().lower()
        key = input("Введите ключевое слово: ").strip().lower()

    print(vigenere(word, key, alphabet))
