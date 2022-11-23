import random

combined_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' \
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:-!?_;\"'
alphabet_length = len(combined_alphabet)


def VernamEncrypting(path_in, path_out, path_key):
    with open(path_in, encoding='UTF8') as file, \
            open(path_out, mode='w', encoding='UTF8') as out, open(path_key, encoding='UTF8', mode='w') as key:
        print(alphabet_length)
        for line in file:
            for symbol in line:
                if symbol in combined_alphabet:
                    key_number = random.randrange(0, alphabet_length)
                    idx = combined_alphabet.index(symbol)
                    key.write(combined_alphabet[key_number])
                    out.write(combined_alphabet[key_number ^ idx])
                else:
                    out.write(symbol)


def VernamDecrypting(path_in, path_out, path_key):
    with open(path_in, encoding='UTF8') as file, \
            open(path_out, mode='w', encoding='UTF8') as out, open(path_key, encoding='UTF8', mode='r') as key_file:
        key = key_file.read()
        key_count = 0
        for line in file:
            for symbol in line:
                if symbol in combined_alphabet:
                    key_number = combined_alphabet.index(key[key_count])
                    idx = combined_alphabet.index(symbol)
                    out.write(combined_alphabet[key_number ^ idx])
                    key_count += 1
                else:
                    out.write(symbol)

