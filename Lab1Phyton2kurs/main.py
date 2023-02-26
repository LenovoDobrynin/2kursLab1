import random
import math
import datetime


def p1():
    tmp = input("Enter a real number: ")

    if float(tmp) < 0:
        print("Negative number")
    else:
        rubles, coins = tmp.replace(',', '.').split('.')
        print(f"{rubles} руб. {coins} коп.")


def p2():
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 4, 3, 2, 1]
    print("Array #1: ", arr1)

    for i in range(len(arr1)-1):
        if arr1[i] <= arr1[i+1]:
            print("True")
        else:
            print("False")


def p3():
    karta = input("Enter the card numbers (without spaces): ")
    if len(karta) != 16:
        print("wrong format of card number")
    else:
        res = karta[:4] + '#'*8 + karta[-4:]
        print(res)


def p4():
    text = input("Type some text: ")
    words = text.replace('.', ' ').replace(',', ' ').split(' ')
    res1 = []
    res2 = []
    res3 = []
    for word in words:
        if len(word) > 7:
            res1.append(word)
        elif len(word) >=4 and len(word) <=7:
            res2.append(word)
        else:
            res3.append(word)
    print(res1, res2, res3)


def p5():
    text = input('Type some text: ')
    words = text.replace(',', ' ').replace('.', ' ').split(' ')
    res = []
    for word in words:
        letter = word[0]
        if letter.title() == letter:
            res.append(word.upper())
        else:
            res.append(word)
    print(' '.join(res))


def p6():
    text = input("Type some text: ")
    res = []
    for symbol in text:
        if text.count(symbol) == 1:
            res.append(symbol)

    print("symbols, that count is 1: ", ' '.join(res))


def p7():
    sites = ['www.google.com', 'vk.com', 'www.ya.ru', 'donnu.ru']
    tmp = []
    for site in sites:
        if 'www.' in site:
            tmp.append(f'http://{site}')
        else:
            tmp.append(f'https://www.{site}')

    res = []
    for site in tmp:
        if site.endswith('.com'):
            res.append(site)
        else:
            res.append(f'{site}.com')

    print(res)


def p8():
    arr = [random.randint(1, 100) for _ in range(0, random.randint(1, 100))]
    length = 2 ** math.ceil(math.log2(len(arr)))  # магическая формула для поиска ближайшей степени двойки
    print(arr)
    [arr.append(0) for _ in range(len(arr), length)]
    print(arr)


def p9():
    bank = {1000: 20, 500: 10, 100: 10, 50: 10}
    bank_summ = sum(x * y for x, y in bank.items())
    print("ATM Machine balance: ", bank_summ)
    request = int(input("Type cash that u want: "))
    if request % 50 != 0:
        print("You need to type some num, multiple of 50")
    else:
        for nominal in bank.keys():
            _tmp = int(request / nominal) // 1 if int(request / nominal) // 1 <= bank[nominal] else bank[nominal]
            request = request - (_tmp * nominal)
            bank[nominal] = _tmp
        print(str(bank).replace(': ', '*').replace(', ', ' + '))


def p10():
    pwd = 't3st'
    if len(pwd) < 8:
        print('bad password')
    elif pwd.isdigit():
        print('bad password')
    elif pwd.isalpha():
        print('bad password')
    else:
        print('good password')


def frange(x: int, y: int, z: float):
    while x <= (y - z):
        yield float('{:.1f}'.format(x + z))
        x = x + z

def p11():
    for x in frange(1, 3, 0.1):
        print(x, end='\t')


def get_frames(signal: list, size=1024, overlap=0.5):
    length = int(size * overlap)
    step = 0

    while step < len(signal) - 1:
        yield signal[step: step + size]
        step += length


def p12():
    length = int(input('type len of signal: '))
    signal = [x for x in range(length)]
    for frame in get_frames(signal, 4, 0.5):
        print(frame)


def extra_enumerate(x):
    tmp = 0
    for y in x:
        tmp += y
        yield y, tmp, tmp / sum(x)


def p13():
    x = [1, 2, 3, 4]
    for elem, summ, frac in extra_enumerate(x):
        print(elem, summ, frac)


def non_empty(func):
    def wrap():
        ret = func()
        removed = 0

        for x in ret:
            if x is None or x == '':
                ret.pop(removed)
            removed += 1
        return ret

    return wrap


@non_empty
def getList():
    return ['1', '', '2', 3, '', 4]


def p14():
    print(getList())


def pre_proccess(a=0.97):
    def decorator(func):
        def wrap(*args):
            s = args[0]
            for x in range(len(s)):
                s[x] = s[x] - a * s[x - 1]
                func(s)
        return wrap
    return decorator


@pre_proccess(a=0.95)
def plot_signal(s):
    for sample in s:
        print(sample)


def p15():
    signal = [1, 1, 2, 3, 4, 5, 8, 10, 15, 20, 25, 31]
    plot_signal(signal)


def p16():
    teams = ['Liverpool', 'Dynamo-Kiev', 'Dynamo-Piter', 'PSG',
             'Real Madrid', 'Barselona', 'Arselan', 'Baltika',
             'Juventus', 'Chelsi', 'Milan', 'Bavaria',
             'Borussia', 'Shakhtar', 'Manchester', 'Zenit']
    playDate = datetime.datetime(2023, 2, 16, 19, 00)

    random.shuffle(teams)
    groups = [teams[x * 4: x * 4 + 4] for x in range(4)]
    [print('Group # ', x + 1, ': ', groups[x]) for x in range(len(groups))]

    for x in range(len(teams)):
        print('Game # ', x, ': ', playDate.strftime("%d/%m/%Y %H:%M"))
        playDate += datetime.timedelta(days=14)


def main():
    points = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16]

    for point in points:
        point()


if __name__ == '__main__':
    main()

