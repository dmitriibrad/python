import random


def jokes(n, var):
    while var <= n:
        a = random.choice(nouns)
        nouns.remove(a)
        b = random.choice(adverbs)
        adverbs.remove(b)
        c = random.choice(adjectives)
        adjectives.remove(c)
        list_joke.append(f'{a} {b} {c}')
        var += 1
    return print(list_joke)


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_joke = []
n = int(input('Введите n шуток: '))
i = 1
jokes(n, i)
