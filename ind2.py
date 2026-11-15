def analysis(text: str) -> dict:
    text = list(text.lower())

    for i in range(len(text)):
        if not text[i].isalpha():
            text[i] = " "

    text = "".join(text)
    text = text.split()
    result = {}

    for word in text:
        result[word] = result.get(word, 0) + 1

    result = dict(sorted(result.items(), key=lambda x: x[1])[::-1])

    return result


if __name__ == "__main__":
    a = input("Введите произвольный текст: ").strip()
    while not a:
        a = input("Введите произвольный текст: ").strip()

    res = analysis(a)

    print("\nСписок победителей:")
    counter = 1
    for i in res:
        if counter > 10:
            break

        print(f"{counter}) {i} -- {res[i]} раз")
        counter += 1
