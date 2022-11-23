from collections import Counter

russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
russian_alphabet_length = len(russian_alphabet)
english_alphabet_length = len(english_alphabet)

actual_frequency = {'а': 8.01, 'б': 1.59, 'в': 4.54, 'г': 1.7, 'д': 2.98, 'е': 8.45, 'ё': 0.04, 'ж': 0.94, 'з': 1.65,
                    'и': 7.35, 'й': 1.21, 'к': 3.49, 'л': 4.40, 'м': 3.21, 'н': 6.70, 'о': 10.97, 'п': 2.81, 'р': 4.73,
                    'с': 5.47, 'т': 6.62, 'у': 2.62, 'ф': 0.26, 'х': 0.97, 'ц': 0.48, 'ч': 1.44, 'ш': 0.73, 'щ': 0.36,
                    'ъ': 0.04, 'ы': 1.90, 'ь': 1.74, 'э': 0.32, 'ю': 0.64, 'я': 2.01}


def CeaserEncrypting(path_in, shift, path_out):
    with open(path_in, encoding='UTF8') as file, open(path_out, mode='w', encoding='UTF8') as out:
        for line in file:
            line = line.lower()
            for symbol in line:
                if symbol in english_alphabet:
                    idx = english_alphabet.index(symbol)
                    out.write(english_alphabet[(idx + shift) % english_alphabet_length])
                if symbol in russian_alphabet:
                    idx = russian_alphabet.index(symbol)
                    out.write(russian_alphabet[(idx + shift) % russian_alphabet_length])
                else:
                    out.write(symbol)

def CeaserDecrypting(path, shift, path_out):
    CeaserEncrypting(path, -shift, path_out)


def CeaserHack(path_in, path_out):
    with open(path_in, encoding='UTF8') as file:
        text = file.read()
        frequency = Counter(text.lower())
        max_frequency_rus = 0
        max_frequency_eng = 0
        max_idx_rus = -1
        max_idx_eng = -1
        for symbol in frequency.keys():
            if symbol in english_alphabet:
                if frequency[symbol] > max_frequency_eng:
                    max_frequency_eng = frequency[symbol]
                    max_idx_eng = english_alphabet.index(symbol)
            if symbol in russian_alphabet:
                if frequency[symbol] > max_frequency_rus:
                    max_frequency_rus = frequency[symbol]
                    max_idx_rus = russian_alphabet.index(symbol)
        eng_shift = max_idx_eng - english_alphabet.index('e')
        rus_shift = max_idx_rus - russian_alphabet.index('о')
        if max_frequency_rus >= max_frequency_eng:
            CeaserDecrypting(path_in, rus_shift, path_out)
        else:
            CeaserDecrypting(path_in, eng_shift, path_out)

